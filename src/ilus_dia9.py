#!/usr/bin/env python3
"""Ilustrações do post 10 (dia 9, 26/10)."""
from ilus import *

C = ["23:46"]
F = ("00:19 00:54 00:58 01:01 01:03 13:26 13:37 13:53 14:09 15:04 15:16 15:21 15:26 16:56 17:01 17:04 "
     "17:10 17:40 17:45 17:49 17:57 17:58 19:04 19:08 19:26 19:33 20:38 20:53 20:54 20:55 21:00 21:02 "
     "21:03 21:04 21:06 21:08 21:20 21:23 21:25 21:36 21:40 21:45 21:46 21:47 21:50 21:56 21:59 22:07 22:11").split()


def tempo():
    linha_do_tempo("91-dia9-linha-do-tempo.png", "October 26, hour by hour", C, F,
                   notas=[("17:57", "5:57 p.m.: \"8 tones is the sweet spot\"", "r"),
                          ("21:04", "9:04 p.m.: \"I'm physically sitting here\"", "r")])


def dois_pcs():
    t = Tela(900, 600, "9:03 p.m.: which computer?", "MOCKUP")
    d = t.d
    def pc(x, nome, cor, txt, laptop=True):
        d.rectangle((x, 140, x + 320, 340), fill=(30, 30, 40), outline=INK, width=4)
        d.rectangle((x + 16, 156, x + 304, 324), fill=cor)
        if laptop:
            d.polygon([(x - 30, 350), (x + 350, 350), (x + 380, 390), (x - 60, 390)], fill=(170, 170, 175), outline=INK)
        else:
            d.rectangle((x + 140, 340, x + 180, 372), fill=(170, 170, 175), outline=INK)
            d.rectangle((x + 90, 372, x + 230, 390), fill=(170, 170, 175), outline=INK)
        t.texto(x + 160, 410, nome, 24, INK, True, "mt")
        t.texto(x + 160, 240, txt, 20, PAPER, True, "mm")
    pc(80, "Mac", (60, 60, 70), "Claude is\nlooking here", False)
    pc(500, "Windows notebook", BLUE, "I am\ntyping here")
    t.seta(470, 100, 380, 140, RED, 5)
    t.texto(450, 480, "\"I'm physically sitting in front of the notebook,\nwith my hands on its keyboard.\"", 22, RED, True, "mt")
    t.salva("92-dois-computadores.png")


if __name__ == "__main__":
    tempo(); dois_pcs()
