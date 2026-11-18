#!/usr/bin/env python3
"""Peças comuns das ilustrações do blog: tela com o quadriculado da caixa do
Mega Drive, caixas, setas, rótulos e gráficos simples. Tudo desenhado do zero,
sem arte do jogo."""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "public", "img")
RED, GREEN, YELLOW, BLUE = (200, 38, 44), (21, 146, 74), (244, 196, 0), (4, 100, 182)
INK, PAPER, GRAY, LIGHT = (17, 17, 17), (255, 255, 255), (130, 130, 130), (236, 236, 236)
DJ = "/usr/share/fonts/truetype/dejavu/"


def fonte(px, bold=True, mono=False):
    nome = "DejaVuSansMono-Bold.ttf" if mono else ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")
    return ImageFont.truetype(DJ + nome, px)


class Tela:
    def __init__(self, w, h, titulo=None, selo=None):
        self.w, self.h = w, h
        self.im = Image.new("RGB", (w, h), PAPER)
        self.d = ImageDraw.Draw(self.im)
        for x in range(0, w, 24):
            self.d.line((x, 0, x, h), fill=(242, 242, 242))
        for y in range(0, h, 24):
            self.d.line((0, y, w, y), fill=(242, 242, 242))
        self.top = 0
        if titulo:
            self.d.rectangle((0, 0, w, 54), fill=INK)
            self.d.text((24, 27), titulo, font=fonte(26), fill=PAPER, anchor="lm")
            self.top = 54
        if selo:
            f = fonte(14)
            tw = self.d.textlength(selo, font=f)
            self.d.rectangle((w - tw - 36, self.top + 12, w - 12, self.top + 38), fill=YELLOW)
            self.d.text((w - tw - 24, self.top + 25), selo, font=f, fill=INK, anchor="lm")

    def caixa(self, x0, y0, x1, y1, cab=None, cor=BLUE, linhas=(), tam=18, fundo=PAPER):
        d = self.d
        d.rectangle((x0 + 5, y0 + 5, x1 + 5, y1 + 5), fill=(200, 200, 200))
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
        self.im.save(os.path.join(OUT, nome), optimize=True)
        print("ok", nome)


def barras(nome, titulo, rotulos, valores, cores, unidade="", linha=None, linha_rot=None,
           w=1200, h=560, maxv=None, selo=None, notas=None):
    """Barras horizontais com valor no fim; linha tracejada opcional."""
    t = Tela(w, h, titulo, selo)
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


def hm(s):
    h, m = s.split(":")
    return int(h) + int(m) / 60


def linha_do_tempo(nome, titulo, commits, falas, notas=(), sombras=()):
    """notas: (hora, texto, lado) com lado 'l' ou 'r'; sombras: (h0, h1, texto)."""
    t = Tela(1200, 540, titulo)
    d = t.d
    x0, x1 = 70, 1150
    X = lambda h: x0 + (x1 - x0) * h / 24
    yc, yf = 250, 380
    for h0, h1, s in sombras:
        d.rectangle((X(h0), 110, X(h1), 440), fill=(225, 232, 245))
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
