#!/usr/bin/env python3
"""Ilustrações do post 4 (dia 3, 20/10)."""
import random
from ilus import *


def tempo():
    commits = ("09:52 10:41 11:21 11:42 11:51 13:04 13:40 14:53 15:40 15:56 16:03 16:38 16:54 16:54 "
               "17:28 17:57 18:17 18:50 22:42 23:19 23:40").split()
    falas = ("09:30 10:03 10:06 10:14 10:21 10:28 11:20 11:22 11:54 13:20 13:22 13:24 14:22 15:17 15:23 "
             "15:25 15:45 16:13 16:23 16:27 16:30 18:05 18:09 18:30 22:32 23:11 23:30 23:54 23:56").split()
    linha_do_tempo("38-dia3-linha-do-tempo.png", "October 20, hour by hour", commits, falas,
                   notas=[("10:21", "10:21 a.m.: rewrite the merman", "l"),
                          ("16:23", "4:23 p.m.: what about FM music?", "l"),
                          ("23:56", "11:56 p.m.: \"are you sure?\"", "r")],
                   sombras=[(19.0, 22.4, "nobody working")])


def merman():
    t = Tela(1200, 520, "The merman rewrite, measured")
    d = t.d
    def painel(x0, tit, a, b, un, maxv, ra, rb):
        t.texto(x0 + 240, t.top + 40, tit, 20, INK, True, "mt")
        base = 440
        for i, (v, c, r) in enumerate(((a, GRAY, ra), (b, GREEN, rb))):
            x = x0 + 90 + i * 200
            h = 300 * v / maxv
            d.rectangle((x, base - h, x + 120, base), fill=c, outline=INK, width=3)
            t.texto(x + 60, base - h - 34, f"{v:,}{un}".replace(",", ","), 20, INK, True, "mt")
            t.texto(x + 60, base + 12, r, 16, INK, False, "mt")
    painel(40, "One merman, one frame (CPU cycles)", 3200, 3050, "", 3400, "original C", "68000 rewrite")
    painel(640, "The whole sub-CPU frame (busy part of the room)", 88.9, 88.1, "%", 100, "before", "after")
    t.texto(600, 486, "5% faster per merman. Less than 1% on the frame. The cost was somewhere else.",
            17, RED, True, "mt")
    t.salva("32-merman-medido.png")


def lista_vivos():
    t = Tela(1200, 600, "256 entity slots, a dozen in use", "DIAGRAM")
    d = t.d
    random.seed(7)
    vivos = {0, 1, 3, 5, 64, 65, 66, 70, 71, 90, 91, 130}
    def grade(x0, y0, setas):
        s = 22
        for i in range(256):
            x, y = x0 + (i % 16) * s, y0 + (i // 16) * s
            c = RED if i == 0 else (GREEN if i in vivos else LIGHT)
            d.rectangle((x, y, x + s - 3, y + s - 3), fill=c, outline=(190, 190, 190))
        if setas:
            ordem = sorted(vivos)
            for a, b in zip(ordem, ordem[1:]):
                xa, ya = x0 + (a % 16) * s + 9, y0 + (a // 16) * s + 9
                xb, yb = x0 + (b % 16) * s + 9, y0 + (b // 16) * s + 9
                d.line((xa, ya, xb, yb), fill=BLUE, width=2)
    grade(90, 130, False)
    grade(690, 130, True)
    t.texto(266, 500, "Before: every loop walks all 256,\nthree loops per frame", 17, INK, True, "mt")
    t.texto(866, 500, "After: a list of live slots,\njump straight to them", 17, INK, True, "mt")
    t.texto(600, 104, "red = Alucard   green = in use   gray = empty", 15, GRAY, False, "mt")
    t.salva("33-lista-de-vivos.png")


def agua():
    t = Tela(1200, 620, "Water out of a palette swap", "DIAGRAM")
    d = t.d
    x0, y0, w, h = 60, 110, 512, 448
    linha = 300
    cores = [(120, 60, 40), (200, 180, 150), (70, 70, 110), (160, 40, 40), (40, 120, 60), (220, 200, 60)]
    tint = lambda c: tuple(int((v + a) / 2) for v, a in zip(c, (48, 64, 96)))
    for y in range(y0, y0 + h, 16):
        for x in range(x0, x0 + w, 32):
            c = cores[((x // 32) + (y // 16) * 3) % 6]
            if y >= linha + 12:
                c = tint(c)
            d.rectangle((x, y, x + 31, y + 15), fill=c)
    d.rectangle((x0, linha, x0 + w, linha + 12), fill=(150, 190, 230))
    d.rectangle((x0, y0, x0 + w, y0 + h), outline=INK, width=4)
    for x in range(x0 - 20, x0 + w + 20, 16):
        d.line((x, linha, x + 8, linha), fill=RED, width=3)
    t.texto(x0 + w / 2, y0 + h + 14, "the screen, 224 lines", 15, GRAY, False, "mt")
    passos = [("1. Every VBLANK", "normal palette in, and an interrupt\narmed for the line above the water"),
              ("2. The beam reaches that line", "the horizontal interrupt fires"),
              ("3. Display off for a moment", "copy the tinted palette into the VDP;\nthe blank lines show as foam"),
              ("4. Display back on", "everything below is drawn\nwith the tinted colors")]
    y = 130
    for tit, txt in passos:
        t.texto(640, y, tit, 19, BLUE, True)
        t.texto(640, y + 28, txt, 16)
        y += 108
    t.seta(630, 340, x0 + w + 24, linha + 4, RED, 3)
    t.salva("35-agua-hint.png")


def orcamento():
    t = Tela(1200, 600, "Too many sprites on a line", "DIAGRAM")
    d = t.d
    def sprite(x, y, w, h, c, faltam=(), pisca=False):
        if pisca:
            for yy in range(y, y + h, 4):
                d.line((x, yy, x + w, yy), fill=(200, 200, 200))
            d.rectangle((x, y, x + w, y + h), outline=GRAY, width=2)
            return
        d.rectangle((x, y, x + w, y + h), fill=c, outline=INK, width=2)
        for a, b in faltam:
            d.rectangle((x - 1, y + a, x + w + 1, y + b), fill=PAPER)
    for k, x0 in enumerate((60, 640)):
        d.rectangle((x0, 130, x0 + 500, 470), fill=(30, 30, 40))
        d.rectangle((x0, 280, x0 + 500, 320), outline=YELLOW, width=2)
    # antes: cortes em linhas
    sprite(80, 200, 60, 140, RED)
    for i, x in enumerate(range(160, 540, 46)):
        yy = 230 + (i % 3) * 10
        cortes = [(282 - yy, 318 - yy)] if i >= 5 else ()
        sprite(x, yy, 38, 100, GREEN if i < 4 else YELLOW, cortes)
    # depois: objeto inteiro fora, e pisca
    sprite(660, 200, 60, 140, RED)
    for i, x in enumerate(range(740, 1120, 46)):
        sprite(x, 230 + (i % 3) * 10, 38, 100, GREEN if i < 4 else YELLOW, pisca=(i == 6))
    t.texto(310, 490, "Before: the VDP cuts whatever comes last.\nLines go missing from random sprites.", 16, INK, True, "mt")
    t.texto(890, 490, "After: the port counts first. Alucard, then bodies,\nthen effects. What doesn't fit sits out whole,\nand a different one sits out each frame.", 16, INK, True, "mt")
    t.texto(310, 100, "red: Alucard   green: enemies   yellow: effects", 15, GRAY, False, "mt")
    t.texto(890, 100, "yellow band: a line already full", 15, GRAY, False, "mt")
    t.salva("36-orcamento-por-linha.png")


def fm():
    t = Tela(1200, 560, "The FM music path, October 20", "DIAGRAM")
    t.caixa(30, 120, 300, 300, "VGM file", GRAY, ["a Mega Drive arrangement,", "every chip write", "with its timing"])
    t.caixa(345, 120, 615, 300, "build tools", GREEN, ["writes grouped per", "1/60 s, repeats", "dropped, compressed"])
    t.caixa(660, 120, 930, 300, "sub-CPU", BLUE, ["unpacks a bit of the", "song every frame into", "shared memory"])
    t.caixa(975, 120, 1170, 300, "main 68000", RED, ["plays it on the", "YM2612 and PSG"])
    t.caixa(660, 360, 930, 520, "Mega CD PCM chip", BLUE, ["the drums, as", "samples"])
    t.seta(305, 210, 340, 210)
    t.seta(620, 210, 655, 210)
    t.seta(935, 210, 970, 210)
    t.seta(795, 305, 795, 355)
    t.texto(30, 380, "The CD stays free for loading:\nthe song lives in RAM.", 17, INK, True)
    t.salva("37-fm-caminho.png")


if __name__ == "__main__":
    tempo()
    merman()
    lista_vivos()
    agua()
    orcamento()
    fm()
