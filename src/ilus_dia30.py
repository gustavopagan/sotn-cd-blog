#!/usr/bin/env python3
from ilus import *
from PIL import Image
import shutil
U = "/mnt/user-data/uploads/SOTN CD/"
F = "00:04 00:08 00:15 00:19 00:20 00:22 00:23 00:47 00:57 01:12 01:18 01:23 01:24 01:25 01:27 01:30 01:31 01:34 02:06 09:30 10:52 10:52 11:25 11:26 11:26 11:30 11:34 11:47 11:50 11:55 12:30 12:33 12:36 12:37 12:38 12:41 12:45 13:05 13:07 13:25 13:39 13:39 13:39 13:50 13:50 13:51 13:53 13:54 13:57 14:04 14:05 15:23 15:24 15:31 15:31 15:32 15:34 15:35 15:36 15:40 15:41 15:51 15:56 16:01 16:10 16:11 16:15 16:17 16:19 16:20 16:22 16:37 16:42 16:44 16:45 16:47 16:48 16:51 16:56 17:04 17:05 17:14 17:15 17:26 17:28 17:29 17:31 17:31 17:33 17:34 17:36 17:37 17:39 17:46 17:47 17:47 18:27 18:30 18:30 18:34 18:38 18:40 18:44 18:46 18:47 19:53 19:56 20:53 20:53 20:55 20:58 21:02 21:08 21:09 21:09 21:11 21:13 21:16 21:18 21:19 21:20 21:24 21:26 21:30 21:32 21:36 22:34 22:34 22:36 22:37 22:44 22:47 23:07 23:15 23:17 23:23 23:25 23:25 23:27 23:30 23:30 23:31 23:32 23:33 23:34 23:39 23:45 23:50 23:53".split()


def asm():
    t = Tela(1100, 520, "Assembly by default", "DIAGRAM")
    t.caixa(40, 120, 340, 300, "the scarce thing", RED, ["code memory:", "every module window", "lives on a few", "hundred spare bytes"])
    t.caixa(400, 120, 700, 300, "the answer", BLUE, ["rewrite everything", "that saves bytes,", "not just the", "measured bottleneck"])
    t.caixa(760, 120, 1060, 300, "cold code", GREEN, ["Claude's reservation.", "Mine: put it behind", "a switch, and I test it"])
    t.seta(345, 210, 395, 210); t.seta(705, 210, 755, 210)
    t.texto(550, 380, "12:41 p.m.: write it into every doc, so the next chats\ndon't slide into avoiding the rewrite.", 21, INK, False, "mm")
    t.salva("202-assembly.png")


def ophan():
    im = Image.open(U + "40-frentes/familiar-ophan/medidas/c6_tira.png").convert("RGB")
    cw = 258
    crops = [im.crop((i * cw + 30, 70, i * cw + 130, 170)) for i in range(5)]
    out = Image.new("RGB", (100 * 5 + 40, 100), (20, 20, 20))
    for i, c in enumerate(crops):
        out.paste(c, (i * 110, 0))
    out.resize((out.width * 3, out.height * 3), Image.NEAREST).save(OUT + "/207-ophan-jogo.png", optimize=True)


if __name__ == "__main__":
    C = open("/tmp/c30.txt").read().split()
    linha_do_tempo("201-dia30-linha-do-tempo.png", "November 16, hour by hour", C, F,
                   notas=[("01:27", "1:27 a.m.: \"it's happening again\"", "l"),
                          ("11:55", "11:55 a.m.: rewrite EVERYTHING?", "r")])
    asm(); ophan()
    Image.open(U + "10-insumos/menu_art/mockup/submenus/sub_familiars c_previa.png").convert("RGB").save(OUT + "/203-familiares-tela.png", optimize=True)
    Image.open(U + "10-insumos/menu_art/botoes/botoes_glifos_previa.png").convert("RGB").save(OUT + "/204-glifos.png", optimize=True)
    shutil.copy(U + "50-previas/indicadores_estados_ruins.gif", OUT + "/205-estados.gif")
    Image.open(U + "50-previas/indicadores_vapor_quadro.png").convert("RGB").save(OUT + "/206-vapor.png", optimize=True)
    print("ok")
