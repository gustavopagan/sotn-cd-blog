#!/usr/bin/env python3
"""Ilustrações do post 6 (dia 5, 22/10)."""
from ilus import *


def tempo():
    commits = ("00:36 00:36 00:36 00:36 10:16 10:36 15:10 17:16 17:37 17:43 17:48 17:49 17:56 18:02 18:05 "
               "18:05 18:12 18:15 18:22 18:24 19:23 19:26 19:26 20:05 20:19 20:45 20:46 20:56 21:23 21:24 "
               "21:32 21:37 21:37 21:48 21:53 21:54 22:06 22:35 22:49 22:50 22:51 22:52 23:01 23:07 23:07 "
               "23:11 23:33 23:56").split()
    falas = ("10:14 10:16 10:17 10:19 15:08 17:26 17:29 17:32 17:36 17:45 18:01 19:20 19:25 19:26 19:28 "
             "19:31 19:33 19:35 19:42 19:43 19:44 19:46 19:51 19:51 19:51 19:55 19:57 19:59 20:08 20:10 "
             "20:30 20:35 20:43 21:10 21:16 21:19 21:27 21:29 21:35 21:40 21:47 21:57 22:07 22:10 22:12 "
             "22:45 23:01 23:03 23:04 23:05 23:08 23:13 23:23 23:25 23:27 23:29 23:30").split()
    linha_do_tempo("56-dia5-linha-do-tempo.png", "October 22, hour by hour", commits, falas,
                   notas=[("15:08", "3:08 p.m.: Comix Zone balloons?", "r"),
                          ("17:29", "5:29 p.m.: one chat per task", "l"),
                          ("21:40", "9:40 p.m.: balloons approved", "r")],
                   sombras=[(0.7, 10.2, "quiet")])


def frentes():
    t = Tela(1200, 640, "October 22: one chat per task", "DIAGRAM")
    d = t.d
    caixas = [("Death scene", "text and balloons", BLUE),
              ("Weapons", "sword, shield, colors", RED),
              ("Effects", "glows, dither", GREEN),
              ("Save room", "the 3D coffin", GRAY),
              ("Enemies", "rotating parts", YELLOW),
              ("Castle maps", "every room", BLUE)]
    w, gap = 170, 22
    x0 = (1200 - (6 * w + 5 * gap)) // 2
    for i, (a, b, c) in enumerate(caixas):
        x = x0 + i * (w + gap)
        t.caixa(x, 120, x + w, 250, a, c if c != YELLOW else (190, 150, 0), [b], tam=15)
        t.seta(x + w // 2, 256, 600, 410, GRAY, 3, cab=12)
    t.caixa(420, 420, 780, 540, "main build", INK, ["each finished task", "merged here and retested"], tam=16)
    t.texto(600, 570, "Each chat works on its own copy of the project. The ones I approve get added to the main build.",
            16, INK, False, "mt")
    t.salva("57-frentes-paralelas.png")


def paleta():
    t = Tela(1200, 520, "Alucard's 15 colors, renegotiated", "DIAGRAM")
    d = t.d
    fixas = {2: ((255, 0, 38), "red\n#ff0026"), 3: ((252, 180, 72), "gold"),
             5: ((76, 0, 255), "blue\n#4c00ff"), 7: ((2, 201, 62), "green\n#02c93e"),
             10: ((28, 179, 255), "light blue\n#1cb3ff")}
    tons = [(40, 30, 40), (70, 60, 70), (110, 90, 100), (150, 130, 130), (190, 170, 160), (230, 215, 200),
            (60, 40, 30), (110, 70, 50), (160, 110, 70), (90, 30, 40), (140, 50, 60), (200, 90, 90),
            (30, 40, 70), (60, 80, 120), (220, 220, 230)]
    def linha(y, rot, depois):
        t.texto(60, y + 30, rot, 18, INK, True, "lm")
        for i in range(15):
            x = 250 + i * 60
            c = fixas[i][0] if depois and i in fixas else tons[i]
            d.rectangle((x, y, x + 52, y + 60), fill=c, outline=INK, width=3 if depois and i in fixas else 1)
            if depois and i in fixas:
                t.texto(x + 26, y + 70, fixas[i][1], 12, INK, True, "mt")
    linha(130, "before", False)
    linha(290, "after", True)
    t.texto(600, 450, "Five slots now hold fixed colors, picked by me, for every sword, shield and item in the game.\nAlucard was redrawn with the other ten.",
            16, INK, False, "mt")
    t.salva("58-paleta-alucard.png")


def pisca():
    t = Tela(1200, 470, "How an item on the floor asks for attention", "DIAGRAM")
    d = t.d
    x0, x1 = 160, 1140
    seg = (x1 - x0) / 6.0
    X = lambda s: x0 + s * seg
    for s in range(7):
        d.line((X(s), 360, X(s), 372), fill=INK, width=2)
        t.texto(X(s), 378, f"{s} s", 15, INK, False, "mt")
    d.line((x0, 360, x1, 360), fill=INK, width=2)
    t.texto(140, 160, "outline", 17, INK, True, "rm")
    t.texto(140, 260, "white flash", 17, INK, True, "rm")
    # contorno: pisca a 15 Hz nos 2 primeiros segundos
    k = 0.0
    while k < 2:
        d.rectangle((X(k), 140, X(k + 1 / 30), 180), fill=BLUE)
        k += 2 / 15
    # flash: 3 piscadas a 15 Hz a cada 2 s
    for base in (2, 4, 6):
        for j in range(3):
            a = base - 0.4 + j * 2 / 15
            if a < 6:
                d.rectangle((X(a), 240, X(a + 1 / 15), 280), fill=YELLOW, outline=INK)
    t.texto(X(1), 196, "blinks for the first 2 s", 15, BLUE, True, "mt")
    t.texto(X(4), 296, "3 quick flashes, every 2 s", 15, (150, 110, 0), True, "mt")
    t.texto(600, 420, "The first version was a dithered glow. It drowned the items, so I asked for short white flashes instead.",
            16, INK, False, "mt")
    t.salva("59-item-pisca.png")


def baloes():
    t = Tela(1200, 560, "Where a speech balloon goes", "DIAGRAM")
    d = t.d
    def pessoa(x, y, c):
        d.ellipse((x - 18, y - 18, x + 18, y + 18), fill=c, outline=INK, width=3)
        d.rectangle((x - 20, y + 20, x + 20, y + 110), fill=c, outline=INK, width=3)
    def balao(x0, y0, x1, y1, tx, ty):
        d.rounded_rectangle((x0, y0, x1, y1), 18, fill=PAPER, outline=INK, width=3)
        bx = min(max(tx, x0 + 30), x1 - 30)
        d.polygon([(bx - 14, y1 - 2), (bx + 14, y1 - 2), (tx, ty)], fill=PAPER, outline=INK)
        d.line((bx - 12, y1 - 2, bx + 12, y1 - 2), fill=PAPER, width=4)
        for k in range(3):
            d.line((x0 + 20, y0 + 22 + k * 18, x1 - 20 - k * 30, y0 + 22 + k * 18), fill=GRAY, width=6)
    # errado
    pessoa(200, 300, GREEN)
    pessoa(420, 300, (90, 60, 120))
    balao(120, 230, 300, 320, 200, 300)
    t.texto(310, 460, "Before: centered on the speaker,\ncovering the face", 16, RED, True, "mt")
    # certo
    pessoa(800, 300, GREEN)
    pessoa(1020, 300, (90, 60, 120))
    balao(790, 140, 980, 230, 805, 272)
    t.seta(990, 185, 1010, 250, GRAY, 2, cab=8)
    t.texto(910, 460, "After: shifted toward the listener,\ntail near the speaker's head,\nshown half a second late", 16, GREEN, True, "mt")
    t.texto(200, 420, "speaker", 14, INK, False, "mt")
    t.texto(420, 420, "listener", 14, INK, False, "mt")
    t.texto(800, 420, "speaker", 14, INK, False, "mt")
    t.texto(1020, 420, "listener", 14, INK, False, "mt")
    t.salva("60-baloes-regras.png")


if __name__ == "__main__":
    tempo(); frentes(); paleta(); pisca(); baloes()
