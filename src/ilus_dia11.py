#!/usr/bin/env python3
"""Ilustrações do post 12 (dia 11, 28/10)."""
from ilus import *


def pastas():
    t = Tela(900, 700, "The project folder, before and after the cleanup", "MOCKUP")
    antes = ["build_noite", "build save", "teste save 3d", "build final", "build_compressao", "fm", "docs\\ref",
             "_xfer\\audio_noite", "sotn-megacd", "..."]
    depois = ["00-disco", "10-insumos", "20-toolchain", "30-principal", "40-frentes", "50-previas", "60-audio",
              "70-docs-ref", "sotn-megacd"]
    d = t.d
    for col, (tit, itens, cor) in enumerate((("before", antes, GRAY), ("after (today)", depois, GREEN))):
        x = 50 + col * 430
        d.rectangle((x, 100, x + 380, 620), fill=PAPER, outline=INK, width=3)
        d.rectangle((x, 100, x + 380, 146), fill=cor, outline=INK, width=3)
        t.texto(x + 190, 123, tit, 22, PAPER, True, "mm")
        for i, n in enumerate(itens):
            y = 166 + i * 40
            d.rectangle((x + 20, y + 4, x + 46, y + 24), fill=YELLOW, outline=INK)
            t.texto(x + 60, y, n, 22, INK, False, mono=True)
    t.texto(450, 640, "Left: names from the chat history. Right: the top level today. The numbers set the reading order.", 18, INK, False, "mt")
    t.salva("101-pastas.png")


def tempo():
    C = "03:43 04:39 04:45 06:27".split()
    F = "00:34 01:14 01:26 01:32 01:34 01:37 01:39 01:41 02:54 09:49 17:47 17:49 17:53 19:16".split()
    linha_do_tempo("102-dia11-linha-do-tempo.png", "October 28, hour by hour", C, F,
                   notas=[("01:41", "1:41 a.m.: code first, then the name", "l"),
                          ("09:49", "9:49 a.m.: the mermen are still slow", "l")])


if __name__ == "__main__":
    pastas(); tempo()
