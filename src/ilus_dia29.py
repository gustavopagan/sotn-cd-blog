#!/usr/bin/env python3
from ilus import *
from PIL import Image, ImageDraw, ImageFont
M = "/mnt/user-data/uploads/SOTN CD/10-insumos/menu_art/"
C = "00:01 00:16 00:18 00:26 00:43 00:47 00:51 00:53 00:54 00:55 00:57 01:23 01:24 07:27 07:35 07:36 07:49 07:53 08:03 08:09 08:14 08:34 09:00 09:07 11:02 11:03 11:09 11:10 11:13 11:18 11:20 11:31 11:36 11:37 11:42 11:42 11:44 11:47 11:48 13:16 13:17 13:17 13:18 13:19 13:19 13:20 13:29 13:29 13:31 14:17 14:19 14:21 14:22 14:53 14:55 14:59 15:23 15:23 15:24 15:25 15:25 15:34 15:39 15:41 15:53 16:19 18:08 18:12 18:40 19:04 19:21 19:27 19:31 19:47 19:50 19:51 20:01 20:03 20:10 20:10 20:13 20:13 20:14 20:14 20:40 20:59 21:04 21:05 21:05 21:08 21:08 21:25 21:33 21:33 21:33 22:50 23:55 23:58".split()
F = "00:01 00:12 00:15 00:18 00:23 00:24 07:25 07:32 08:02 08:04 08:05 08:09 10:58 11:15 11:17 11:19 13:16 13:16 14:21 14:50 15:21 15:33 15:34 15:35 15:36 15:41 15:42 15:44 15:48 15:50 15:53 16:03 16:19 17:27 17:28 17:35 17:43 17:44 17:46 17:52 18:04 18:06 18:14 18:15 18:19 18:21 18:23 18:24 18:25 18:34 18:35 19:03 19:20 19:22 19:25 19:26 19:29 19:45 20:07 20:07 20:08 20:12 20:23 20:30 21:02 21:04 21:06 22:39 22:43 22:48 22:51 22:53 22:55 22:59 23:00 23:02 23:03 23:04 23:10 23:34 23:51 23:51 23:53 23:56".split()


def menus():
    a = [Image.open(M + f).convert("RGB") for f in ["mockup/menu_principal_previa.png", "mockup/submenus/sub_equip.png", "mockup/submenus/sub_equip b2.png"]]
    im = Image.new("RGB", (256 * 3 + 24, 224), (20, 20, 20))
    for i, x in enumerate(a):
        im.paste(x, (i * 268, 0))
    im.resize((im.width * 2, 448), Image.NEAREST).save(OUT + "/197-menus-mockup.png", optimize=True)


def fundos():
    a = Image.open(M + "fundo/fundo_bayer4_sombra_previa_3x.png").convert("RGB").crop((0, 0, 384, 336))
    b = Image.open(M + "fundo/fundo_sombra_dither_leve_previa_3x.png").convert("RGB").crop((0, 0, 384, 336))
    im = Image.new("RGB", (384 * 2 + 12, 336), (20, 20, 20)); im.paste(a, (0, 0)); im.paste(b, (396, 0))
    im.save(OUT + "/198-fundos-dither.png", optimize=True)


def fontes():
    txt = "Change your equipment."
    rows = []
    for f in ["SOTN_Original_MCD.ttf", "SOTN_Reduzida_MCD.ttf"]:
        ft = ImageFont.truetype(M + "fonte/" + f, 8)
        im = Image.new("RGB", (124, 12), (20, 24, 80)); d = ImageDraw.Draw(im); d.fontmode = "1"
        d.text((2, 2), txt, font=ft, fill=(255, 255, 255)); rows.append(im)
    out = Image.new("RGB", (124, 26), (0, 0, 0))
    for i, r in enumerate(rows):
        out.paste(r, (0, i * 14))
    out.resize((out.width * 7, out.height * 7), Image.NEAREST).save(OUT + "/199-fontes.png", optimize=True)


def latencia():
    t = Tela(1100, 460, "What bothered me in the old menu", "DIAGRAM")
    t.caixa(40, 140, 330, 290, "press", BLUE, ["a direction", "on the pad"])
    t.caixa(410, 140, 700, 290, "wait", RED, ["the cursor lags,", "the screen updates", "in a frozen way"])
    t.caixa(780, 140, 1070, 290, "see it", BLUE, ["the item", "changes"])
    t.seta(335, 215, 405, 215); t.seta(705, 215, 775, 215)
    t.texto(555, 370, "7:25 a.m.: the slow entry into Equip is tolerable. This part is not.", 20, INK, False, "mm")
    t.salva("200-latencia-menu.png")


if __name__ == "__main__":
    linha_do_tempo("196-dia29-linha-do-tempo.png", "November 15, hour by hour", C, F,
                   notas=[("07:25", "7:25 a.m.: \"unacceptable\"", "l"),
                          ("18:04", "6:04 p.m.: my font edits", "r")])
    menus(); fundos(); fontes(); latencia()
