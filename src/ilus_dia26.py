#!/usr/bin/env python3
from ilus import *
from PIL import Image
C = "00:06 00:36 00:48 00:51 00:57 00:58 00:58 01:20 01:55 02:02 02:30 02:33 02:40 02:40 02:44 02:46 02:47 02:48 02:49 02:54 03:14 03:22 03:32 03:40 03:59 04:03 21:08 21:10 21:10 21:15 21:18 21:19 21:25 21:34 21:35 21:41 21:42 21:45 21:46 22:01 22:04 22:09 22:13 22:23 22:27 22:33 22:37 22:42 22:48 22:49 22:51 22:52 22:58 23:02 23:05 23:08 23:13 23:14 23:16 23:36 23:59".split()
F = "00:24 00:28 00:40 00:43 00:51 00:54 01:02 01:05 01:11 01:16 01:19 01:26 01:26 01:28 01:30 01:30 21:05 21:07 21:07 21:13 21:16 21:39 21:46 21:58 21:59 22:20 22:30 22:42 22:57 23:00 23:04 23:13 23:24 23:26 23:57 23:58".split()
U = "/mnt/user-data/uploads/SOTN CD/"


def rodadas():
    t = Tela(1100, 640, "Six tries at a walk, 10:23 to 11:13 p.m.", "DIAGRAM")
    rows = [("10:23", "simulated frame by frame, like the original", RED),
            ("10:33", "walks the step gradually, no jump", RED),
            ("10:42", "anchored at the waist; I: \"accelerates abruptly\"", RED),
            ("10:58", "one step at a time; back = forward reversed", RED),
            ("11:05", "step start kept in the room, not on screen", RED),
            ("11:13", "approved", GREEN)]
    for i, (h, s, c) in enumerate(rows):
        y = 100 + i * 82
        t.d.rectangle((40, y, 160, y + 60), fill=c, outline=INK, width=2)
        t.texto(100, y + 30, h, 22, PAPER, True, "mm")
        t.texto(185, y + 30, s, 21, INK, False, "lm")
    t.salva("179-rodadas-caminhada.png")


def transfere():
    t = Tela(1100, 480, "From the port to the PS1", "DIAGRAM")
    t.caixa(40, 140, 360, 300, "Mega CD port", BLUE, ["room, camera,", "Alucard's position"])
    t.caixa(740, 140, 1060, 300, "PS1 original", RED, ["same room,", "same spot, same buttons"])
    t.seta(365, 220, 735, 220, rotulo="copied over\nby a script")
    t.texto(550, 380, "My idea at 12:28 a.m., so Claude wouldn't need me\nto walk Alucard to the right place.", 21, INK, False, "mm")
    t.salva("180-port-para-ps1.png")


if __name__ == "__main__":
    linha_do_tempo("175-dia26-linha-do-tempo.png", "November 12, hour by hour", C, F,
                   notas=[("01:11", "1:11 a.m.: PS1-level smoothness", "l"),
                          ("21:59", "9:59 p.m.: \"a bit stiff\"", "r")],
                   sombras=[(4.2, 20.9, "quiet until evening")])
    im = Image.open(U + "_claude/poses-inimigos/ps1-referencia-2026-11-12/blade/tira-blade-96.png").convert("RGB")
    r = im.crop((0, 9 * 190, 1184, 9 * 190 + 160))
    r.resize((r.width * 3 // 2, r.height * 3 // 2), Image.NEAREST).save(OUT + "/176-blade-ps1.png", optimize=True)
    barras("177-pulados.png", "Skipped frames per 1,000, ten Entrance rooms",
           ["port, before", "port, after", "PS1"], [17.0, 13.7, 0], [RED, YELLOW, GREEN], "",
           w=1100, h=400, selo="MEASURED", maxv=19)
    barras("178-porta.png", "Pause at the door from room 0 to room 2 (frames)",
           ["port, before", "port, after", "PS1"], [174, 125, 26], [RED, YELLOW, GREEN], "",
           w=1100, h=400, selo="MEASURED")
    rodadas(); transfere()
