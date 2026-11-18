#!/usr/bin/env python3
"""Ilustrações do post 8 (dia 7, 24/10)."""
from ilus import *

C = ("15:56 15:56 15:49 15:20 15:14 14:39 14:38 14:37 14:37 14:36 14:24 14:07 14:01 13:31 13:31 13:25 13:13 "
     "12:45 12:45 12:45 12:45 08:11 08:04 08:04 07:51 07:50 07:45 07:31 07:25 07:23 07:23 07:20 07:15 07:13 "
     "07:12 07:05 07:02 07:00 06:59 06:58 06:56 06:54 06:52 06:44 06:40 06:30 06:22 06:13 05:19 04:32 04:10 "
     "03:31 02:33 01:49").split()
F = ("00:10 00:28 00:31 00:37 00:41 00:42 00:45 00:49 00:53 00:54 00:55 00:57 00:58 01:04 01:05 02:26 02:30 "
     "02:33 02:38 02:41 02:55 02:56 03:00 03:01 03:02 03:06 03:11 03:34 03:35 03:38 03:40 03:41 03:46 03:48 "
     "03:50 03:53 03:55 04:00 04:16 04:17 04:18 04:19 04:24 04:48 04:55 05:52 10:59 11:11 11:15 11:30 11:32 "
     "11:54 12:29 12:30 12:32 12:33 12:35 13:43 13:44 13:54 14:00 14:04 14:08 14:09 14:13 14:22 19:49 19:52 "
     "20:13 21:05 21:38 21:48 21:55 21:59 22:01 22:28 23:09 23:10 23:20 23:22 23:25 23:51").split()


def tempo():
    linha_do_tempo("76-dia7-linha-do-tempo.png", "October 24, hour by hour", C, F,
                   notas=[("03:41", "3:41 a.m.: \"let's go pixel art\"", "l"),
                          ("05:52", "5:52 a.m.: my last message until 11", "l"),
                          ("14:22", "2:22 p.m.: merge everything", "l")])


def som():
    t = Tela(1200, 560, "Who plays what: the two music modes", "DIAGRAM")
    t.caixa(60, 110, 560, 360, "Music on the Mega Drive chip", GREEN,
            ["YM2612 + PSG: the songs, rearranged", "", "Mega CD PCM chip: free for", "every sound effect", "", "the CD is free for loading"], tam=17)
    t.caixa(640, 110, 1140, 360, "Original music, streamed", RED,
            ["Mega CD PCM chip: busy", "playing the soundtrack", "", "sound effects squeezed elsewhere", "", "a 2 s buffer to cover loading"], tam=17)
    t.texto(600, 400, "The conclusion that night: rewrite the songs for the YM2612 and keep the PCM chip for effects.\nThe stream stayed as an experiment behind a build switch.",
            16, INK, False, "mt")
    t.salva("77-som-dois-modos.png")


def soma():
    t = Tela(1200, 560, "2:36 p.m. to 2:39 p.m.: the first big merge", "DIAGRAM")
    fr = [("Pause menu", BLUE), ("2D coffin", RED), ("Black behind\nthe trees", GRAY), ("Optimization", GREEN), ("Streamed\nmusic (off)", (190, 150, 0))]
    w, gap = 190, 25
    x0 = (1200 - (5 * w + 4 * gap)) // 2
    for i, (n, c) in enumerate(fr):
        x = x0 + i * (w + gap)
        ls = n.split("\n")
        t.caixa(x, 120, x + w, 230, ls[0], c, ls[1:] or [""], tam=15)
        t.seta(x + w // 2, 236, 600, 380, GRAY, 3, cab=12)
    t.caixa(420, 390, 780, 500, "main build", INK, ["one disc with all of it"], tam=16)
    t.salva("78-soma-24-10.png")


if __name__ == "__main__":
    tempo(); som(); soma()
