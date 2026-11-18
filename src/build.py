#!/usr/bin/env python3
"""Gera index.html do blog a partir do post em Markdown simples."""
import html, os, re, sys

SRC = sys.argv[1]
raw = open(SRC, encoding="utf-8").read()
fm, body = raw.split("---", 2)[1], raw.split("---", 2)[2]
title = re.search(r'title:\s*"(.*)"', fm).group(1)

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\[\[(.*?)\]\]", r'<span class="note">\1</span>', t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"(?<![\w/])\*(.+?)\*(?![\w])", r"<em>\1</em>", t)
    return t

blocks = [b.strip() for b in body.strip().split("\n\n") if b.strip()]
out, footer = [], ""
for i, b in enumerate(blocks):
    if b == "---":
        continue
    m = re.match(r"!\[\]\(\.\./imagens/([^)]+)\)\n\*(.*)\*$", b)
    if m:
        f = re.sub(r"\.(png|jpg)$", "", m.group(1))
        f = f + (".png" if f.startswith("06") else ".jpg")
        out.append(f'<figure><img src="img/{f}" alt="{html.escape(re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", m.group(2)))}" loading="lazy">'
                   f'<figcaption>{inline(m.group(2))}</figcaption></figure>')
        continue
    if b.startswith("*How this is made"):
        footer = inline(b.strip("*"))
        continue
    out.append(f"<p>{inline(b)}</p>")

tpl = open(os.path.join(os.path.dirname(__file__), "template.html"), encoding="utf-8").read()
page = (tpl.replace("{{TITLE}}", html.escape(title))
           .replace("{{BODY}}", "\n".join(out))
           .replace("{{FOOTER}}", footer))
open(os.path.join(os.path.dirname(__file__), "..", "public", "index.html"), "w", encoding="utf-8").write(page)
print("ok", len(out), "blocos")
