#!/usr/bin/env python3
"""Ilustrações do post 13 (dia 12, 29/10)."""
from ilus import *


def tempo():
    C = ("01:18 01:20 06:35 06:35 07:07 08:35 08:36 08:45 08:45 14:20 14:35 15:29 15:39 15:39 17:25 22:41 22:57 23:31").split()
    F = ("00:38 00:43 00:45 00:46 00:49 00:59 01:00 01:02 01:04 01:05 01:07 10:18 10:21 10:22 10:25 10:43 10:45 "
         "11:30 11:36 13:55 13:57 13:59 14:03 14:05 14:06 18:55 18:58 19:01 19:36 19:37 19:39 19:41 19:44 19:51 "
         "20:10 20:11 20:39 20:40 20:41 21:30 21:40 21:52 22:47 22:54 23:02 23:04").split()
    linha_do_tempo("103-dia12-linha-do-tempo.png", "October 29, hour by hour", C, F,
                   notas=[("01:02", "1:02 a.m.: how big is the Backup RAM?", "l"),
                          ("14:03", "2:03 p.m.: Mike Tyson explains", "l"),
                          ("22:47", "10:47 p.m.: moving to the desktop", "r")])


def bram():
    t = Tela(900, 520, "Saving on a Mega CD", "DIAGRAM")
    d = t.d
    t.caixa(60, 110, 420, 330, "PlayStation", GRAY, ["a memory card,", "15 blocks,", "several saves"], tam=22)
    t.caixa(480, 110, 840, 330, "Mega CD", BLUE, ["8 KB of Backup RAM", "inside the console,", "shared by every game"], tam=22)
    t.texto(450, 380, "The port saves HP, level, gold, the room and which doors are open.\nIn the space the console has, one save fits.", 21, INK, False, "mt")
    t.salva("104-bram.png")


def tyson():
    t = Tela(900, 360, "2:03 p.m.", "MOCKUP")
    d = t.d
    d.rounded_rectangle((300, 110, 860, 200), 22, fill=BLUE)
    t.texto(580, 155, "explain it as if you were Mike Tyson", 26, PAPER, True, "mm")
    d.rounded_rectangle((40, 230, 600, 310), 22, fill=LIGHT, outline=GRAY)
    t.texto(320, 270, "(Claude's answer is not in my archive)", 20, GRAY, False, "mm")
    t.salva("105-tyson.png")


if __name__ == "__main__":
    tempo(); bram(); tyson()
