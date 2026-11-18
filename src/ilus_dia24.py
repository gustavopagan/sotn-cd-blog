#!/usr/bin/env python3
from ilus import *
from PIL import Image
C = "05:31 10:08 10:37 10:40 10:42 10:48 10:49 10:49 10:50 11:29 11:29 11:29 11:30 11:30 11:31 11:41 11:49 11:57 12:06 12:27 12:35 13:54 14:12 14:12 14:22 14:25 14:25 14:25 14:25 14:25 14:25 14:26 14:27 14:31 14:48 14:49 15:13 15:20 15:22 15:32 16:01 16:02 16:03 16:03 16:04 16:04 16:06 16:06 16:08 16:11 16:17 16:21 16:31 16:34 16:34 16:35 16:39 16:41 16:41 16:42 16:43 16:47 16:48 16:49 16:49 16:49 16:50 16:50 16:50 17:19 17:20 17:27 17:28 17:29 17:39 17:53 18:16 18:42 18:43".split()
F = "09:35 10:03 10:04 10:07 10:07 10:07 10:07 10:08 10:08 10:33 10:35 10:39 10:41 10:41 10:44 10:46 11:29 11:29 11:29 11:29 11:29 11:29 11:29 11:29 11:30 11:34 11:38 11:41 11:43 11:46 11:47 11:47 11:47 11:47 11:47 11:47 11:49 11:49 11:49 13:30 13:52 14:01 14:03 14:04 14:24 14:24 14:24 14:24 14:24 14:24 14:24 14:24 14:25 15:36 15:40 15:53 15:56 15:58 15:59 16:01 16:01 16:01 16:01 16:01 16:01 16:01 16:02 16:04 16:07 16:08 16:09 16:32 16:33 16:33 16:33 16:35 16:35 16:39 16:40 16:40 16:47 16:47 16:48 16:55 16:58 17:03 17:05 17:08 17:08 17:09 17:12 17:13 17:14 17:14 17:15 17:17 17:18 17:19 17:23 17:25 17:30 17:31 17:33 17:40 17:41 17:47 17:48 17:52 18:21 18:22 18:23 18:25 18:25 18:26 18:27 18:29 20:12 20:12 20:13 20:13 20:30".split()
PREV = "/mnt/user-data/uploads/SOTN CD/50-previas/"


def sala():
    barras("162-sala-de-teste.png", "Starting a test disc in another room",
           ["before: rebuild, worst", "before: rebuild, best", "after: edit the disc"],
           [540, 240, 1], [RED, RED, GREEN], " s", w=1100, h=420, selo="MEASURED",
           notas=["", "", "under a second"])


def disco():
    t = Tela(1100, 560, "Where my C: drive went", "MEASURED")
    d = t.d
    x0 = 300
    esc = 640 / 930
    linhas = [("C: drive (930 GB)", [(846, RED, "used 846"), (84, GREEN, "free 84")]),
              ("WSL disk file", [(408, RED, "408 GB on disk")]),
              ("what was in it", [(60, BLUE, "60 GB exported")]),
              ("C: after", [(442, RED, "used 442"), (488, GREEN, "free 488")])]
    for i, (rot, partes) in enumerate(linhas):
        y = 120 + i * 100
        t.texto(x0 - 16, y + 25, rot, 18, INK, True, "rm")
        x = x0
        for v, c, s in partes:
            w = v * esc
            d.rectangle((x, y, x + w, y + 50), fill=c, outline=INK, width=2)
            t.texto(x + w / 2 if w > 110 else x + w + 8, y + 25, s, 16, PAPER if w > 110 else INK, True, "mm" if w > 110 else "lm")
            x += w
    t.texto(550, 520, "The WSL disk file grows but never shrinks by itself.", 18, INK, False, "mm")
    t.salva("163-disco-c.png")


def fila():
    t = Tela(1100, 520, "A window on the build queue", "MOCKUP")
    d = t.d
    cab = ["request", "task", "state", "progress"]
    xs = [40, 220, 480, 660]
    for x, c in zip(xs, cab):
        t.texto(x, 90, c, 18, INK, True)
    rows = [("1110-a", "sub-nativo", "building", 0.62), ("1110-b", "cores-ce2", "building", 0.25),
            ("1110-c", "poses-inimigos", "waiting", 0), ("1110-d", "limites", "waiting", 0),
            ("1110-e", "menus-som", "done", 1), ("1110-f", "orcamento-no3", "done", 1)]
    for i, (a, b, c, p) in enumerate(rows):
        y = 140 + i * 56
        if i % 2 == 0:
            d.rectangle((30, y - 10, 1070, y + 36), fill=LIGHT)
        t.texto(xs[0], y, a, 17, INK, False, mono=True)
        t.texto(xs[1], y, b, 17)
        t.texto(xs[2], y, c, 17, GREEN if c == "done" else (BLUE if c == "building" else GRAY), True)
        d.rectangle((xs[3], y, xs[3] + 360, y + 22), outline=INK, width=2)
        if p:
            d.rectangle((xs[3] + 2, y + 2, xs[3] + 2 + 356 * p, y + 20), fill=GREEN if p == 1 else BLUE)
    t.texto(550, 488, "Illustration. The real page refreshes every 3 s; progress is elapsed time against similar past builds.", 15, GRAY, False, "mm")
    t.salva("165-fila.png")


def gigantes():
    t = Tela(1100, 520, "Why not one giant at a time", "DIAGRAM")
    d = t.d
    d.rectangle((40, 400, 1060, 430), fill=GRAY)
    for x, n, c in ((360, "Blade", (190, 110, 40)), (780, "Gurkha", (60, 120, 60))):
        d.rectangle((x - 40, 250, x + 40, 400), fill=c, outline=INK, width=3)
        t.texto(x, 325, n, 18, PAPER, True, "mm")
    d.ellipse((90, 330, 150, 400), fill=RED, outline=INK, width=3)
    t.texto(120, 310, "Alucard", 16, INK, True, "mm")
    pts = [(150, 330), (300, 180), (450, 170), (620, 200), (780, 240)]
    for a, b in zip(pts, pts[1:]):
        d.line((a, b), fill=BLUE, width=5)
    t.seta(620, 200, 760, 240, BLUE, 5)
    t.texto(420, 130, "bat, mist or double jump", 18, BLUE, True, "mm")
    t.texto(550, 470, "Fly over the first giant and you are where the second one should be.", 18, INK, False, "mm")
    t.salva("166-dois-gigantes.png")


def falas():
    t = Tela(1100, 460, "One dialogue, one track", "DIAGRAM")
    d = t.d
    t.texto(40, 100, "PS1: each line is its own file, loaded on its turn", 18, INK, True)
    x = 40
    for i, w in enumerate([180, 120, 220, 150]):
        d.rectangle((x, 140, x + w, 190), fill=BLUE, outline=INK, width=2)
        t.texto(x + w / 2, 165, f"line {i+1}", 16, PAPER, True, "mm")
        x += w + 40
        if i < 3:
            t.texto(x - 20, 165, "load", 13, GRAY, False, "mm")
    t.texto(40, 250, "Mega CD: the whole dialogue as one CD audio track", 18, INK, True)
    x = 40
    d.rectangle((40, 290, 40 + 790, 340), fill=PAPER, outline=INK, width=2)
    for i, w in enumerate([180, 120, 220, 150]):
        d.rectangle((x, 290, x + w, 340), fill=GREEN, outline=INK, width=2)
        t.texto(x + w / 2, 315, f"line {i+1}", 16, PAPER, True, "mm")
        x += w + 40
    t.texto(40, 370, "The gaps stay in as silence, if the original timing counted on them.", 17, INK, False)
    t.salva("167-falas.png")


def gurkha():
    im = Image.open(PREV + "gigantes/folha_gurkha.png").convert("RGB").crop((0, 0, 1536, 512))
    im = im
    im.save(OUT + "/164-gurkha-poses.png", optimize=True)
    print("ok gurkha")


if __name__ == "__main__":
    print(len(C), len(F))
    linha_do_tempo("161-dia24-linha-do-tempo.png", "November 10, hour by hour", C, F,
                   notas=[("11:38", "11:38 a.m.: how did they test in 1997?", "r"),
                          ("16:55", "4:55 p.m.: my C: drive is filling up", "l")],
                   sombras=[(0, 9.5, "queue down overnight")])
    sala(); disco(); fila(); gigantes(); falas(); gurkha()
