#!/usr/bin/env python3
"""Ilustrações do post 15 (dia 14, 31/10)."""
from ilus import *

F = ("00:36 00:48 00:52 00:54 00:57 00:58 01:01 01:05 01:07 01:09 01:13 01:14 01:20 01:26 01:29 09:20 13:57 14:12 "
     "14:34 14:39 14:49 14:53 15:05 15:14 15:30 15:38 16:49 16:51 17:03 17:29 17:44 17:49 17:51 17:52 17:54 17:56 "
     "17:57 18:06 18:08 18:09 18:10 18:11 18:14 18:20 18:43 18:44 18:49 18:53 19:07 19:08 19:54 19:59 20:02 20:05 "
     "20:11 20:18 20:21 20:52 21:07 21:18").split()


def tempo(C):
    linha_do_tempo("113-dia14-linha-do-tempo.png", "October 31, hour by hour", C, F,
                   notas=[("01:07", "1:07 a.m.: work alone until 10", "l"),
                          ("18:11", "6:11 p.m.: the queue went down", "l"),
                          ("19:59", "7:59 p.m.: my money bags", "r")])


def cores12():
    t = Tela(900, 480, "Twelve colors for everything you pick up", "DIAGRAM")
    d = t.d
    cores = [(0, 0, 0), (255, 0, 38), (252, 180, 72), (180, 110, 40), (76, 0, 255), (2, 201, 62),
             (28, 179, 255), (34, 34, 34), (72, 72, 72), (100, 140, 110), (180, 180, 150), (255, 255, 255)]
    for i, c in enumerate(cores):
        x = 60 + i * 66
        d.rectangle((x, 120, x + 56, 190), fill=c, outline=INK, width=2)
    t.texto(450, 220, "Money, hearts, candles, food, subweapons: every one has to be drawn\nwith these, in every room of the castle.", 22, INK, False, "mt")
    t.texto(450, 330, "\"12 colors for everything is really hard.\"", 26, RED, True, "mt")
    t.texto(450, 380, "That evening I asked for a deep search for one or two more.", 20, INK, False, "mt")
    t.salva("114-doze-cores.png")


if __name__ == "__main__":
    import sys
    tempo(sys.argv[1].split() if len(sys.argv) > 1 else []); cores12()
