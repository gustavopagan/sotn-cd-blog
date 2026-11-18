#!/usr/bin/env python3
"""Ilustrações do post 11 (dia 10, 27/10)."""
from ilus import *

C = ("02:48 04:03 04:25 04:58 05:06 05:09 05:43 12:20 14:50 15:10 16:27 17:51 18:40").split()
F = "08:14 09:54 13:46 16:19 16:22 16:27 16:48 17:57 18:16 18:19 19:24 23:44 23:46 23:50 23:53".split()


def tempo():
    linha_do_tempo("95-dia10-linha-do-tempo.png", "October 27, hour by hour", C, F,
                   notas=[("16:27", "4:27 p.m.: \"inventory only\"", "l"),
                          ("18:16", "6:16 p.m.: back to streaming?", "l"),
                          ("23:50", "11:50 p.m.: \"too many codes\"", "r")])


def compressao():
    t = Tela(900, 620, "Every object frame in the castle, compressed four ways")
    d = t.d
    dados = [("raw", 19.74, GRAY), ("LZ4W (in use)", 10.09, BLUE), ("LZSA2", 7.40, GREEN), ("ZX0", 6.89, (0, 110, 50))]
    x0, x1, y = 250, 820, 110
    for i, (n, v, c) in enumerate(dados):
        yy = y + i * 105
        d.text((x0 - 14, yy + 32), n, font=fonte(22), fill=INK, anchor="rm")
        d.rectangle((x0, yy, x0 + (x1 - x0) * v / 24, yy + 64), fill=c, outline=INK, width=3)
        d.text((x0 + (x1 - x0) * v / 24 + 10, yy + 32), f"{v:.1f} MB", font=fonte(22), fill=INK, anchor="lm")
    t.texto(450, 540, "Summed over every package on the disc. Smaller costs more time to unpack:\nLZSA2 went to loading screens, LZ4W stayed for what unpacks mid-game.", 20, INK, False, "mt")
    t.salva("96-compressao.png")



def codigos():
    t = Tela(900, 640, "What I was looking at, 11:50 p.m.", "MOCKUP")
    d = t.d
    linhas = ["D104  D105  D106  D107  D114", "DA1  DA4  DA6     (weapons chat)", "DFX1  DFX3  DFX5  (effects chat)",
              "DSV1  DSV7        (save room chat)", "DR1  DR8  DR10    (rotation chat)", "DC14  DC17  DC21  (scenery chat)",
              "DK1  DK2          (color chat)", "DZ1  DZ4          (compression chat)", "TK1  TC17  TFX4  TA3  (tests)",
              "B-001  B-004      (backlog)"]
    d.rectangle((60, 100, 840, 560), fill=(20, 20, 26), outline=INK, width=4)
    for i, l in enumerate(linhas):
        t.texto(90, 124 + i * 42, l, 22, (120, 230, 140), True, mono=True)
    t.texto(450, 580, "Every chat numbered its own decisions and tests. Real codes from that week.", 19, INK, False, "mt")
    t.salva("97-codigos.png")


if __name__ == "__main__":
    tempo(); compressao(); codigos()
