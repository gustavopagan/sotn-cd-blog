#!/usr/bin/env python3
"""Ilustrações do post 5 (dia 4, 21/10)."""
from ilus import *


def tempo():
    commits = ("00:02 00:27 00:30 00:52 01:09 01:16 01:22 01:26 01:32 01:47 01:47 01:48 06:30 06:45 06:56 "
               "07:07 07:26 07:30 07:45 07:55 07:59 08:08 08:15 08:32 13:21 13:51 13:54 14:30 16:11 16:36 "
               "16:52 17:07 17:43 18:21 19:11 21:02 21:19 21:45 22:51 23:00").split()
    falas = ("00:24 06:24 06:35 07:19 07:52 07:58 13:17 13:36 13:50 13:58 14:00 14:01 14:54 14:55 15:18 "
             "15:20 15:24 16:21 16:40 17:02 17:29 18:03 18:10 18:34 19:26 19:29 20:42 20:43 21:07 21:16 "
             "21:21 21:26 22:33 22:35 22:48 22:58 23:00 23:04 23:14 23:26").split()
    linha_do_tempo("44-dia4-linha-do-tempo.png", "October 21, hour by hour", commits, falas,
                   notas=[("06:35", "6:35 a.m.: more assembly?", "l"),
                          ("13:50", "1:50 p.m.: Bloodlines water", "l"),
                          ("22:33", "10:33 p.m.: can the gate rotate?", "r")],
                   sombras=[(1.9, 6.3, "nobody working"), (8.6, 13.2, "quiet")])


def mermen():
    barras("45-mermen-teto.png", "Mermen on screen at once, mermen room",
           ["before, at worst", "after my rule"], [7, 3], [GRAY, GREEN], w=1200, h=330, maxv=8,
           notas=["4 placed in the room + 3 from the spawner", "\"no more than 3, at any moment\""])


def morte():
    import random
    t = Tela(1200, 520, "The red merman's death, before and after", "DIAGRAM")
    d = t.d
    def corpo(cx, cy):
        d.ellipse((cx - 22, cy - 22, cx + 22, cy + 22), fill=RED, outline=INK, width=3)
    random.seed(4)
    cx, cy = 300, 380
    corpo(cx, cy)
    for i in range(6):
        x, y = cx + random.randint(-200, 200), cy - random.randint(60, 250)
        d.line((cx, cy, x, y), fill=(200, 200, 200), width=2)
        d.rectangle((x - 9, y - 9, x + 9, y + 9), fill=YELLOW, outline=INK, width=2)
    t.texto(cx, 430, "6 pieces, 6 smoke clouds,\nshape and angle drawn at random", 17, INK, True, "mt")
    import math
    cx = 900
    corpo(cx, cy)
    for ang, v in ((-40, 200), (0, 240), (40, 200)):
        a = math.radians(ang - 90)
        x, y = cx + v * math.cos(a), cy + v * math.sin(a)
        t.seta(cx, cy, x, y, BLUE, 3)
        d.rectangle((x - 11, y - 11, x + 11, y + 11), fill=YELLOW, outline=INK, width=2)
    t.texto(cx, 430, "3 pieces, 3 clouds,\na fixed fan at -40, 0 and 40 degrees", 17, INK, True, "mt")
    t.salva("46-merman-morte.png")


def rotacao():
    t = Tela(1200, 420, "Rotating the drawbridge in real time: the bill")
    d = t.d
    x0, x1, y = 330, 1100, t.top + 90
    esc = (x1 - x0) / 30
    for i, (r, v, c) in enumerate((("one frame lasts", 16.7, GREEN), ("one redraw of the bridge", 26, RED))):
        yy = y + i * 110
        d.text((x0 - 16, yy + 30), r, font=fonte(19), fill=INK, anchor="rm")
        d.rectangle((x0, yy, x0 + v * esc, yy + 60), fill=c, outline=INK, width=3)
        d.text((x0 + v * esc + 12, yy + 30), f"{v:g} ms", font=fonte(20), fill=INK, anchor="lm")
    t.texto(600, 350, "The Mega CD's rotation chip, by Claude's estimate, needs more than a whole frame to turn the bridge once.\nThe port uses 17 pre-drawn angles instead.",
            16, INK, False, "mt")
    t.salva("47-rotacao-custo.png")


BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


def pontilhado():
    t = Tela(1200, 470, "Dissolving without transparency: a 4 x 4 Bayer dither", "DIAGRAM")
    d = t.d
    # porta genérica 12 x 20 "pixels" de 8 px
    def porta(x0, y0, nivel):
        for j in range(20):
            for i in range(12):
                if BAYER[j % 4][i % 4] < nivel:
                    continue
                c = (150, 40, 40) if (i in (0, 11) or j in (0, 19)) else (190, 60, 50)
                if i == 9 and j == 10:
                    c = YELLOW
                d.rectangle((x0 + i * 8, y0 + j * 8, x0 + i * 8 + 7, y0 + j * 8 + 7), fill=c)
    for k, n in enumerate((0, 4, 8, 12, 16)):
        x = 80 + k * 220
        porta(x, 130, n)
        d.rectangle((x - 4, 126, x + 100, 294), outline=GRAY, width=1)
        t.texto(x + 48, 310, f"{n * 100 // 16}% gone", 17, INK, True, "mt")
    t.texto(600, 370, "Each step removes the pixels whose number in the 4 x 4 grid is below the threshold.\nThe same trick dissolves Alucard when he turns into the bat or the wolf.",
            16, INK, False, "mt")
    t.salva("48-pontilhado-bayer.png")


def reflexo():
    t = Tela(1200, 660, "Bloodlines-style water", "DIAGRAM")
    d = t.d
    x0, y0, w = 60, 110, 520
    lin = 300
    # cena acima: colunas e arcos simplificados
    d.rectangle((x0, y0, x0 + w, lin), fill=(60, 50, 80))
    for i in range(4):
        cx = x0 + 60 + i * 130
        d.rectangle((cx - 18, y0 + 60, cx + 18, lin), fill=(170, 160, 150))
        d.ellipse((cx - 40, y0 + 10, cx + 40, y0 + 90), outline=(170, 160, 150), width=8)
    # vampiro e merman genéricos
    d.rectangle((x0 + 200, lin - 70, x0 + 222, lin), fill=(40, 90, 50))
    d.rectangle((x0 + 360, lin - 60, x0 + 384, lin), fill=(200, 120, 40))
    # reflexo espelhado e escurecido
    sub = t.im.crop((x0, lin - 190, x0 + w, lin)).transpose(Image.FLIP_TOP_BOTTOM)
    sub = Image.eval(sub, lambda v: v // 2)
    t.im.paste(sub, (x0, lin))
    d.rectangle((x0 + 200, lin, x0 + 222, lin + 70), fill=(30, 25, 40))  # sem reflexo do Alucard
    d.rectangle((x0, y0, x0 + w, lin + 190), outline=INK, width=4)
    for x in range(x0 - 20, x0 + w + 20, 16):
        d.line((x, lin, x + 8, lin), fill=RED, width=3)
    t.texto(x0 + 211, lin + 80, "no\nreflection", 13, YELLOW, True, "mt")
    t.texto(x0 + 211, lin - 100, "Alucard", 13, PAPER, True, "mt")
    t.texto(x0 + 372, lin - 90, "merman", 13, PAPER, True, "mt")
    passos = [("Above the line", "the room, drawn normally"),
              ("At the waterline", "an interrupt turns on the VDP's\nshadow mode and points the\nbackground at mirrored rows"),
              ("Below the line", "the room upside down, darker:\na reflection, not transparency"),
              ("Alucard", "half vampire, so no reflection.\nMy rule.")]
    y = 125
    for tit, txt in passos:
        t.texto(640, y, tit, 19, BLUE, True)
        t.texto(640, y + 28, txt, 16)
        y += 128
    t.salva("49-agua-bloodlines.png")


def fade():
    t = Tela(1200, 380, "A room transition faded in the palette, Gunstar Heroes style", "DIAGRAM")
    d = t.d
    cores = [(200, 38, 44), (21, 146, 74), (244, 196, 0), (4, 100, 182), (220, 220, 220), (140, 90, 60)]
    for k in range(8):
        x = 70 + k * 135
        f = 1 - k / 7
        for j, c in enumerate(cores):
            cc = tuple(int(v * f) for v in c)
            d.rectangle((x, 120 + j * 30, x + 100, 146 + j * 30), fill=cc, outline=INK)
        t.texto(x + 50, 310, f"step {k}", 15, INK, True, "mt")
    t.texto(600, 340, "Eight steps, only colors change. No sprites, no layers, nearly free.", 16, INK, False, "mt")
    t.salva("50-fade-paleta.png")


def asm():
    barras("51-laco-asm.png", "One loop of the sub-CPU, rewritten in assembly (mermen room)",
           ["C version", "assembly"], [20, 13], [GRAY, GREEN], unidade="% of the frame", w=1200, h=330, maxv=25,
           notas=["the end-of-frame pass over the entities", "same results, frame by frame"])


if __name__ == "__main__":
    tempo(); mermen(); morte(); rotacao(); pontilhado(); reflexo(); fade(); asm()
