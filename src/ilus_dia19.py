#!/usr/bin/env python3
"""Ilustrações do post 20 (dia 19, 05/11)."""
from ilus import *
C = "00:04 00:04 00:49 00:53 01:30 01:46 01:52 01:53 01:55 01:57 02:17 02:33 12:22 12:22 12:24 13:02 13:04 13:04 13:07 13:56 14:08 14:08 14:15 14:33 14:34 14:53 15:07 15:14 15:25 15:39 15:40 15:47 15:58 15:59 16:25 16:25 16:35 17:45 18:14 18:18 18:24 18:32 18:36 18:50 19:01 19:05 19:09 19:22 23:37 23:43 23:43 23:47 23:49".split()
F = "00:09 00:10 12:02 12:08 12:19 14:00 14:07 14:26 14:27 15:01 16:21 16:22 16:24 17:15 17:16 17:33 17:37 18:20 18:28 23:37 23:42 23:45 23:48".split()


def antes_depois():
    t = Tela(900, 600, "How I reported problems, before and after", "DIAGRAM")
    t.caixa(40, 110, 420, 470, "before", GRAY, ["play in RetroArch,", "describe it in words,", "save a state, find", "the file, paste the path,", "hope Claude reproduces it"], tam=21)
    t.caixa(480, 110, 860, 470, "with the live editor", GREEN, ["play in the editor,", "press F8, click on", "the thing that's wrong,", "write a comment;", "Claude reads it all"], tam=21)
    t.texto(450, 520, "Each comment is saved with pictures of the screen, in a folder Claude can open.", 19, INK, False, "mt")
    t.salva("136-live-antes-depois.png")


if __name__ == "__main__":
    linha_do_tempo("137-dia19-linha-do-tempo.png", "November 5, hour by hour", C, F,
                   notas=[("16:22", "4:22 p.m.: why is the HUD all sprites?", "l"),
                          ("17:33", "5:33 p.m.: a live editor?", "r")])
    antes_depois()
