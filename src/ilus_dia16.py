#!/usr/bin/env python3
"""Ilustrações do post 17 (dia 16, 02/11)."""
from ilus import *
C = "00:08 00:10 00:12 00:28 00:28 00:30 00:30 00:33 00:45 00:45 00:46 00:48 00:50 00:50 01:00 01:00 01:01 01:02 01:10 01:19 01:20 01:25 01:25 01:41 01:46 01:49 01:50 01:55 01:55 02:02 02:04 02:06 02:13 02:14 02:16 02:20 02:36 02:56 03:21 03:25 03:31 03:33 03:48 03:52 04:02 04:02 04:04 14:19 14:52 14:52 14:59 15:07 15:17 15:17 15:23 15:31 15:33 15:58 19:03 19:08 19:14 20:11 20:15 20:24 21:07 21:13 22:03 22:10 23:04 23:15 23:24 23:31 23:31 23:59".split()
F = "00:01 00:04 00:06 00:11 00:24 00:25 00:28 00:29 00:31 00:36 00:43 00:44 00:46 00:50 00:52 00:53 00:54 00:56 00:57 01:37 01:39 01:46 01:47 01:52 01:54 01:58 01:59 02:01 02:02 02:05 02:07 02:10 02:11 02:16 02:17 02:41 02:43 02:46 02:52 02:53 02:58 03:00 04:52 04:53 12:35 12:53 12:59 13:47 14:10 17:40 17:46 17:53 17:57 18:21 18:52 18:55 18:57 18:59 19:00 19:02 19:04 20:19 20:21 20:24 20:26 20:27 20:49 21:09 21:27 21:29 21:41 22:00 22:04 23:03 23:13 23:15 23:20 23:23 23:28 23:29 23:41 23:43 23:45 23:50 23:56 23:57".split()


def tempo():
    linha_do_tempo("125-dia16-linha-do-tempo.png", "November 2, hour by hour", C, F,
                   notas=[("01:37", "1:37 a.m.: frames 34 to 80, by hand", "l"),
                          ("20:24", "8:24 p.m.: a fixed cycle?", "l"),
                          ("22:00", "10:00 p.m.: the rules are too rigid", "r")])


def ciclo():
    t = Tela(900, 680, "My proposal for the Diplocephalus", "DIAGRAM")
    import math
    passos = ["two steps\nforward", "spit fire", "two steps\nback", "spit fire"]
    cores = [GREEN, RED, BLUE, RED]
    cx, cy, r = 450, 350, 200
    for i, (p, c) in enumerate(zip(passos, cores)):
        a = math.radians(-90 + i * 90)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        t.caixa(int(x - 110), int(y - 50), int(x + 110), int(y + 50), None, c, [], tam=20, fundo=c)
        t.texto(x, y - (14 if "\n" in p else 0), p, 22, PAPER, True, "mm")
    for i in range(4):
        a0 = math.radians(-90 + i * 90 + 25); a1 = math.radians(-90 + i * 90 + 65)
        t.seta(cx + r * math.cos(a0), cy + r * math.sin(a0), cx + r * math.cos(a1), cy + r * math.sin(a1), INK, 4)
    t.texto(450, 338, "a loop that\nignores\nthe player", 19, INK, True, "mm")
    t.texto(450, 625, "If the routine never changes, every frame of it can be prepared in advance.", 20, INK, False, "mt")
    t.salva("126-diplo-ciclo.png")


if __name__ == "__main__":
    tempo(); ciclo()
