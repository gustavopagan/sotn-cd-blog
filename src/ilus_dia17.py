#!/usr/bin/env python3
"""Ilustrações do post 18 (dia 17, 03/11)."""
from ilus import *
C = "00:08 00:08 00:20 00:24 00:54 01:10 01:26 01:44 14:37 15:04 15:12 15:25 17:06 17:43 17:52 19:45 19:57 19:59 20:01 20:20".split()
F = "00:00 00:15 00:17 00:18 00:51 00:53 01:15 01:22 01:28 11:22 11:24 11:25 11:46 13:55 13:57 14:00 14:08 14:24 14:25 14:27 14:29 14:32 14:45 17:35 17:42 17:43 17:51 17:52 18:54 19:13 19:40 19:43 20:11 20:13 20:16 20:47 20:51 20:57 20:58 21:00 22:20 23:19 23:28 23:35".split()


def tempo():
    linha_do_tempo("127-dia17-linha-do-tempo.png", "November 3, hour by hour", C, F,
                   notas=[("11:24", "11:24 a.m.: \"always answer like this\"", "l"),
                          ("14:00", "2:00 p.m.: four legs, one object", "l"),
                          ("20:16", "8:16 p.m.: big enemies go to the background", "r")])


def leigo():
    t = Tela(900, 470, "11:24 a.m.", "MOCKUP")
    d = t.d
    d.rounded_rectangle((40, 100, 600, 180), 22, fill=LIGHT, outline=GRAY)
    t.texto(320, 140, "(a summary in plain words)", 22, GRAY, False, "mm")
    d.rounded_rectangle((200, 210, 860, 400), 22, fill=BLUE)
    t.texto(530, 305, "\"Wow, this answer turned out really good,\nI could understand it! Give me a rule I can\nadd to the project so you always\nanswer me like this.\"", 22, PAPER, True, "mm")
    t.salva("128-resposta-leiga.png")


def pernas():
    t = Tela(900, 520, "Four legs, one object", "DIAGRAM")
    d = t.d
    def perna(x, y, c):
        d.rectangle((x, y, x + 34, y + 120), fill=c, outline=INK, width=3)
        d.rectangle((x - 6, y + 112, x + 44, y + 132), fill=c, outline=INK, width=3)
    for i in range(4):
        perna(80 + i * 70, 160, [GREEN, BLUE, RED, (190, 150, 0)][i])
        t.texto(97 + i * 70, 310, f"#{i + 1}", 18, INK, True, "mt")
    t.texto(200, 360, "4 entities, each moving\non its own", 20, INK, False, "mt")
    t.seta(400, 230, 500, 230, INK, 5)
    d.rectangle((560, 140, 840, 310), outline=INK, width=3)
    for i in range(4):
        perna(580 + i * 64, 160, GREEN)
    t.texto(700, 360, "1 entity: the legs\nmove together", 20, INK, False, "mt")
    t.texto(450, 450, "My proposal for the Diplocephalus's front legs. The cost: they lose their independence.", 18, GRAY, False, "mt")
    t.salva("129-pernas.png")


def fundo():
    t = Tela(900, 560, "Big enemies drawn on a background plane", "DIAGRAM")
    t.caixa(40, 110, 420, 330, "as sprites", RED, ["counted on every line,", "16 per line at most,", "pieces blink when full"], tam=21)
    t.caixa(480, 110, 860, 330, "on a plane", GREEN, ["drawn like scenery,", "no sprite limit,", "moved by scrolling"], tam=21)
    t.texto(450, 380, "The catch I pointed out at 8:51 p.m.: a piece partly in front of a pillar\ncan end up behind it by accident, because the plane has one depth.", 20, INK, False, "mt")
    t.salva("130-inimigo-no-fundo.png")


if __name__ == "__main__":
    tempo(); leigo(); pernas(); fundo()
