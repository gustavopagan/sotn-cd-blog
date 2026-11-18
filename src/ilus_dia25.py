#!/usr/bin/env python3
from ilus import *
from PIL import Image
C = "00:11 00:11 00:17 00:20 00:21 00:22 00:24 00:25 00:55 09:44 10:06 10:14 20:36 20:38 20:48 20:55 21:01 21:32 21:35 22:41 22:42 22:46 22:46 23:42".split()
F = "00:05 00:06 00:07 00:21 00:24 08:54 09:40 09:41 11:30 11:35 20:26 20:29 20:44 21:26 21:45 21:48 22:20 22:40 22:42 22:43 22:44 22:46 22:48 22:51 23:53".split()
U = "/mnt/user-data/uploads/SOTN CD/"


def lado(paths, out, esc=2, gap=12):
    ims = [Image.open(p).convert("RGB") for p in paths]
    h = max(i.height for i in ims)
    im = Image.new("RGB", (sum(i.width for i in ims) + gap * (len(ims) - 1), h), (20, 20, 20))
    x = 0
    for i in ims:
        im.paste(i, (x, 0)); x += i.width + gap
    if esc != 1:
        im = im.resize((im.width * esc, im.height * esc), Image.NEAREST)
    im.save(OUT + "/" + out, optimize=True); print("ok", out)


def ciclo():
    t = Tela(1100, 500, "My spec for the giants, 12:21 a.m.", "DIAGRAM")
    d = t.d
    for i, (txt, c) in enumerate((("2 steps\nforward", BLUE), ("2 steps\nback", BLUE), ("repeat", GRAY))):
        x = 60 + i * 250
        t.caixa(x, 140, x + 200, 260, None, c, [])
        t.texto(x + 100, 200, txt, 22, INK, True, "mm")
        if i < 2:
            t.seta(x + 205, 200, x + 245, 200)
    t.seta(660, 265, 160, 265, GRAY, 3)
    t.caixa(820, 140, 1060, 260, "Alucard close?", RED, ["one attack"], 22)
    t.seta(765, 200, 815, 200, RED)
    t.texto(790, 120, "if", 20, RED, True, "mm")
    t.texto(60, 330, "\"That's it, no more logic.\"", 26, INK, True)
    t.texto(60, 380, "Hitbox: like a simple enemy, the skeleton.", 22, INK, False)
    t.salva("173-gigantes-ciclo.png")


def ps1():
    t = Tela(1100, 520, "The PS1 inside the tester", "DIAGRAM")
    t.caixa(40, 140, 320, 300, "me", BLUE, ["play the PS1 original", "save a state", "next to Blade"])
    t.caixa(410, 140, 690, 300, "tester", GRAY, ["loads the state", "runs without a window"])
    t.caixa(780, 140, 1060, 300, "Claude", RED, ["reads poses, timing", "and how the blades", "rotate, frame by frame"])
    t.seta(325, 220, 405, 220); t.seta(695, 220, 775, 220)
    t.texto(550, 400, "My idea at 10:42 p.m.: read the enemy from the PS1 running,\nnot only from the decompiled code.", 21, INK, False, "mm")
    t.salva("174-ps1-testador.png")


if __name__ == "__main__":
    linha_do_tempo("168-dia25-linha-do-tempo.png", "November 11, hour by hour", C, F,
                   notas=[("00:21", "12:21 a.m.: maximum economy", "l"),
                          ("21:45", "9:45 p.m.: I'll make the jingles", "r")])
    lado([U + "_claude/blog/outros/alisia/shots/f00500.png", U + "_claude/blog/outros/alisia/shots/f01300.png",
          U + "_claude/el2/sfx/ad.s3.png"], "169-alisia.png", 2)
    Image.open(U + "_claude/el2/sfx/x.png").convert("RGB").save(OUT + "/170-sound-tests.png", optimize=True)
    Image.open(U + "_claude/poses-inimigos/cmp/cmp01800.png").convert("RGB").crop((0, 0, 512, 448)).save(OUT + "/171-blade-gurkha-port.png", optimize=True)
    im = Image.open(U + "live/pontos/ponto-67/tela_marcada.png").convert("RGB")
    im.resize((512, 480), Image.NEAREST).save(OUT + "/172-rondo.png", optimize=True)
    ciclo(); ps1()
