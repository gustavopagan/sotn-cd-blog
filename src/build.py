#!/usr/bin/env python3
"""Gera o site em public/ a partir de posts/*.md.

Uso: python3 src/build.py [--drafts]
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
    t = re.sub(r"(?<![\w/])\*(.+?)\*(?![\w])", r"<em>\1</em>", t)
    return t


def img_name(f):
    base = re.sub(r"\.(png|jpg|gif)$", "", f)
    for ext in (".jpg", ".png", ".gif"):
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
    for b in [x.strip() for x in body.strip().split("\n\n") if x.strip()]:
        if b == "---":
            continue
        # Seção nova e rodapé "How this is made" encerram a voz aberta.
        if voz and (b.startswith("## ") or b.startswith("*How this is made")):
            out.append("</div>")
            voz = None
        m = re.match(r"@@VOZ:(gus|claude)@@$", b)
        if m:
            if voz:
                out.append("</div>")
            voz = m.group(1)
            nome = "GUS" if voz == "gus" else "CLAUDE"
            out.append(f'<div class="voz voz-{voz}"><p class="quem mono">{nome}</p>')
            continue
        m = re.match(r"@@CODE(\d+)@@$", b)
        if m:
            out.append(f'<pre class="term"><code>{html.escape(codes[int(m.group(1))])}</code></pre>')
            continue
        m = re.match(r"((?:!\[\]\(\.\./imagens/[^)]+\)\n)+)\*(.*)\*$", b)
        if m:
            alt = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", m.group(2))
            itens = []
            for f in re.findall(r"\(\.\./imagens/([^)]+)\)", m.group(1)):
                nome = img_name(f)
                try:
                    from PIL import Image as _I
                    with _I.open(os.path.join(ROOT, "public", "img", nome)) as _im:
                        _w, _h = _im.size
                except Exception:
                    _w, _h = 4, 3
                itens.append((nome, _w, _h))
            def tela(nome, _w, _h, est=""):
                if nome in DIAGRAMAS:  # diagrama: painel chapado, sem tubo de CRT
                    cel = nome.replace(".png", "-m.png")
                    fonte_cel = (f'<source media="(max-width: 700px)" srcset="../img/{cel}">'
                                 if os.path.exists(os.path.join(ROOT, "public", "img", cel)) else "")
                    return (f'<span class="painel"{est}><picture>{fonte_cel}<img src="../img/{nome}" width="{_w}"'
                            f' height="{_h}" alt="{html.escape(alt)}" loading="lazy"></picture></span>')
                cls = ' class="px"' if _w < 900 else ""
                return (f'<span class="crt"{est}><span class="tubo"><img src="../img/{nome}"{cls}'
                        f' width="{_w}" height="{_h}" alt="{html.escape(alt)}" loading="lazy"></span></span>')
            numero[0] += 1
            cap = (f'<figcaption class="cap"><span class="num">{numero[0]}</span>'
                   f'<p>{inline(m.group(2))}</p></figcaption>')
            if len(itens) == 1:
                out.append(f"<figure>{tela(*itens[0])}{cap}</figure>")
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
            out.append(f'<figure class="grupo"><div class="degrau{zz}" style="--ar:100/{tot:.3f};--zar:100/{ztot:.3f}">'
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
            out.append('<div class="quote"><div class="in">' + "".join(f'<p class="q">{inline(ln)}</p>' for ln in q)
                       + "".join(f'<p class="tr">{inline(ln)}</p>' for ln in tr) + "</div></div>")
            continue
        if b.startswith("*How this is made"):
            how = inline(b.strip("*"))
            continue
        out.append(f"<p>{inline(b)}</p>")
    if voz:
        out.append("</div>")
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
(function(){try{
var S=sessionStorage, post=!!document.querySelector('article');
if(post){
  var v=S.getItem('sotnVolta'); S.removeItem('sotnVolta');
  if(v!==null) addEventListener('load',function(){scrollTo(0,+v)});
  var t=0; addEventListener('scroll',function(){clearTimeout(t);t=setTimeout(function(){
    S.setItem('sotnUlt',JSON.stringify({u:location.href,y:scrollY}))},200)});
  S.setItem('sotnUlt',JSON.stringify({u:location.href,y:v!==null?+v:0}));
}else{
  var r=document.referrer, dentro=false;
  try{dentro=r&&new URL(r).origin===location.origin}catch(e){}
  var u=S.getItem('sotnUlt');
  if(dentro) S.removeItem('sotnUlt');
  else if(u){u=JSON.parse(u); S.setItem('sotnVolta',u.y); location.replace(u.u)}
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
                 f'<span class="bar"><b>{rot.upper()} {html.escape(num)}</b><span>{html.escape(data)}</span></span>'
                 f'<span class="t">{html.escape(sem_dia(meta["title"]))}</span>'
                 f'<span class="ex">{html.escape(meta.get("excerpt", ""))}</span></a>')
idx = '<section class="list w720">\n' + "\n".join(cards) + "\n</section>"
open(os.path.join(ROOT, "public", "index.html"), "w", encoding="utf-8").write(page(SITE, idx, 0))
print("ok:", ", ".join(m["slug"] + ("" if m.get("status") == "published" else " (rascunho)") for m, _ in posts))
