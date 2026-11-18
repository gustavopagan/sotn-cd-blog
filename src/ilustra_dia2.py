#!/usr/bin/env python3
"""Ilustrações do post 3 (dia 2), desenhadas do zero: nenhuma arte do jogo.

  public/img/21-sprites-por-linha.png  limite de 16 sprites por linha
  public/img/22-musica-em-minutos.png  a conta da música
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "public", "img")
RED, GREEN, YELLOW, BLUE = (200, 38, 44), (21, 146, 74), (244, 196, 0), (4, 100, 182)
INK, PAPER = (17, 17, 17), (255, 255, 255)


def fonte(px):
    for f in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"):
        if os.path.exists(f):
            return ImageFont.truetype(f, px)
    return ImageFont.load_default()


# silhueta genérica de zumbi (16 x 32), 1 = corpo, 2 = olho; desenho próprio
ZUMBI = [
    "....1111........", "...111111.......", "...112121.......", "...111111.......",
    "....1111........", ".....11.........", "...111111.......", "..11111111......",
    ".111111111111...", "111.11111..1111.", "11..11111....11.", "....11111.......",
    "....11111.......", "....11111.......", "....111111......", "....11.111......",
    "....11..11......", "...111..11......", "...11...11......", "...11...111.....",
    "..111...111.....", "..11.....11.....", "..11.....11.....", ".111.....111....",
    ".11.......11....", ".11.......11....", "111.......111...", "11.........11...",
    "11.........11...", "111........111..", "................", "................",
]
# silhueta genérica de vampiro de capa (16 x 32); desenho próprio
VAMP = [
    "......111.......", ".....11111......", ".....12121......", ".....11111......",
    "......111.......", "....3311133.....", "...333111333....", "..33331113333...",
    "..33311111333...", ".333.11111.333..", ".333.11111.333..", ".333.11111.3333.",
    ".333.11111.3333.", "3333.11111.33333", "3333.11.11.33333", "3333.11.11.33333",
    "3333.11.11.33333", "333..11.11..3333", "333..11.11..3333", "333..11.11..333.",
    "33...11.11...33.", "33...11.11...33.", "3....11.11....3.", ".....11.11......",
    ".....11.11......", "....111.111.....", "....11...11.....", "....11...11.....",
    "...111...111....", "...11.....11....", "................", "................",
]


def boneco(d, x, y, mapa, cores, fantasma=False):
    for j, linha in enumerate(mapa):
        for i, c in enumerate(linha):
            if c == ".":
                continue
            if fantasma:
                if (i + j) % 2 == 0:
                    d.point((x + i, y + j), fill=(150, 150, 150))
            else:
                d.point((x + i, y + j), fill=cores[c])


def sprites_por_linha():
    W, H = 256, 224
    tela = Image.new("RGB", (W, H), (34, 30, 52))
    d = ImageDraw.Draw(tela)
    # parede e chão genéricos
    for x in range(0, W, 32):
        d.rectangle((x, 40, x + 29, 150), fill=(52, 46, 74))
    d.rectangle((0, 182, W, H), fill=(70, 60, 50))
    for x in range(0, W, 16):
        d.line((x, 182, x, H), fill=(58, 50, 42))
    zc = {"1": (110, 140, 100), "2": RED}
    vc = {"1": (220, 220, 230), "2": RED, "3": (150, 20, 30)}
    y = 150
    boneco(d, 18, y, VAMP, vc)
    xs = [44, 70, 96, 122, 148, 174, 200, 226]
    for k, x in enumerate(xs):
        boneco(d, x, y, ZUMBI, zc, fantasma=(k >= 6))
    # a linha medida
    ly = 168
    d.line((0, ly, W, ly), fill=YELLOW)
    img = tela.resize((W * 3, H * 3), Image.NEAREST)
    out = img
    d2 = ImageDraw.Draw(out)
    d2.text((W * 3 - 200, 12), "ILLUSTRATION", font=fonte(20), fill=(170, 170, 190))
    out.save(os.path.join(OUT, "21-sprites-por-linha.png"), optimize=True)


def musica():
    W, H = 768, 330
    im = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(im)
    f, fb = fonte(20), fonte(24)
    d.text((24, 18), "The music math (minutes of CD audio)", font=fb, fill=INK)
    barras = [("All songs, intro + loop", 114, RED),
              ("Room for music on the disc", 75, GREEN),
              ("Loops only", 50, BLUE)]
    esc = 5.2
    for k, (nome, v, cor) in enumerate(barras):
        y = 80 + k * 76
        d.text((24, y), nome, font=f, fill=INK)
        d.rectangle((24, y + 28, 24 + v * esc, y + 58), fill=cor, outline=INK, width=3)
        d.text((34 + v * esc, y + 30), f"~{v}", font=fb, fill=INK)
    x75 = 24 + 75 * esc
    for yy in range(70, 300, 10):
        d.line((x75, yy, x75, yy + 5), fill=INK, width=2)
    im.save(os.path.join(OUT, "22-musica-em-minutos.png"), optimize=True)


if __name__ == "__main__":
    sprites_por_linha()
    musica()
    print("ok")
