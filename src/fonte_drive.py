#!/usr/bin/env python3
"""Fonte "CD Drive": letreiro pesado de blocos, inspirado no logotipo MEGA DRIVE.

Desenhada do zero numa grade de 10 unidades de altura: hastes verticais grossas,
barras horizontais mais finas, cantos chanfrados, diagonais retas. Só maiúsculas
(as minúsculas apontam para as mesmas formas), algarismos e a pontuação do blog.

Saída: public/fonts/cd-drive.woff2 e .ttf
"""
import os
from shapely.geometry import Polygon, box
from shapely.geometry.polygon import orient
from shapely.ops import unary_union
from shapely.affinity import scale, translate
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "public", "fonts")
U = 70          # unidades da fonte por unidade da grade (altura das maiúsculas: 700)
LADO = 0.35     # espaço de cada lado: as letras quase encostam, como no letreiro MEGA-CD
# ajuste ótico (esquerda, direita) das letras com lado em diagonal, que parecem afastadas
AJUSTE = {"M": (-0.75, 0), "W": (0, 0), "A": (-0.75, 0), "X": (-0.5, -0.5), "Y": (-0.4, -0.4),
          "V": (0, 0), "7": (0, -1.2), "/": (-1.2, -1.2), "1": (-0.4, 0), "K": (0, -0.3)}
V, H = 3.2, 2.2  # haste vertical, barra horizontal


def P(*pts):
    return Polygon(pts)


def R(x0, y0, x1, y1):
    return box(x0, y0, x1, y1)


def cham(x0, y0, x1, y1, c=1.2):
    return P((x0 + c, y0), (x1 - c, y0), (x1, y0 + c), (x1, y1 - c), (x1 - c, y1), (x0 + c, y1), (x0, y1 - c), (x0, y0 + c))


def un(*g):
    return unary_union(g)


def menos(a, *b):
    return a.difference(unary_union(b))


G = {}
# --- letras ---
G["A"] = menos(P((0, 0), (4, 10), (10, 10), (10, 0)),
               P((3.67, 0), (4.47, 2), (6.8, 2), (6.8, 0)),
               P((5.35, 4.2), (6.8, 4.2), (6.8, 7.8), (5.75 + 0.0, 7.8)))
G["B"] = menos(P((0, 0), (8, 0), (10, 1.8), (10, 3.8), (8.8, 5), (10, 6.2), (10, 8.2), (8, 10), (0, 10)),
               P((V, H), (6.6, H), (7.1, 2.7), (7.1, 3.4), (6.6, 3.9), (V, 3.9)),
               P((V, 6.1), (6.6, 6.1), (7.1, 6.6), (7.1, 7.3), (6.6, 7.8), (V, 7.8)))
O_ext = cham(0, 0, 10, 10, 1.6)
G["O"] = menos(O_ext, R(V, H, 10 - V, 10 - H))
G["C"] = menos(O_ext, R(V, H, 11, 10 - H))
G["D"] = menos(P((0, 0), (7, 0), (10, 4.2), (10, 5.8), (7, 10), (0, 10)),
               P((V, H), (5.9, H), (6.8, 4.4), (6.8, 5.6), (5.9, 10 - H), (V, 10 - H)))
G["E"] = un(R(0, 0, V, 10), R(0, 10 - H, 9.6, 10), R(0, 0, 9.6, H), P((0, 3.9), (8.2, 3.9), (7.0, 6.1), (0, 6.1)))
G["E"] = menos(G["E"], P((0, 10), (1.2, 10), (0, 8.8)))
G["F"] = menos(un(R(0, 0, V, 10), R(0, 10 - H, 9.6, 10), P((0, 3.9), (8.2, 3.9), (7.0, 6.1), (0, 6.1))),
               P((0, 10), (1.2, 10), (0, 8.8)))
G["G"] = un(G["C"], R(10 - V, 0, 10, 6.1), P((5.0, 3.9), (10, 3.9), (10, 6.1), (6.2, 6.1)))
G["G"] = menos(G["G"], R(10 - V, 6.1, 11, 10 - H))
G["H"] = un(R(0, 0, V, 10), R(10 - V, 0, 10, 10), R(0, 3.9, 10, 6.1))
G["I"] = R(0, 0, V, 10)
G["J"] = P((6.8, 10), (10, 10), (10, 1.4), (8.6, 0), (1.4, 0), (0, 1.4), (0, 3.8), (V, 3.8), (V, H), (6.8, H))
G["K"] = un(R(0, 0, V, 10), P((V, 3.9), (6.0, 3.9), (10, 10), (6.4, 10), (V, 5.4)),
            P((V, 6.1), (V, 4.6), (6.4, 0), (10, 0), (5.8, 6.1)))
G["L"] = un(R(0, 0, V, 10), R(0, 0, 9.6, H))
G["M"] = un(P((0, 0), (3.5, 0), (8.5, 10), (5, 10)), R(5, 10 - H, 15, 10),
            P((5.2, 0), (8.6, 0), (12.5, 7.8), (9.1, 7.8)), R(11.8, 0, 15, 10))
G["W"] = scale(G["M"], 1, -1, origin=(0, 5))
G["N"] = un(R(0, 0, V, 10), R(7, 0, 10.2, 10), P((0, 10), (3.7, 10), (10.2, 0), (6.5, 0)))
G["P"] = menos(P((0, 0), (V, 0), (V, 3.6), (8, 3.6), (10, 5.4), (10, 8.2), (8, 10), (0, 10)),
               P((V, 5.8), (6.6, 5.8), (7.1, 6.3), (7.1, 7.3), (6.6, 10 - H), (V, 10 - H)))
G["Q"] = un(G["O"], P((5.4, 0.6), (8.6, 0.6), (11, -1.6), (7.8, -1.6)))
G["R"] = un(G["P"], P((4.4, 3.7), (7.9, 3.7), (10.4, 0), (6.9, 0)))
G["S"] = P((1.4, 10), (10, 10), (10, 7.8), (V, 7.8), (V, 6.1), (8.6, 6.1), (10, 4.7), (10, 1.4), (8.6, 0), (0, 0),
           (0, H), (6.8, H), (6.8, 3.9), (1.4, 3.9), (0, 5.3), (0, 8.6))
G["T"] = un(R(0, 10 - H, 10, 10), R(3.4, 0, 6.6, 10))
G["U"] = P((0, 10), (V, 10), (V, H), (6.8, H), (6.8, 10), (10, 10), (10, 1.4), (8.6, 0), (1.4, 0), (0, 1.4))
G["V"] = P((0, 10), (V, 10), (V, 4.6), (5.5, 1.7), (7.8, 4.6), (7.8, 10), (11, 10), (11, 3.6), (7.6, 0), (3.4, 0), (0, 3.6))
G["X"] = un(P((0, 10), (3.7, 10), (10.4, 0), (6.7, 0)), P((6.7, 10), (10.4, 10), (3.7, 0), (0, 0)))
G["Y"] = P((0, 10), (3.5, 10), (5.2, 7.3), (6.9, 10), (10.4, 10), (6.8, 4.6), (6.8, 0), (3.6, 0), (3.6, 4.6))
G["Z"] = P((0, 10), (10, 10), (10, 7.8), (4.2, H), (10, H), (10, 0), (0, 0), (0, H), (5.8, 7.8), (0, 7.8))
# --- algarismos ---
G["0"] = menos(cham(0, 0, 9, 10, 1.6), R(V, H, 9 - V, 10 - H), P((V, H + 0.2), (V, 4.6), (9 - V, 10 - H - 0.2), (9 - V, 5.4)))
G["1"] = P((0.6, 7.8), (2.8, 10), (5.8, 10), (5.8, 0), (2.6, 0), (2.6, 7.8))
G["2"] = P((0, 10), (8.6, 10), (10, 8.6), (10, 5.3), (8.6, 3.9), (V, 3.9), (V, H), (10, H), (10, 0), (0, 0), (0, 4.7),
           (1.4, 6.1), (6.8, 6.1), (6.8, 7.8), (0, 7.8))
G["3"] = P((0, 10), (8.6, 10), (10, 8.6), (10, 1.4), (8.6, 0), (0, 0), (0, H), (6.8, H), (6.8, 3.9), (2.4, 3.9), (2.4, 6.1),
           (6.8, 6.1), (6.8, 7.8), (0, 7.8))
G["4"] = P((0, 10), (V, 10), (V, 6.1), (6.8, 6.1), (6.8, 10), (10, 10), (10, 0), (6.8, 0), (6.8, 3.9), (1.4, 3.9), (0, 5.3))
G["5"] = P((0, 10), (10, 10), (10, 7.8), (V, 7.8), (V, 6.1), (8.6, 6.1), (10, 4.7), (10, 1.4), (8.6, 0), (0, 0), (0, H),
           (6.8, H), (6.8, 3.9), (0, 3.9))
G["6"] = menos(P((1.4, 10), (10, 10), (10, 7.8), (V, 7.8), (V, 6.1), (8.6, 6.1), (10, 4.7), (10, 1.4), (8.6, 0), (1.4, 0),
                 (0, 1.4), (0, 8.6)), R(V, H, 6.8, 3.9))
G["9"] = scale(G["6"], -1, -1, origin=(5, 5))
G["7"] = P((0, 10), (10, 10), (10, 7.8), (6.0, 0), (2.5, 0), (6.4, 7.8), (0, 7.8))
G["8"] = menos(cham(0, 0, 10, 10, 1.4), R(V, H, 10 - V, 3.9), R(V, 6.1, 10 - V, 10 - H))
# --- pontuação ---
G["."] = R(0, 0, V, H)
G[","] = P((0, H), (V, H), (V, 0), (1.4, -1.8), (0.2, -1.8), (1.0, 0), (0, 0))
G[":"] = un(R(0, 0, V, H), R(0, 5.2, V, 7.4))
G[";"] = un(G[","], R(0, 5.2, V, 7.4))
G["-"] = R(0, 3.9, 6.4, 6.1)
G["·"] = R(0, 3.9, V, 6.1)
G["'"] = P((0.6, 10), (V, 10), (V, 8.6), (1.6, 6.6), (0.4, 6.6), (0.6, 8.6))
G["’"] = G["'"]
G["/"] = P((0, -0.6), (3.2, -0.6), (8.4, 10.6), (5.2, 10.6))
G["!"] = un(R(0, 3.6, V, 10), R(0, 0, V, H))
G["?"] = un(P((0, 10), (8.6, 10), (10, 8.6), (10, 5.3), (8.6, 3.9), (6.6, 3.9), (6.6, 3.4), (3.4, 3.4), (3.4, 6.1),
              (6.8, 6.1), (6.8, 7.8), (0, 7.8)), R(3.4, 0, 6.6, H))
G["("] = P((1.4, 10.8), (4.2, 10.8), (4.2, 8.8), (V, 8.8), (V, 1.2), (4.2, 1.2), (4.2, -0.8), (1.4, -0.8), (0, 0.6), (0, 9.4))
G[")"] = scale(G["("], -1, 1, origin=(2.1, 5))
G["&"] = un(menos(cham(0, 0, 10, 10, 1.4), R(V, H, 6.8, 3.9), R(V, 6.1, 6.8, 7.8), R(6.8, 6.1, 11, 10.1)),
            R(6.8, 3.9, 11.4, 6.1))
G["+"] = un(R(0, 3.9, 8, 6.1), R(2.4, 1.4, 5.6, 8.6))
G["×"] = un(P((0, 8), (2, 8), (8, 2), (6, 2)), P((6, 8), (8, 8), (2, 2), (0, 2)))
G["%"] = un(R(0, 6, 3.6, 10), R(7.4, 0, 11, 4), P((0, 0), (3.4, 0), (11, 10), (7.6, 10)))
G["#"] = un(R(2, 0, 4.2, 10), R(6.2, 0, 8.4, 10), R(0, 2.6, 10.4, 4.6), R(0, 5.6, 10.4, 7.6))
G['"'] = un(G["'"], translate(G["'"], 4.2, 0))
G["“"] = G['"']
G["”"] = G['"']
G["‘"] = G["'"]
G["→"] = un(R(0, 3.9, 8, 6.1), P((6, 1.4), (8.6, 1.4), (12, 5), (8.6, 8.6), (6, 8.6), (9.2, 5)))
G["←"] = scale(G["→"], -1, 1, origin=(6, 5))


def glifo(geo, ch=""):
    pen = TTGlyphPen(None)
    if geo is None or geo.is_empty:
        return pen.glyph(), 0, 0
    minx, _, maxx, _ = geo.bounds
    aj_e, aj_d = AJUSTE.get(ch, (0, 0))
    geo = translate(geo, LADO + aj_e - minx, 0)
    polys = [geo] if geo.geom_type == "Polygon" else list(geo.geoms)
    for p in polys:
        p = orient(p, sign=-1.0)  # contorno externo no sentido horário (TrueType)
        for anel in [p.exterior] + list(p.interiors):
            pts = list(anel.coords)[:-1]
            pen.moveTo((round(pts[0][0] * U), round(pts[0][1] * U)))
            for x, y in pts[1:]:
                pen.lineTo((round(x * U), round(y * U)))
            pen.closePath()
    larg = round((maxx - minx + 2 * LADO + aj_e + aj_d) * U)
    return pen.glyph(), larg, round((LADO + aj_e) * U)


def nome(ch):
    return "uni%04X" % ord(ch)


def monta():
    os.makedirs(OUT, exist_ok=True)
    ordem = [".notdef", "space"] + [nome(c) for c in G]
    fb = FontBuilder(1000, isTTF=True)
    fb.setupGlyphOrder(ordem)
    cmap = {32: "space", 0xA0: "space"}
    glyphs, metrics = {}, {}
    vazio = TTGlyphPen(None).glyph()
    glyphs[".notdef"], metrics[".notdef"] = vazio, (500, 0)
    glyphs["space"], metrics["space"] = vazio, (int(3.4 * U), 0)
    for ch, geo in G.items():
        g, w, lsb = glifo(geo, ch)
        glyphs[nome(ch)] = g
        metrics[nome(ch)] = (w, lsb)
        cmap[ord(ch)] = nome(ch)
        if ch.isalpha() and ch.lower() != ch:
            cmap[ord(ch.lower())] = nome(ch)
    fb.setupGlyf(glyphs)
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=820, descent=-180)
    fb.setupCharacterMap(cmap)
    fb.setupNameTable({"familyName": "CD Drive", "styleName": "Regular", "uniqueFontIdentifier": "CD Drive 1.0",
                       "fullName": "CD Drive", "psName": "CDDrive-Regular", "version": "1.0",
                       "copyright": "Original lettering for the SOTN Mega CD devlog"})
    fb.setupOS2(sTypoAscender=820, sTypoDescender=-180, usWinAscent=820, usWinDescent=180, sCapHeight=700, sxHeight=700,
                achVendID="SOTN")
    fb.setupPost()
    fb.save(os.path.join(OUT, "cd-drive.ttf"))
    fb.font.flavor = "woff2"
    fb.save(os.path.join(OUT, "cd-drive.woff2"))
    print("ok", len(G), "glifos")


if __name__ == "__main__":
    monta()
