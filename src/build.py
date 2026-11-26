#!/usr/bin/env python3
"""Gera o site em public/ a partir de posts/*.md.

Uso: python3 src/build.py [--drafts] [--sem-grade]
  --sem-grade pula a conferência da grade (src/grade_test.py); sem ela o build falha se algo sair do quadriculado.
  --drafts inclui os posts com status: draft (só para prévia, nunca para o push).

Saída: public/index.html (lista de posts) e public/posts/<slug>.html.
"""
import glob, html, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DRAFTS = "--drafts" in sys.argv
import time as _t
VERSAO = str(int(_t.time()))
SITE = "Symphony of the Night for Mega CD"


def front(raw):
    _, fm, body = raw.split("---", 2)
    meta = dict(re.findall(r'^(\w+):\s*"?(.*?)"?\s*$', fm, re.M))
    return meta, body


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\[\[(.*?)\]\]", r'<span class="note">\1</span>', t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', t)
    t = t.replace("\\*", "\0")  # \* é asterisco de verdade, não itálico
    t = re.sub(r"(?<![\w/])\*(.+?)\*(?![\w])", r"<em>\1</em>", t)
    return t.replace("\0", "*")


def img_name(f):
    base = re.sub(r"\.(png|jpg|gif|mp4)$", "", f)
    for ext in (".jpg", ".png", ".gif", ".mp4"):
        if os.path.exists(os.path.join(ROOT, "public", "img", base + ext)):
            return base + ext
    raise SystemExit("imagem faltando em public/img: " + f)


def render(body):
    # blocos de código primeiro, para as linhas em branco dentro deles não quebrarem o bloco
    codes = []
    def keep(m):
        codes.append(m.group(1))
        return f"\n\n@@CODE{len(codes) - 1}@@\n\n"
    body = re.sub(r"```\n(.*?)\n```", keep, body, flags=re.S)
    out, how = [], ""
    numero = [0]
    # [gus] / [claude] numa linha própria: quem narra daqui até a próxima troca.
    body = re.sub(r"^\[(gus|claude)\][ \t]*\n?", r"\n\n@@VOZ:\1@@\n\n", body, flags=re.M)
    voz = None
    # A linha da voz (div.vl) se interrompe nas figuras e volta depois delas.
    def fecha_voz():
        if out and out[-1].startswith("<figure"):
            out.append("</div>")
        else:
            out.append("</div></div>")
    def figura(h):
        if voz and not out[-1].startswith("<figure"):
            out.append("</div>")
        out.append(h)
    def poe(h):
        if voz and out and out[-1].startswith("<figure"):
            out.append('<div class="vl">')
        out.append(h)
    for b in [x.strip() for x in body.strip().split("\n\n") if x.strip()]:
        if b == "---":
            continue
        # Seção nova e rodapé "How this is made" encerram a voz aberta.
        if voz and (b.startswith("## ") or b.startswith("*How this is made")):
            fecha_voz()
            voz = None
        m = re.match(r"@@VOZ:(gus|claude)@@$", b)
        if m:
            if voz:
                fecha_voz()
            voz = m.group(1)
            nome = "GUS" if voz == "gus" else "CLAUDE"
            out.append(f'<div class="voz voz-{voz}"><p class="quem mono">{nome}</p><div class="vl">')
            continue
        m = re.match(r"@@CODE(\d+)@@$", b)
        if m:
            poe(f'<pre class="term"><code>{html.escape(codes[int(m.group(1))])}</code></pre>')
            continue
        m = re.match(r"((?:!\[\]\(\.\./imagens/[^)]+\)\n)+)\*(.*)\*$", b)
        if m:
            alt = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", m.group(2))
            itens = []
            for f in re.findall(r"\(\.\./imagens/([^)]+)\)", m.group(1)):
                nome = img_name(f)
                if nome.endswith(".mp4"):  # vídeo: medida pelo ffprobe, 16:9 se não houver
                    try:
                        import subprocess as _sp
                        _o = _sp.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                      "stream=width,height", "-of", "csv=p=0",
                                      os.path.join(ROOT, "public", "img", nome)],
                                     capture_output=True, text=True, check=True).stdout.strip()
                        _w, _h = (int(x) for x in _o.split(","))
                    except Exception:
                        _w, _h = 16, 9
                    itens.append((nome, _w, _h))
                    continue
                try:
                    from PIL import Image as _I
                    with _I.open(os.path.join(ROOT, "public", "img", nome)) as _im:
                        _w, _h = _im.size
                except Exception:
                    _w, _h = 4, 3
                itens.append((nome, _w, _h))
            medida = [""]  # altura da figura para a grade: --r (altura/largura), --rm (celular), --k (moldura)
            def tela(nome, _w, _h, est=""):
                if nome in DIAGRAMAS:  # diagrama: painel chapado, sem tubo de CRT
                    cel = nome.replace(".png", "-m.png")
                    tem_cel = os.path.exists(os.path.join(ROOT, "public", "img", cel))
                    fonte_cel = rm = ""
                    if tem_cel:
                        with _I.open(os.path.join(ROOT, "public", "img", cel)) as _im:
                            _cw, _ch = _im.size
                        rm = f";--rm:{_ch / _cw:.6f}"
                        fonte_cel = (f'<source media="(max-width: 700px)" srcset="../img/{cel}"'
                                     f' width="{_cw}" height="{_ch}">')
                    medida[0] = f"--r:{_h / _w:.6f}{rm};--k:0px"
                    return (f'<span class="painel"{est}><picture>{fonte_cel}<img src="../img/{nome}" width="{_w}"'
                            f' height="{_h}" alt="{html.escape(alt)}" loading="lazy"></picture></span>')
                if nome.endswith(".mp4"):  # vídeo no tubo, com controles; capa em NOME-capa.jpg se houver
                    medida[0] = f"--r:{_h / _w:.6f};--k:8px"
                    capa = nome[:-4] + "-capa.jpg"
                    pst = (f' poster="../img/{capa}"'
                           if os.path.exists(os.path.join(ROOT, "public", "img", capa)) else "")
                    return (f'<span class="crt video"{est}><span class="tubo"><video src="../img/{nome}"{pst}'
                            f' width="{_w}" height="{_h}" controls playsinline preload="metadata"'
                            f' aria-label="{html.escape(alt)}"></video></span></span>')
                # pixel art amplia sem suavizar; foto (jpg ou "-foto.png") amplia suave
                foto = nome.endswith((".jpg", ".jpeg", "-foto.png"))
                medida[0] = f"--r:{_h / _w:.6f};--k:8px"
                cls = ' class="px"' if _w < 900 and not foto else ""
                return (f'<span class="crt"{est}><span class="tubo"><img src="../img/{nome}"{cls}'
                        f' width="{_w}" height="{_h}" alt="{html.escape(alt)}" loading="lazy"></span></span>')
            numero[0] += 1
            cap = (f'<figcaption class="cap"><span class="num">{numero[0]}</span>'
                   f'<p>{inline(m.group(2))}</p></figcaption>')
            if len(itens) == 1:
                t1 = tela(*itens[0])
                figura(f'<figure style="{medida[0]}">{t1}{cap}</figure>')
                continue
            # várias telas lado a lado, levemente sobrepostas; a de cima muda ao passar o mouse.
            # No celular, de 3 telas para cima, viram um zigue-zague em duas colunas.
            n = len(itens); sob = 9.0
            w = (100 + (n - 1) * sob) / n
            hs = [w * h / wd for _, wd, h in itens]
            tot = max(hs)
            zw, zcol = 54.0, 46.0
            zh = [zw * h / wd for _, wd, h in itens]
            zt = [0.0]
            for k in range(1, n):
                zt.append(zt[-1] + zh[k - 1] * 0.55)
            ztot = max(t + h for t, h in zip(zt, zh))
            telas = []
            for k, (nome, wd, h) in enumerate(itens):
                est = (f' style="--l:{k * (w - sob):.3f}%;--t:0%;--w:{w:.3f}%;'
                       f'--zl:{(k % 2) * zcol:.3f}%;--zt:{zt[k] / ztot * 100:.3f}%;--zw:{zw:.3f}%;z-index:{n - k}"')
                telas.append(tela(nome, wd, h, est))
            zz = " zz" if n >= 3 else ""
            figura(f'<figure class="grupo" style="--r:{tot / 100:.6f};--rm:{(ztot if zz else tot) / 100:.6f};--k:0px"><div class="degrau{zz}" style="--ar:100/{tot:.3f};--zar:100/{ztot:.3f}">'
                       + "".join(telas) + f"</div>{cap}</figure>")
            continue
        if b.startswith("## "):
            out.append(f'<div class="secr"><h2 class="sec">{inline(b[3:])}</h2><i></i></div>')
            continue
        if b.startswith(">"):
            linhas = [ln[1:].strip() for ln in b.split("\n")]
            linhas = [ln for ln in linhas if ln]
            q = [ln for ln in linhas if not ln.startswith("(Translated")]
            tr = [ln for ln in linhas if ln.startswith("(Translated")]
            poe('<div class="quote"><div class="in">' + "".join(f'<p class="q">{inline(ln)}</p>' for ln in q)
                       + "".join(f'<p class="tr">{inline(ln)}</p>' for ln in tr) + "</div></div>")
            continue
        if b.startswith("*How this is made"):
            how = inline(b.strip("*"))
            continue
        poe(f"<p>{inline(b)}</p>")
    if voz:
        fecha_voz()
    return "\n".join(out), how


sys.path.insert(0, os.path.join(ROOT, "src"))
import fontes  # noqa: E402

FONTES_HEAD = fontes.publica()
try:
    DIAGRAMAS = set(open(os.path.join(ROOT, "src", "diagramas.txt")).read().split())
except FileNotFoundError:
    DIAGRAMAS = set()


def sem_dia(t):
    """\"Day 23: Nine chats...\" vira \"Nine chats...\": o dia já está no selo e na linha de cima."""
    return re.sub(r"^Day \d+:\s*", "", t)


def dia(meta):
    m = re.match(r"Day (\d+)", meta.get("kicker", ""))
    return ("Day", m.group(1)) if m else ("Post", meta.get("badge", ""))


def page(title, content, depth, badge=""):
    tpl = open(os.path.join(ROOT, "src", "template.html"), encoding="utf-8").read()
    home = "../" if depth else "./"
    out = (tpl.replace("{{FONTES}}", FONTES_HEAD).replace("{{BADGE}}", badge)
               .replace("{{TITLE}}", html.escape(title))
               .replace("{{HOME}}", home)
               .replace("{{CONTENT}}", content)
               .replace("</body>", (PREVIA if DRAFTS else "") + "</body>"))
    if DRAFTS:
        # Na prévia o navegador guardava páginas antigas: cada build muda o endereço.
        out = re.sub(r'href="([^"#:?]+\.html)"', r'href="\1?v=' + VERSAO + '"', out)
        out = re.sub(r'href="(\.\.?/)"', r'href="\1index.html?v=' + VERSAO + '"', out)
    return out


# Só na prévia (--drafts): o visualizador recarrega a página inicial a cada
# nova versão; volta para o último post aberto, na mesma altura.
PREVIA = """<script>
// botão da régua de conferência da grade (só na prévia)
(function(){var b=document.createElement('button');b.textContent='GRID CHECK';
b.style.cssText='position:fixed;right:8px;top:8px;z-index:61;font:12px/24px monospace;padding:0 8px;background:#000;color:#0f0;border:0;cursor:pointer;opacity:.75';
b.onclick=function(){window.sotnRegua&&window.sotnRegua()};document.body.appendChild(b)})();
(function(){try{
var S=sessionStorage, post=!!document.querySelector('article');
if(post){
  var v=S.getItem('sotnVolta'); S.removeItem('sotnVolta');
  if(v!==null) addEventListener('load',function(){scrollTo(0,+v)});
  var t=0; addEventListener('scroll',function(){clearTimeout(t);t=setTimeout(function(){
    S.setItem('sotnUlt2',JSON.stringify({u:location.pathname.split('/').pop(),y:scrollY}))},200)});
  S.setItem('sotnUlt2',JSON.stringify({u:location.pathname.split('/').pop(),y:v!==null?+v:0}));
  // clique num link do próprio blog: a lista abre e fica (o visualizador não manda o referrer)
  document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href]');
    if(a&&!/^[a-z]+:/i.test(a.getAttribute('href'))){S.removeItem('sotnUlt2');S.setItem('sotnDentro','1')}},true);
}else{
  var r=document.referrer, dentro=false;
  try{dentro=r&&new URL(r).origin===location.origin}catch(e){}
  if(S.getItem('sotnDentro')){dentro=true;S.removeItem('sotnDentro')}
  S.removeItem('sotnUlt');
  var u=S.getItem('sotnUlt2');
  if(dentro) S.removeItem('sotnUlt2');
  else if(u){u=JSON.parse(u);
    // só o nome do post, relativo a esta página: o endereço completo muda a cada versão
    if(/^[a-z0-9-]+\\.html$/.test(u.u)){S.removeItem('sotnUlt2'); S.setItem('sotnVolta',u.y); location.replace('posts/'+u.u+location.search)}}
}
}catch(e){}})();
</script>
"""


posts = []
for f in sorted(glob.glob(os.path.join(ROOT, "posts", "*.md"))):
    meta, body = front(open(f, encoding="utf-8").read())
    if meta.get("status") != "published" and not DRAFTS:
        continue
    posts.append((meta, body))

# cada título e subtítulo vai sair na CD Drive: letra que a fonte não tem cairia em outra fonte
faltas = []
for meta, body in posts:
    for s in [meta["title"]] + re.findall(r"^## (.*)$", body, re.M):
        f = fontes.cobertura("CD Drive", s)
        if f:
            faltas.append(f'{meta["slug"]}: "{s}" -> sem {" ".join(f)}')
if faltas:
    raise SystemExit("A fonte CD Drive não tem estas letras (desenhe-as em src/fonte_drive.py ou troque o texto):\n  "
                     + "\n  ".join(faltas))

os.makedirs(os.path.join(ROOT, "public", "posts"), exist_ok=True)
for old in glob.glob(os.path.join(ROOT, "public", "posts", "*.html")):
    os.remove(old)

for i, (meta, body) in enumerate(posts):
    content, how = render(body)
    nav = []
    if i > 0:
        p = posts[i - 1][0]
        d = " ".join(dia(p))
        nav.append(f'<a class="prev" href="{p["slug"]}.html"><span class="d">&larr; {html.escape(d)}</span>'
                   f'<span class="t">{html.escape(sem_dia(p["title"]))}</span></a>')
    if i + 1 < len(posts):
        n = posts[i + 1][0]
        d = " ".join(dia(n))
        nav.append(f'<a class="next" href="{n["slug"]}.html"><span class="d">{html.escape(d)} &rarr;</span>'
                   f'<span class="t">{html.escape(sem_dia(n["title"]))}</span></a>')
    draft = '<p class="note">Draft: not published yet</p>' if meta.get("status") != "published" else ""
    rot, num = dia(meta)
    badge = f'<div class="badge"><span>{rot.upper()}</span><b>{html.escape(num)}</b></div>'
    how_html = ""
    if how:
        how_html = ('<div class="how"><div class="bar"><b>How</b><span>this is made</span></div>'
                    f'<p>{re.sub(r"^How this is made:\s*", "", how)}</p></div>')
    art = (f'<article class="w720">\n<div class="kicker">{html.escape(meta["kicker"])}</div>\n'
           f'<h1 class="ttl">{html.escape(sem_dia(meta["title"]))}</h1>\n{draft}\n'
           f'{content}\n{how_html}\n'
           f'<nav class="posts-nav">{"".join(nav)}</nav>\n</article>')
    open(os.path.join(ROOT, "public", "posts", meta["slug"] + ".html"), "w", encoding="utf-8").write(
        page(f'{meta["title"]} | {SITE}', art, 1, badge))

cards = []
for meta, _ in reversed(posts):
    rot, num = dia(meta)
    data = meta["kicker"].split("·", 1)[1].strip() if "·" in meta["kicker"] else meta["kicker"]
    cards.append(f'<a class="card" href="posts/{meta["slug"]}.html">'
                 + (f'<span class="bar"><b>{rot.upper()} {html.escape(num)}</b><span>{html.escape(data)}</span></span>'
                    if rot == "Day" else f'<span class="bar"><b>{html.escape(meta["kicker"].upper())}</b></span>')
                 + f'<span class="t">{html.escape(sem_dia(meta["title"]))}</span>'
                 f'<span class="ex">{html.escape(meta.get("excerpt", ""))}</span></a>')
idx = '<section class="list w720">\n' + "\n".join(cards) + "\n</section>"
open(os.path.join(ROOT, "public", "index.html"), "w", encoding="utf-8").write(page(SITE, idx, 0))
print("ok:", ", ".join(m["slug"] + ("" if m.get("status") == "published" else " (rascunho)") for m, _ in posts))

# A grade é contrato: todo bloco no quadriculado de 24 px, em várias larguras de janela.
if "--sem-grade" not in sys.argv:
    try:
        import playwright  # noqa: F401
    except ImportError:
        print("AVISO: grade não conferida (playwright não instalado)")
    else:
        sys.path.insert(0, os.path.join(ROOT, "src"))
        import grade_test
        if grade_test.main():
            raise SystemExit("build falhou: conteúdo fora da grade")
