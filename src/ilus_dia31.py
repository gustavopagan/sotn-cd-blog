#!/usr/bin/env python3
from ilus import *
from PIL import Image
U = "/mnt/user-data/uploads/SOTN CD/_claude/menu-nativo/"
C = "00:20 00:31 00:36 00:41 00:44 00:46 01:00 01:05 01:07 01:16 01:17 01:37 01:42 01:50 01:51 01:52 01:55 02:29 02:29 02:41 03:30 03:44 03:47 04:25 08:08 08:15 08:16 08:17 08:40 09:04 09:04 09:25 09:25 10:08 11:19 11:48 11:53 11:56 12:00 12:01 12:01 12:12 12:37 12:41 12:45 12:49 13:01 13:02 13:02 13:45 13:57 13:58 14:01 14:20 14:35 15:00 15:13 15:25 15:28 16:00 16:38 16:49 17:08 17:40 17:59 19:18 19:19 20:35 21:15 22:52 23:11 23:11".split()
F = "11:31 11:32 11:34 11:40 12:12 12:26 12:32 13:00 13:01 13:25 13:29 13:30 13:59 14:40 14:48 14:51".split()

if __name__ == "__main__":
    linha_do_tempo("208-dia31-linha-do-tempo.png", "November 17, hour by hour", C, F,
                   notas=[("11:32", "11:32 a.m.: \"too little of the menu came over\"", "r"),
                          ("13:25", "1:25 p.m.: stop building FM", "l")],
                   sombras=[(0, 8.0, "assembly rewrite, overnight")])
    barras("209-bytes-sub.png", "Free bytes in the logic program, whole castle",
           ["before the night", "that morning", "after the merges", "that evening"],
           [1828, 6516, 5420, 11212], [RED, GREEN, YELLOW, GREEN], "",
           w=1100, h=440, selo="MEASURED", linha=2048, linha_rot="project goal 2,048")
    barras("210-bytes-ipx.png", "Free bytes in the drawing program, whole castle",
           ["before", "after"], [1624, 2328], [RED, GREEN], "", w=1100, h=340, selo="MEASURED",
           linha=2048, linha_rot="goal 2,048", maxv=2600)
    a = Image.open(U + "shots_f/f02750.png").convert("RGB"); b = Image.open(U + "shots_t/f03060.png").convert("RGB")
    im = Image.new("RGB", (1040, 448), (20, 20, 20)); im.paste(a, (0, 0)); im.paste(b, (528, 0))
    im.save(OUT + "/211-menu-nativo.png", optimize=True)
    Image.open(U + "elementos/elementos_opcoes.png").convert("RGB").save(OUT + "/212-elementos.png", optimize=True)
