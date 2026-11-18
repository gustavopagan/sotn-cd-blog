#!/usr/bin/env python3
"""Ilustrações do post 9 (dia 8, 25/10)."""
from ilus import *

C = "01:35 01:56 02:09 02:15 03:03 20:09 20:21 20:21".split()
F = ("00:31 00:32 00:53 00:54 00:55 00:59 01:00 01:02 01:03 01:38 01:39 01:57 20:09 20:14 20:41 "
     "20:44 21:04 23:08 23:17 23:27 23:31 23:32 23:46").split()


def tempo():
    linha_do_tempo("86-dia8-linha-do-tempo.png", "October 25, a Sunday", C, F,
                   notas=[("00:53", "12:53 a.m.: borrow a Sonic sound", "l"),
                          ("20:14", "8:14 p.m.: colors approved", "r"),
                          ("23:27", "11:27 p.m.: every item, Alucard's colors", "r")])


def acorde():
    t = Tela(900, 560, "Two notes from one FM channel", "DIAGRAM")
    d = t.d
    t.texto(450, 90, "One YM2612 channel has four operators.", 24, INK, True, "mt")
    ops = [("op 1", "x 4", BLUE), ("op 2", "x 3", RED), ("op 3", "", GRAY), ("op 4", "", GRAY)]
    for i, (n, r, c) in enumerate(ops):
        x = 70 + i * 200
        t.caixa(x, 150, x + 160, 270, n, c, [r or "shapes", "" if r else "the tone"], tam=22)
    t.texto(450, 310, "Two of them sound at frequencies in a 4 : 3 ratio,\nwhich is a perfect fourth. One key, two notes.", 22, INK, False, "mt")
    t.texto(450, 410, "My idea: build one instrument per interval the riff needs,\nand play the organ's chords without spending more channels.", 22, BLUE, True, "mt")
    t.salva("87-fm-duas-vozes.png")


def itens():
    t = Tela(900, 560, "Everything you pick up uses Alucard's fixed colors", "DIAGRAM")
    d = t.d
    cores = [(255, 0, 38), (252, 180, 72), (76, 0, 255), (2, 201, 62), (28, 179, 255)]
    for i, c in enumerate(cores):
        d.rectangle((120 + i * 135, 100, 120 + i * 135 + 110, 150), fill=c, outline=INK, width=3)
    # coração
    x, y = 180, 300
    d.ellipse((x - 50, y - 40, x, y + 10), fill=cores[0], outline=INK, width=3)
    d.ellipse((x, y - 40, x + 50, y + 10), fill=cores[0], outline=INK, width=3)
    d.polygon([(x - 48, y - 2), (x + 48, y - 2), (x, y + 60)], fill=cores[0])
    t.texto(x, 390, "hearts", 22, INK, True, "mt")
    # moeda / saco
    x = 450
    d.ellipse((x - 55, y - 50, x + 55, y + 60), fill=cores[1], outline=INK, width=3)
    t.texto(x, y + 5, "$", 52, INK, True, "mm")
    t.texto(x, 390, "money", 22, INK, True, "mt")
    # power-up
    x = 720
    d.rectangle((x - 50, y - 50, x + 50, y + 50), fill=cores[2], outline=INK, width=3)
    d.rectangle((x - 25, y - 25, x + 25, y + 25), fill=cores[4], outline=INK, width=3)
    d.rectangle((x - 8, y - 8, x + 8, y + 8), fill=cores[3])
    t.texto(x, 390, "power-ups", 22, INK, True, "mt")
    t.texto(450, 450, "Generic shapes, not the game's art. The point: no extra palette for items.", 20, GRAY, False, "mt")
    t.salva("88-itens-cores-fixas.png")


if __name__ == "__main__":
    tempo(); acorde(); itens()
