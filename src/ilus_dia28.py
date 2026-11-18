#!/usr/bin/env python3
from ilus import *
from PIL import Image
U = "/mnt/user-data/uploads/SOTN CD/"
C = "00:00 00:14 00:17 00:23 00:24 00:25 00:39 01:10 01:12 01:27 01:33 01:52 01:53 03:12 03:20 03:32 03:37 03:37 14:24 15:05 15:51 15:58 16:03 16:06 16:07 16:30 16:32 16:33 16:43 17:01 17:36 17:47 17:55 18:47 19:12 19:18 19:28 19:41 19:51 19:59 20:50 21:01 21:07 21:16 21:27 21:34 22:03 22:13 22:22 22:31 22:46 23:27 23:37".split()
F = "00:13 00:16 00:21 00:36 00:45 00:45 00:47 00:53 01:11 01:18 01:20 01:32 01:34 01:48 01:55 01:56 02:13 02:18 02:20 02:23 02:25 02:40 02:41 02:42 02:46 02:49 02:55 03:07 03:11 03:12 03:14 12:30 12:32 14:14 14:23 14:55 14:59 15:00 15:02 15:03 15:46 15:46 15:48 15:58 16:20 16:24 16:26 16:31 16:36 16:37 16:38 16:40 16:43 16:46 16:48 16:52 16:58 17:29 17:31 17:33 17:39 17:42 18:00 18:03 18:31 18:41 18:45 18:46 18:47 18:49 19:01 19:04 19:12 19:17 19:20 19:31 19:39 19:50 19:52 19:59 20:35 20:35 20:40 20:41 20:49 20:52 20:53 20:55 20:56 21:14 21:33 22:01 22:08 22:18 22:19 22:20 22:58".split()


def regra():
    t = Tela(1100, 470, "My rule for removing what the port doesn't show", "DIAGRAM")
    t.caixa(40, 140, 330, 300, "invisible", GRAY, ["the PS1 computes it,", "the port doesn't draw it"])
    t.caixa(410, 140, 700, 300, "investigate", BLUE, ["what is it?", "what does the player lose?"])
    t.caixa(780, 140, 1070, 300, "pending item", GREEN, ["how to bring it back,", "adapted to the Mega CD"])
    t.seta(335, 220, 405, 220); t.seta(705, 220, 775, 220)
    t.texto(555, 380, "12:32 p.m.: nothing removed for this reason just disappears.", 21, INK, False, "mm")
    t.salva("192-regra-invisivel.png")


def adapta():
    t = Tela(1100, 600, "Effects drawn with primitives, and what I decided", "DIAGRAM")
    rows = [("Gas Cloud", "a plain square hitbox in the middle of the cloud"),
            ("Library rotating wall", "sit in the chair in front of it and it fades out with dither, like the area doors"),
            ("Falling stairs (Salem Witch)", "dust sprites we already have"),
            ("Elevator chain", "rigid. They probably used primitives to make it bend"),
            ("Library bookshelf", "switched off until we get to that area")]
    for i, (a, b) in enumerate(rows):
        y = 100 + i * 96
        t.d.rectangle((40, y, 380, y + 70), fill=BLUE, outline=INK, width=2)
        t.texto(210, y + 35, a, 19, PAPER, True, "mm")
        t.texto(400, y + 35, b, 18, INK, False, "lm")
    t.salva("193-adaptacoes.png")


def bencao():
    t = Tela(1100, 600, "The Angel's blessings, as I specified them", "DIAGRAM")
    rows = [("6:45 p.m.", "each kill holds the luck buffs, up to a ceiling of 70"),
            ("6:45 p.m.", "60 s without a kill at the same spawn point: luck resets at once"),
            ("6:47 p.m.", "scales with level: 10% of the power at Lv 1, the full value at Lv 99"),
            ("6:49 p.m.", "lasts 15 s at first, 60 s at the end"),
            ("7:01 p.m.", "one blessing at a time at Lv 1, up to three at Lv 99"),
            ("7:52 p.m.", "the INT buff drops 3 s after a spell, so at least one gets the buff"),
            ("7:59 p.m.", "subweapons: 1 in 8 chance per 5 hearts spent")]
    for i, (h, s) in enumerate(rows):
        y = 100 + i * 68
        t.d.rectangle((40, y, 170, y + 50), fill=YELLOW, outline=INK, width=2)
        t.texto(105, y + 25, h, 17, INK, True, "mm")
        t.texto(190, y + 25, s, 19, INK, False, "lm")
    t.salva("194-bencaos.png")


if __name__ == "__main__":
    linha_do_tempo("191-dia28-linha-do-tempo.png", "November 14, hour by hour", C, F,
                   notas=[("02:46", "2:46 a.m.: generating it directly doesn't work", "l"),
                          ("18:03", "6:03 p.m.: I made the ring myself", "r")])
    regra(); adapta(); bencao()
    a = [Image.open(U + "40-frentes/primitivas/fotos/NO3-%s.png" % n).convert("RGB") for n in ["220-sub1-hellfire", "380-sub1-tetra-spirit", "425-sub1-soul-steal"]]
    im = Image.new("RGB", (sum(x.width for x in a) + 24, a[0].height), (20, 20, 20)); x = 0
    for i in a:
        im.paste(i, (x, 0)); x += i.width + 12
    im.save(OUT + "/195-magias.png", optimize=True)
