#!/usr/bin/env python3
from ilus import *
from PIL import Image
U = "/mnt/user-data/uploads/SOTN CD/"
C = []
F = "00:00 00:02 00:10 01:11 01:19 01:20 01:26 01:27 01:30 01:37 01:42 01:44 01:47 08:24 08:24 08:38 08:53 08:58 09:03 09:03 09:04 11:11 11:12 11:14 12:57 12:58 13:05 14:28 14:29 14:42 16:31 16:33 16:38 16:39 16:41 16:41 16:42 16:44 16:59 17:09 17:14 17:15 17:17 17:20 17:23 17:24 17:26 17:30 17:47 17:48 17:50 21:56 21:57 22:02 22:27 22:48 23:38 23:41 23:41".split()


def pico():
    rows = []
    for ln in open(U + "live/comentarios/pico-de-subprincipal/metricas.csv", encoding="utf-8").read().splitlines()[1:]:
        p = ln.split(";")
        q = int(p[0])
        if 2900 <= q <= 3060:
            rows.append((q, float(p[1]), float(p[2])))
    t = Tela(1100, 520, "The spike I asked about, frame by frame", "MEASURED")
    d = t.d
    x0, x1, y0, y1 = 110, 1060, 110, 440
    q0, q1 = rows[0][0], rows[-1][0]
    X = lambda q: x0 + (x1 - x0) * (q - q0) / (q1 - q0)
    Y = lambda v: y1 - (y1 - y0) * min(v, 200) / 200
    for v in (0, 50, 100, 150, 200):
        d.line((x0, Y(v), x1, Y(v)), fill=LIGHT if v != 100 else RED, width=1 if v != 100 else 3)
        t.texto(x0 - 10, Y(v), f"{v}%", 16, INK, False, "rm")
    for idx, cor in ((1, BLUE), (2, GREEN)):
        pts = [(X(r[0]), Y(r[idx])) for r in rows]
        d.line(pts, fill=cor, width=3)
    t.texto(x0 + 10, y0 - 40, "logic (sub)", 18, BLUE, True)
    t.texto(x0 + 170, y0 - 40, "drawing (main)", 18, GREEN, True)
    t.texto(X(2975) + 150, Y(185), "a Bloody Zombie dies", 18, INK, True, "mm")
    t.texto(x0, 470, f"frames {q0} to {q1} of my recording. Above the red line the frame doesn't fit and the game slows down.", 16, GRAY)
    t.salva("183-pico.png")


def caminho():
    t = Tela(1100, 480, "Two ways to finish the game", "DIAGRAM")
    t.caixa(40, 130, 520, 330, "1. build everything first", BLUE,
            ["familiars, spells, weapons,", "shields, item effects,", "then optimize"])
    t.caixa(580, 130, 1060, 330, "2. make room first", GREEN,
            ["free memory and time now,", "then add the rest", "inside the budget"])
    t.texto(550, 400, "My question at 8:53 a.m. The heavy ones on my mind:\nShield Rod, Moon Rod, Heart Refresh, Power of Sire, the Sword familiar.", 19, INK, False, "mm")
    t.salva("184-dois-caminhos.png")


if __name__ == "__main__":
    pico(); caminho()
    Image.open(U + "_claude/capas-mascara/out/gola.png").convert("RGB").save(OUT + "/181-gola.png", optimize=True)
    Image.open(U + "_claude/capas-mascara/out/ls100.png").convert("RGB").save(OUT + "/182-ls100.png", optimize=True)
    a = Image.open(U + "_claude/orcamento-ce-ps1/telas_agua/z18-f02250.png").convert("RGB")
    b = Image.open(U + "_claude/orcamento-ce-ps1/telas_agua/z18s-f02250.png").convert("RGB")
    im = Image.new("RGB", (1036, 448), (20, 20, 20)); im.paste(a, (0, 0)); im.paste(b, (524, 0))
    im.save(OUT + "/185-agua-silhueta.png", optimize=True)
    print("ok")


def storyboard():
    t = Tela(1100, 470, "That afternoon's shot list, redrawn", "MOCKUP")
    shots = [("4:31 p.m.", "close-up: his mouth", "\"I was brought here by\nhumans who wish to\npay me tribute\""),
             ("4:59 p.m.", "Dracula", "\"Perhaps...\""),
             ("5:09 p.m.", "knees down", "he rises; the goblet\nfalls, breaks, wine\nspreads like blood")]
    for i, (h, a, b) in enumerate(shots):
        x = 40 + i * 350
        t.d.rectangle((x, 110, x + 320, 330), fill=(40, 40, 46), outline=INK, width=3)
        t.texto(x + 160, 220, b, 18, PAPER, False, "mm")
        t.texto(x, 345, h, 18, RED, True)
        t.texto(x, 375, a, 18, INK, True)
    t.texto(40, 425, "Generated video for the prologue. No frames from it here.", 16, GRAY)
    t.salva("186-storyboard.png")


storyboard()
