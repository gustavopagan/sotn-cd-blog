#!/usr/bin/env python3
"""Mais ilustrações do post 3 (dia 2, 19/10)."""
from ilus import *


def hm(s):
    h, m = s.split(":")
    return int(h) + int(m) / 60


def linha_do_tempo():
    commits = ("00:26 00:29 00:35 00:39 00:43 00:49 01:04 01:12 01:48 01:51 02:03 02:04 02:05 "
               "10:28 10:28 11:27 13:42 13:44 14:20 14:46 15:12 15:26 16:08 16:27 16:54 17:07 "
               "17:24 19:29 20:04 20:16 21:10 21:52 22:06 22:44 23:15").split()
    falas = ("00:23 09:38 10:48 12:35 13:33 13:44 13:49 13:55 14:37 14:38 14:42 14:59 15:03 15:19 "
             "15:58 15:59 16:19 16:31 16:34 16:48 17:12 19:05 19:06 19:11 19:12 19:27 19:54 20:15 "
             "20:19 20:24 21:18 21:24 21:55 22:01 22:19 22:55").split()
    t = Tela(1200, 520, "October 19, hour by hour")
    d = t.d
    x0, x1 = 70, 1150
    X = lambda h: x0 + (x1 - x0) * h / 24
    yc, yf = 250, 370
    # sono
    d.rectangle((X(2.1), 120, X(9.6), 430), fill=(225, 232, 245))
    t.texto(X(5.85), 130, "nobody working", 16, BLUE, True, "mt")
    d.line((x0, yc, x1, yc), fill=INK, width=2)
    d.line((x0, yf, x1, yf), fill=INK, width=2)
    t.texto(x0, yc - 50, "Claude's commits (35)", 18, RED, True)
    t.texto(x0, yf - 50, "my messages", 18, BLUE, True)
    for c in commits:
        x = X(hm(c))
        d.rectangle((x - 3, yc - 22, x + 3, yc + 22), fill=RED)
    for f in falas:
        x = X(hm(f))
        d.ellipse((x - 7, yf - 7, x + 7, yf + 7), fill=BLUE, outline=INK)
    for h in range(0, 25, 3):
        x = X(h)
        d.line((x, 440, x, 450), fill=INK, width=2)
        t.texto(x, 456, f"{h:02d}:00", 15, INK, False, "mt")
    t.seta(X(0.4) + 40, 175, X(0.4), yf - 12, BLUE, 3)
    t.texto(X(0.4) + 44, 160, "12:23 a.m.: I go to bed, Claude keeps going", 15, BLUE, True)
    t.seta(X(22.9) - 30, 300, X(22.9), yf - 12, BLUE, 3)
    t.texto(X(22.9) - 30, 290, "10:55 p.m.: other Mega Drive games\nmust have solved this", 15, BLUE, True, "rs")
    t.salva("25-dia2-linha-do-tempo.png")


def controle():
    t = Tela(1200, 560, "The pad, as laid out that night", "DIAGRAM")
    d = t.d
    # corpo genérico do controle
    d.rounded_rectangle((180, 130, 1020, 470), 150, fill=(40, 40, 44), outline=INK, width=4)
    # direcional
    cx, cy = 340, 300
    d.rectangle((cx - 28, cy - 85, cx + 28, cy + 85), fill=(20, 20, 20))
    d.rectangle((cx - 85, cy - 28, cx + 85, cy + 28), fill=(20, 20, 20))
    t.texto(cx, cy - 120, "UP + X = MIST", 18, YELLOW, True, "mm")
    # start
    d.rounded_rectangle((560, 380, 640, 404), 10, fill=(90, 90, 96))
    t.texto(600, 420, "START: the menu, later", 15, PAPER, True, "mt")
    bot = {"X": (720, 230), "Y": (810, 210), "Z": (900, 230),
           "A": (720, 330), "B": (810, 310), "C": (900, 330)}
    rot = {"X": ("BAT", YELLOW), "Y": ("BACKDASH", YELLOW), "Z": ("WOLF", YELLOW),
           "A": ("LEFT HAND", PAPER), "B": ("JUMP", PAPER), "C": ("RIGHT HAND", PAPER)}
    for k, (x, y) in bot.items():
        nova = k in "XYZ"
        d.ellipse((x - 34, y - 34, x + 34, y + 34), fill=RED if nova else (70, 70, 76), outline=INK, width=3)
        t.texto(x, y, k, 24, PAPER, True, "mm")
    for k in "XYZ":
        x, y = bot[k]
        t.texto(x, y - 52, rot[k][0], 16, YELLOW, True, "mm")
    for k in "ABC":
        x, y = bot[k]
        t.texto(x, y + 50, rot[k][0], 15, PAPER, True, "mt")
    t.texto(600, 500, "Red: the six-button pad's extra row, where the shoulder-button moves went.",
            17, INK, False, "mt")
    t.salva("26-controle-6-botoes.png")


def musica():
    t = Tela(1200, 600, "From the PlayStation disc to a CD track", "DIAGRAM")
    d = t.d
    t.caixa(40, 110, 340, 300, "PS1 disc", BLUE,
            ["music compressed (XA),", "woven between the", "game data, read while", "the game runs"])
    t.caixa(450, 110, 750, 300, "build tools", GREEN,
            ["decode, split intro", "and loop, keep or", "drop the intro"])
    t.caixa(860, 110, 1160, 300, "Mega CD disc", RED,
            ["one plain CD audio", "track per song,", "played by the drive", "itself"])
    t.seta(345, 205, 445, 205)
    t.seta(755, 205, 855, 205)
    # intro + loop
    y = 380
    t.texto(40, y, "One song, the way the original stores it:", 18, INK, True)
    d.rectangle((40, y + 40, 330, y + 100), fill=YELLOW, outline=INK, width=3)
    t.texto(185, y + 70, "intro (once)", 18, INK, True, "mm")
    d.rectangle((330, y + 40, 900, y + 100), fill=BLUE, outline=INK, width=3)
    t.texto(615, y + 70, "loop (forever)", 18, PAPER, True, "mm")
    d.arc((380, y + 95, 860, y + 175), 20, 160, fill=BLUE, width=4)
    t.seta(400, y + 135, 386, y + 103, BLUE, 4)
    t.texto(930, y + 50, "Cut the intro and the\ntrack shrinks. Seven\nsongs kept theirs.", 17, INK, False)
    t.salva("27-musica-xa-cdda.png")


def visitas():
    t = Tela(1200, 520, "One map, two versions of the same area", "DIAGRAM")
    t.caixa(60, 110, 560, 420, "First visit (NO3)", GREEN,
            ["where the game really starts", "", "wargs, zombies, mermen,", "bats, Bone Scimitar",
             "", "the port starts here", "from that night on"])
    t.caixa(640, 110, 1140, 420, "Return visit (NP3)", GRAY,
            ["same rooms, later in the game", "", "Owl Knight, Blade, Gurkha,", "Hammer, Slogra and Gaibon",
             "", "the shortcut used", "for the first tests"])
    t.texto(600, 460, "Same layout. Different enemies. I caught it when the enemy list didn't match my memory.",
            17, INK, False, "mt")
    t.salva("28-no3-np3.png")


def grupos():
    t = Tela(1200, 600, "Room groups: where the music is allowed to stop", "DIAGRAM")
    d = t.d
    cores = [GREEN, GREEN, GREEN, BLUE, BLUE, BLUE, BLUE, RED, RED]
    xs = [60 + i * 122 for i in range(9)]
    for i, (x, c) in enumerate(zip(xs, cores)):
        d.rectangle((x + 4, 154, x + 104, 254), fill=(200, 200, 200))
        d.rectangle((x, 150, x + 100, 250), fill=c, outline=INK, width=3)
        t.texto(x + 50, 200, f"room\n{i + 1}", 17, PAPER, True, "mm")
    for i in range(8):
        a = xs[i] + 100
        b = xs[i + 1]
        corte = cores[i] != cores[i + 1]
        d.line((a, 200, b, 200), fill=RED if corte else INK, width=6 if corte else 3)
    for i in (2, 6):
        x = (xs[i] + 100 + xs[i + 1]) / 2
        d.polygon([(x, 270), (x - 12, 292), (x + 12, 292)], fill=RED)
        t.texto(x, 300, "door between\ngroups: one\nshort CD read", 15, RED, True, "mt")
    t.texto(60, 110, "All the rooms of a group sit in memory together.", 18, INK, True)
    t.caixa(60, 400, 560, 560, "Inside a group", GREEN, ["no disc access,", "the music keeps playing"])
    t.caixa(640, 400, 1140, 560, "Between groups", RED, ["a short pause, then the", "music picks up where it was"])
    t.salva("29-grupos-de-salas.png")


if __name__ == "__main__":
    linha_do_tempo()
    controle()
    musica()
    visitas()
    grupos()
