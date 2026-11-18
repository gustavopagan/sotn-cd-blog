#!/usr/bin/env python3
"""Gera o site em public/ a partir de posts/*.md.

Uso: python3 src/build.py [--drafts]
  --drafts inclui os posts com status: draft (só para prévia, nunca para o push).

Saída: public/index.html (lista de posts) e public/posts/<slug>.html.
"""
import glob, html, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DRAFTS = "--drafts" in sys.argv
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
    for b in [x.strip() for x in body.strip().split("\n\n") if x.strip()]:
        if b == "---":
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
                cls = ' class="px"' if _w < 900 else ""
                return (f'<span class="crt"{est}><span class="tubo"><img src="../img/{nome}"{cls}'
                        f' width="{_w}" height="{_h}" alt="{html.escape(alt)}" loading="lazy"></span></span>')
            cap = f"<figcaption>{inline(m.group(2))}</figcaption>"
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
            out.append(f"<h2>{inline(b[3:])}</h2>")
            continue
        if b.startswith("*How this is made"):
            how = inline(b.strip("*"))
            continue
        out.append(f"<p>{inline(b)}</p>")
    return "\n".join(out), how


sys.path.insert(0, os.path.join(ROOT, "src"))
import fontes  # noqa: E402

FONTES_HEAD = fontes.publica()


def page(title, content, depth):
    tpl = open(os.path.join(ROOT, "src", "template.html"), encoding="utf-8").read()
    home = "../" if depth else "./"
    return (tpl.replace("{{FONTES}}", FONTES_HEAD)
               .replace("{{TITLE}}", html.escape(title))
               .replace("{{HOME}}", home)
               .replace("{{CONTENT}}", content))


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
        nav.append(f'<a class="prev" href="{p["slug"]}.html">&larr; {html.escape(p["title"])}</a>')
    if i + 1 < len(posts):
        n = posts[i + 1][0]
        nav.append(f'<a class="next" href="{n["slug"]}.html">{html.escape(n["title"])} &rarr;</a>')
    draft = '<p class="note">Draft: not published yet.</p>' if meta.get("status") != "published" else ""
    art = (f'<article>\n<div class="badge"><span>Post<b>{html.escape(meta["badge"])}</b></span></div>\n'
           f'<p class="kicker">{html.escape(meta["kicker"])}</p>\n<h1>{html.escape(meta["title"])}</h1>\n{draft}\n'
           f'{content}\n<div class="how">{how}</div>\n</article>\n'
           f'<nav class="posts-nav">{"".join(nav)}</nav>')
    open(os.path.join(ROOT, "public", "posts", meta["slug"] + ".html"), "w", encoding="utf-8").write(
        page(f'{meta["title"]} | {SITE}', art, 1))

cards = []
for meta, _ in reversed(posts):
    cards.append(f'<a class="card" href="posts/{meta["slug"]}.html">'
                 f'<span class="num">{html.escape(meta["badge"])}</span>'
                 f'<span class="txt"><span class="kicker">{html.escape(meta["kicker"])}</span>'
                 f'<span class="t">{html.escape(meta["title"])}</span>'
                 f'<span class="ex">{html.escape(meta.get("excerpt", ""))}</span></span></a>')
idx = '<section class="list">\n' + "\n".join(cards) + "\n</section>"
open(os.path.join(ROOT, "public", "index.html"), "w", encoding="utf-8").write(page(SITE, idx, 0))
print("ok:", ", ".join(m["slug"] + ("" if m.get("status") == "published" else " (rascunho)") for m, _ in posts))
