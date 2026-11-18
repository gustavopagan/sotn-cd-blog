#!/usr/bin/env python3
"""Ilustrações do post 14 (dia 13, 30/10)."""
from ilus import *

C = ("21:47 22:12 22:14 22:18 22:20 22:27 22:30 22:37 22:38 22:41 22:54 22:55 22:56 23:00 23:19 23:22 23:25 "
     "23:36 23:53").split()
F = ("00:29 00:37 00:38 00:39 00:41 00:46 00:52 00:54 00:58 00:59 01:01 01:02 01:22 01:23 01:31 01:33 01:36 "
     "01:38 02:02 02:07 02:11 21:04 21:06 21:11 21:31 21:45 21:56 21:57 21:58 21:59 22:02 22:03 22:04 22:09 "
     "22:12 22:16 22:22 22:30 22:31 22:36 22:40 22:41 22:42 22:44 22:46 22:48 22:51 22:57 23:00 23:15").split()


def tempo():
    linha_do_tempo("108-dia13-linha-do-tempo.png", "October 30, hour by hour", C, F,
                   notas=[("00:37", "12:37 a.m.: \"I switched computers\"", "l"),
                          ("21:59", "9:59 p.m.: more resources for YOUR VM", "r")])


def fila():
    t = Tela(900, 640, "The build queue, born October 30", "DIAGRAM")
    t.caixa(40, 110, 400, 290, "Claude's workspace", BLUE, ["edits code, runs", "tests in the emulator,", "asks for a build"], tam=21)
    t.caixa(500, 110, 860, 290, "WSL on my desktop", GREEN, ["Linux inside Windows,", "with the desktop's", "cores and memory"], tam=21)
    t.caixa(270, 380, 630, 560, "fila (queue) folder", (190, 150, 0), ["a request goes in", "as a small file,", "the log comes back"], tam=21)
    t.seta(220, 296, 330, 374, INK, 4, "request")
    t.seta(570, 374, 680, 296, INK, 4)
    t.seta(700, 296, 600, 374, GRAY, 3)
    t.texto(450, 590, "Full builds now run on the desktop. A whole build took 136 seconds there.", 20, INK, False, "mt")
    t.salva("109-fila.png")


def mudanca():
    t = Tela(900, 420, "October 29-30: moving house", "DIAGRAM")
    t.caixa(40, 120, 280, 300, "pagan-laptop", GRAY, ["the project's home", "until October 29"], tam=21)
    t.caixa(330, 140, 570, 280, "external drive", (190, 150, 0), ["the whole", "project folder"], tam=21)
    t.caixa(620, 120, 860, 300, "pagan (desktop)", GREEN, ["more cores,", "more memory"], tam=21)
    t.seta(285, 210, 325, 210, INK, 4)
    t.seta(575, 210, 615, 210, INK, 4)
    t.texto(450, 340, "Machine names as they appear in my messages.", 18, GRAY, False, "mt")
    t.salva("110-mudanca.png")


if __name__ == "__main__":
    tempo(); fila(); mudanca()
