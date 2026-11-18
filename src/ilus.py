#!/usr/bin/env python3
"""Peças comuns das ilustrações do blog: tela com o quadriculado da caixa do
Mega Drive, caixas, setas, rótulos e gráficos simples. Tudo desenhado do zero,
sem arte do jogo."""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "public", "img")
# visual do blog (KV da caixa do Mega-CD, 18/11): cada diagrama é um painel chapado de fundo
# pastel, com barra de título azul-marinho (CD Drive + mono) e, quando diz o que a figura é,
# uma faixa vermelha embaixo. A sombra em xadrez fica por conta da página.
RED, GREEN, YELLOW, BLUE = (210, 35, 42), (0, 150, 75), (243, 210, 60), (27, 86, 176)
INK, PAPER, GRAY, LIGHT = (24, 24, 26), (255, 255, 255), (110, 110, 112), (236, 236, 236)
NAVY, FAIXA, SUB = (30, 44, 102), (174, 41, 0), (230, 233, 245)
FUNDOS = {"barras": (255, 242, 184), "linha": (217, 238, 213), "geral": (214, 231, 246), "rosa": (248, 220, 228)}
FT = os.path.join(ROOT, "fontes")
DIAGRAMAS = os.path.join(ROOT, "src", "diagramas.txt")


def fonte(px, bold=True, mono=False, ital=False):
    if ital:
        return ImageFont.truetype(os.path.join(FT, "cd-drive.ttf"), px)
    if mono or bold:
        return ImageFont.truetype(os.path.join(FT, "monommm5.ttf"), px)
    return ImageFont.truetype(os.path.join(FT, "archivo-regular.ttf"), px)


def xadrez(d, x0, y0, x1, y1, cor=INK, p=2):
    """Sombra em xadrez, a transparência do Mega Drive."""
    for y in range(int(y0), int(y1), p):
        for x in range(int(x0) + ((int(y - y0) // p) % 2) * p, int(x1), 2 * p):
            d.rectangle((x, y, x + p - 1, y + p - 1), fill=cor)


def divide_titulo(t):
    """Título principal com no máximo 2 palavras; o resto vira subtítulo na mono."""
    if "," in t and len(t.split(",")[0].split()) <= 2:
        a, b = t.split(",", 1)
        return a.strip(), b.strip()
    w = t.split()
    return " ".join(w[:2]), " ".join(w[2:])


def faixa_texto(im, x, y, h, principal, sub, s, cor_sub=SUB):
    """Escreve título (CD Drive a 87% de altura, enchendo a faixa) + subtítulo (mono) numa faixa de altura h."""
    d = ImageDraw.Draw(im)
    if principal:
        f = fonte(round(29 * s), ital=True)
        tw = int(d.textlength(principal.upper(), font=f)) + 4
        tmp = Image.new("RGBA", (tw, round(29 * s * 1.3)), (0, 0, 0, 0))
        ImageDraw.Draw(tmp).text((0, round(29 * s * 1.05)), principal.upper(), font=f, fill=PAPER, anchor="ls")
        bb = tmp.getbbox() or (0, 0, 1, 1)
        tmp = tmp.crop((0, bb[1], tw, bb[3]))
        tmp = tmp.resize((tw, max(1, round(tmp.height * 0.87))), Image.LANCZOS)
        im.paste(tmp, (x, y + (h - tmp.height) // 2), tmp)
        x += int(d.textlength(principal.upper() + " ", font=f))
    if sub:
        fm = fonte(round(17 * s), mono=True)
        if x + d.textlength(sub.upper(), font=fm) <= im.width - round(11 * s):  # não cabe: fica só o título
            d.text((x, y + h / 2), sub.upper(), font=fm, fill=cor_sub, anchor="lm")


class Tela:
    def __init__(self, w, h, titulo=None, selo=None, tipo=None, escala=960):
        # escala: largura em que a imagem aparece na página (960 no computador, 336 no celular),
        # para a barra de título sair com 24 px de altura na tela
        self.w, self.h = w, h
        self.s = w / escala
        self.selo = selo
        tipo = tipo or "geral"
        self.fundo = FUNDOS[tipo]
        self.im = Image.new("RGB", (w, h), self.fundo)
        self.d = ImageDraw.Draw(self.im)
        self.top = 0
        if titulo:
            B = round(24 * self.s)
            self.d.rectangle((0, 0, w, B), fill=NAVY)
            faixa_texto(self.im, round(11 * self.s), 0, B, *divide_titulo(titulo), self.s)
            self.top = B + round(12 * self.s)

    def caixa(self, x0, y0, x1, y1, cab=None, cor=BLUE, linhas=(), tam=18, fundo=PAPER):
        d = self.d
        xadrez(d, x0 + 6, y0 + 6, x1 + 7, y1 + 7)
        d.rectangle((x0, y0, x1, y1), fill=fundo, outline=INK, width=3)
        y = y0 + 10
        if cab:
            d.rectangle((x0, y0, x1, y0 + 40), fill=cor, outline=INK, width=3)
            d.text(((x0 + x1) // 2, y0 + 21), cab, font=fonte(19), fill=PAPER, anchor="mm")
            y = y0 + 52
        f = fonte(tam, bold=False)
        for ln in linhas:
            d.text(((x0 + x1) // 2, y), ln, font=f, fill=INK, anchor="mt")
            y += int(tam * 1.4)

    def seta(self, x0, y0, x1, y1, cor=INK, larg=4, rotulo=None, tam=16, cab=14):
        import math
        d = self.d
        d.line((x0, y0, x1, y1), fill=cor, width=larg)
        a = math.atan2(y1 - y0, x1 - x0)
        p1 = (x1 - cab * math.cos(a - 0.45), y1 - cab * math.sin(a - 0.45))
        p2 = (x1 - cab * math.cos(a + 0.45), y1 - cab * math.sin(a + 0.45))
        d.polygon([(x1, y1), p1, p2], fill=cor)
        if rotulo:
            mx, my = (x0 + x1) / 2, (y0 + y1) / 2
            f = fonte(tam, bold=False)
            for i, ln in enumerate(rotulo.split("\n")):
                tw = d.textlength(ln, font=f)
                yy = my - 22 - (len(rotulo.split("\n")) - 1 - i) * (tam + 4)
                d.rectangle((mx - tw / 2 - 4, yy - tam / 2 - 3, mx + tw / 2 + 4, yy + tam / 2 + 3), fill=PAPER)
                d.text((mx, yy), ln, font=f, fill=cor, anchor="mm")

    def texto(self, x, y, s, tam=18, cor=INK, bold=False, anchor="la", mono=False):
        f = fonte(tam, bold=bold, mono=mono)
        for i, ln in enumerate(s.split("\n")):
            self.d.text((x, y + i * int(tam * 1.35)), ln, font=f, fill=cor, anchor=anchor)

    def salva(self, nome):
        salva_com_margem(self.im, nome, self.selo, self.fundo, self.s)
        

def barras(nome, titulo, rotulos, valores, cores, unidade="", linha=None, linha_rot=None,
           w=1200, h=560, maxv=None, selo=None, notas=None):
    """Barras horizontais com valor no fim; linha tracejada opcional."""
    t = Tela(w, h, titulo, selo, "barras")
    d = t.d
    x0, x1 = 300, w - 120
    n = len(valores)
    topo = t.top + 70
    alt = (h - topo - 60) / n
    maxv = maxv or max(valores + ([linha] if linha else [])) * 1.08
    for i, (r, v, c) in enumerate(zip(rotulos, valores, cores)):
        y = topo + i * alt
        bh = alt * 0.62
        d.text((x0 - 16, y + bh / 2), r, font=fonte(18), fill=INK, anchor="rm")
        xe = x0 + (x1 - x0) * v / maxv
        d.rectangle((x0, y, xe, y + bh), fill=c, outline=INK, width=2)
        d.text((xe + 10, y + bh / 2), f"{v:g}{unidade}", font=fonte(18), fill=INK, anchor="lm")
        if notas and notas[i]:
            d.text((x0 + 8, y + bh + 4), notas[i], font=fonte(14, bold=False), fill=GRAY)
    if linha:
        xl = x0 + (x1 - x0) * linha / maxv
        for yy in range(int(topo - 20), int(h - 40), 14):
            d.line((xl, yy, xl, yy + 7), fill=RED, width=3)
        if linha_rot:
            d.text((xl, topo - 34), linha_rot, font=fonte(16), fill=RED, anchor="mm")
    t.salva(nome)
    # versão do celular: 672 px de largura para aparecer em 336, rótulo em cima de cada barra
    W, n = 672, len(valores)
    tm = Tela(W, 0 + 48 + 24 + n * 120 + 24, titulo, None, "barras", escala=336)
    tm.im = tm.im.resize((W, tm.h)); tm.d = ImageDraw.Draw(tm.im)
    tm.d.rectangle((0, 0, W, round(24 * tm.s)), fill=NAVY)
    faixa_texto(tm.im, round(11 * tm.s), 0, round(24 * tm.s), *divide_titulo(titulo), tm.s)
    x0, x1 = 24, W - 120
    for i, (r, v, c) in enumerate(zip(rotulos, valores, cores)):
        y = 48 + 24 + i * 120
        tm.d.text((x0, y + 20), r, font=fonte(30), fill=INK, anchor="lm")
        xe = x0 + (x1 - x0) * v / maxv
        tm.d.rectangle((x0, y + 48, xe, y + 96), fill=c, outline=INK, width=2)
        tm.d.text((xe + 14, y + 72), f"{v:g}{unidade}", font=fonte(32), fill=INK, anchor="lm")
    if linha:
        xl = x0 + (x1 - x0) * linha / maxv
        for yy in range(72, tm.h - 12, 20):
            tm.d.line((xl, yy, xl, yy + 10), fill=RED, width=4)
    salva_com_margem(tm.im, nome.replace(".png", "-m.png"), selo, tm.fundo, tm.s)


def hm(s):
    h, m = s.split(":")
    return int(h) + int(m) / 60


def linha_do_tempo(nome, titulo, commits, falas, notas=(), sombras=()):
    """notas: (hora, texto, lado) com lado 'l' ou 'r'; sombras: (h0, h1, texto)."""
    t = Tela(1200, 540, titulo, None, "linha")
    d = t.d
    x0, x1 = 70, 1150
    X = lambda h: x0 + (x1 - x0) * h / 24
    yc, yf = 250, 380
    for h0, h1, s in sombras:
        d.rectangle((X(h0), 110, X(h1), 440), fill=(222, 230, 244))
        t.texto((X(h0) + X(h1)) / 2, 118, s, 15, BLUE, True, "mt")
    d.line((x0, yc, x1, yc), fill=INK, width=2)
    d.line((x0, yf, x1, yf), fill=INK, width=2)
    t.texto(x0, yc - 50, f"Claude's commits ({len(commits)})", 18, RED, True)
    t.texto(x0, yf - 50, f"my messages ({len(falas)})", 18, BLUE, True)
    for c in commits:
        x = X(hm(c))
        d.rectangle((x - 3, yc - 22, x + 3, yc + 22), fill=RED)
    for f in falas:
        x = X(hm(f))
        d.ellipse((x - 7, yf - 7, x + 7, yf + 7), fill=BLUE, outline=INK)
    for h in range(0, 25, 3):
        x = X(h)
        d.line((x, 450, x, 460), fill=INK, width=2)
        t.texto(x, 466, f"{h:02d}:00", 15, INK, False, "mt")
    for i, (h, s, lado) in enumerate(notas):
        x = X(hm(h))
        y = 300 + (i % 2) * 34
        t.seta(x + (-30 if lado == "r" else 30), y + 6, x, yf - 12, BLUE, 3, cab=10)
        t.texto(x + (-34 if lado == "r" else 34), y - 10, s, 14, BLUE, True, "rs" if lado == "r" else "ls")
    t.salva(nome)
    # versão do celular: 672 px para aparecer em 336, letras de 13 px na tela, sem as notas
    # (a legenda conta o que elas diziam)
    W, H = 672, 48 + 360
    tm = Tela(W, H, titulo, None, "linha", escala=336)
    d = tm.d
    x0, x1 = 24, W - 24
    X = lambda h: x0 + (x1 - x0) * h / 24
    yc, yf = 48 + 104, 48 + 232
    for h0, h1, s in sombras:
        d.rectangle((X(h0), 48 + 24, X(h1), 48 + 300), fill=(222, 230, 244))
        d.text(((X(h0) + X(h1)) / 2, 48 + 40), s.upper()[:14], font=fonte(22), fill=BLUE, anchor="mm")
    d.text((x0, yc - 44), f"CLAUDE'S COMMITS ({len(commits)})", font=fonte(26), fill=RED, anchor="ls")
    d.text((x0, yf - 44), f"MY MESSAGES ({len(falas)})", font=fonte(26), fill=BLUE, anchor="ls")
    d.line((x0, yc, x1, yc), fill=INK, width=3)
    d.line((x0, yf, x1, yf), fill=INK, width=3)
    for c in commits:
        x = X(hm(c))
        d.rectangle((x - 2, yc - 20, x + 2, yc + 20), fill=RED)
    for f in falas:
        x = X(hm(f))
        d.ellipse((x - 8, yf - 8, x + 8, yf + 8), fill=BLUE, outline=INK)
    for h in range(0, 25, 6):
        x = X(h)
        d.line((x, 48 + 300, x, 48 + 314), fill=INK, width=3)
        d.text((x, 48 + 336), f"{h:02d}", font=fonte(26), fill=INK,
               anchor="lm" if h == 0 else ("rm" if h == 24 else "mm"))
    salva_com_margem(tm.im, nome.replace(".png", "-m.png"), None, tm.fundo, tm.s)


def salva_com_margem(im, nome, selo=None, fundo=None, s=None):
    s = s or im.width / 960
    if selo:
        B, m = round(24 * s), round(24 * s)
        out = Image.new("RGB", (im.width, im.height + m + B + m), fundo or FUNDOS["geral"])
        out.paste(im, (0, 0))
        d = ImageDraw.Draw(out)
        d.rectangle((m, im.height + m, im.width - m, im.height + m + B), fill=FAIXA)
        faixa_texto(out, m + round(11 * s), im.height + m, B, "", selo, s, cor_sub=PAPER)
        im = out
    global SALVANDO
    SALVANDO = True
    try:
        im.save(os.path.join(OUT, nome), optimize=True)
    finally:
        SALVANDO = False
    try:
        feitos = set(open(DIAGRAMAS).read().split())
    except FileNotFoundError:
        feitos = set()
    if nome not in feitos and not nome.endswith("-m.png"):
        open(DIAGRAMAS, "a").write(nome + "\n")
    print("ok", nome)


SALVANDO = False
