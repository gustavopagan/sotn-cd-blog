#!/usr/bin/env python3
"""Fontes do blog, servidas pelo próprio site (nada de Google Fonts em tempo de leitura).

- Copia cada arquivo de fontes/ para public/fonts/ com um pedaço do hash no nome,
  para o cache longo do Netlify nunca servir uma versão velha.
- Gera os @font-face e os <link rel=preload> das fontes que aparecem no topo da página.
- Confere se cada texto que vai sair numa fonte existe nela (cobertura de glifos):
  letra que falta cai em outra fonte sem ninguém perceber, então o build avisa.
"""
import hashlib
import os
import shutil

from fontTools.ttLib import TTFont

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SRC = os.path.join(ROOT, "fontes")
OUT = os.path.join(ROOT, "public", "fonts")

LATIN = ("U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,"
         "U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD")
LATIN_EXT = ("U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,"
             "U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF")

# família, arquivo, estilo, peso, display, preload, unicode-range
FONTES = [
    ("CD Drive", "cd-drive.woff2", "normal", "400", "block", True, None),
    ("monoMMM5", "monommm5.woff2", "normal", "400", "block", True, None),
    ("Archivo", "archivo-latin-wdth-normal.woff2", "normal", "100 900", "swap", True, LATIN),
    ("Archivo", "archivo-latin-ext-wdth-normal.woff2", "normal", "100 900", "swap", False, LATIN_EXT),
    ("Archivo", "archivo-latin-wdth-italic.woff2", "italic", "100 900", "swap", False, LATIN),
    ("Archivo", "archivo-latin-ext-wdth-italic.woff2", "italic", "100 900", "swap", False, LATIN_EXT),
    ("Noto Sans JP", "noto-jp-titulo.woff2", "normal", "900", "block", False, None),
]


def _hash(path):
    with open(path, "rb") as f:
        return hashlib.sha1(f.read()).hexdigest()[:8]


def publica():
    """Copia as fontes com hash no nome e devolve o HTML do <head> (preloads + <style>)."""
    os.makedirs(OUT, exist_ok=True)
    nomes = {}
    for _, arq, *_ in FONTES:
        base, ext = os.path.splitext(arq)
        novo = f"{base}.{_hash(os.path.join(SRC, arq))}{ext}"
        if not os.path.exists(os.path.join(OUT, novo)):
            shutil.copyfile(os.path.join(SRC, arq), os.path.join(OUT, novo))
        nomes[arq] = novo
    # tira de public/fonts as versões antigas que não são mais usadas
    vivos = set(nomes.values()) | {"cd-drive.ttf", "cd-drive.woff2"}
    for f in os.listdir(OUT):
        if f not in vivos:
            os.remove(os.path.join(OUT, f))
    pre, faces = [], []
    for fam, arq, estilo, peso, disp, preload, faixa in FONTES:
        url = f"{{{{HOME}}}}fonts/{nomes[arq]}"
        if preload:
            pre.append(f'<link rel="preload" href="{url}" as="font" type="font/woff2" crossorigin>')
        rng = f";unicode-range:{faixa}" if faixa else ""
        wd = ";font-stretch:62% 125%" if fam == "Archivo" else ""
        faces.append(f'@font-face{{font-family:"{fam}";src:url({url}) format("woff2");font-style:{estilo};'
                     f'font-weight:{peso}{wd};font-display:{disp}{rng}}}')
    return "\n".join(pre) + "\n<style>\n" + "\n".join(faces) + "\n</style>"


_cmaps = {}


def cobertura(familia, texto):
    """Caracteres de `texto` que não existem na fonte (já em maiúsculas, como a página mostra)."""
    arq = {"CD Drive": "cd-drive.woff2", "monoMMM5": "monommm5.woff2"}[familia]
    if arq not in _cmaps:
        _cmaps[arq] = set(TTFont(os.path.join(SRC, arq)).getBestCmap())
    return sorted({c for c in texto.upper() if not c.isspace() and ord(c) not in _cmaps[arq]})
