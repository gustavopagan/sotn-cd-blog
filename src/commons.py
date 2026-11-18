#!/usr/bin/env python3
"""Busca imagens no Wikimedia Commons com licença livre e gera o crédito.

  python3 src/commons.py busca "Sega Mega-CD" [--n 8]
      lista candidatos: arquivo, tamanho, licença, autor
  python3 src/commons.py baixa "File:Nome.jpg" public/img/saida.jpg [--larg 1200]
      baixa a miniatura na largura pedida e imprime a linha de crédito em Markdown

Só aceita domínio público, CC0, CC BY e CC BY-SA (qualquer versão). O resto é recusado.
"""
import html, json, re, sys, time, urllib.parse, urllib.request

API = "https://commons.wikimedia.org/w/api.php"
UA = "sotn-cd-blog/1.0 (https://sotn-cd.netlify.app; image credits for a fan devlog)"
OK = re.compile(r"^(public domain|pd\b|pd-|cc0|cc[- ]by(-sa)?( \d\.\d)?)", re.I)


def get(params):
    url = API + "?" + urllib.parse.urlencode(dict(params, format="json", formatversion=2))
    for tent in range(4):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 429 and tent < 3:
                time.sleep(10 * (tent + 1))
                continue
            raise


def limpa(t):
    t = re.sub(r"<[^>]+>", "", t or "")
    return html.unescape(re.sub(r"\s+", " ", t)).strip()


def info(titles, larg=None):
    p = {"action": "query", "titles": "|".join(titles), "prop": "imageinfo",
         "iiprop": "url|size|extmetadata"}
    if larg:
        # tamanhos-padrão de miniatura do Wikimedia (https://w.wiki/GHai); fora deles o servidor limita
        p["iiurlwidth"] = min((s for s in (500, 960, 1280, 1920) if s >= larg), default=1920)
    out = []
    for pg in get(p)["query"]["pages"]:
        if "imageinfo" not in pg:
            continue
        ii = pg["imageinfo"][0]
        md = ii.get("extmetadata", {})
        out.append({
            "title": pg["title"],
            "w": ii.get("width"), "h": ii.get("height"),
            "lic": limpa(md.get("LicenseShortName", {}).get("value")),
            "licurl": md.get("LicenseUrl", {}).get("value", ""),
            "autor": limpa(md.get("Artist", {}).get("value")) or "unknown",
            "page": ii.get("descriptionurl"),
            "orig": ii.get("thumburl") or ii.get("url"),
        })
    return out


def busca(q, n=8):
    r = get({"action": "query", "list": "search", "srsearch": q + " filetype:bitmap",
             "srnamespace": 6, "srlimit": n})
    titles = [x["title"] for x in r["query"]["search"]]
    for c in info(titles) if titles else []:
        ok = "OK " if OK.match(c["lic"]) else "-- "
        print(f'{ok}{c["title"]} | {c["w"]}x{c["h"]} | {c["lic"]} | {c["autor"][:60]}')


def baixa(title, dest, larg=1200):
    c = info([title], larg)
    if not c:
        raise SystemExit("arquivo não encontrado: " + title)
    c = c[0]
    if not OK.match(c["lic"]):
        raise SystemExit(f'licença recusada: {c["lic"]}')
    # miniatura em thumb.wikimedia.org (o original grande cai no limite de uso)
    import io
    from PIL import Image
    req = urllib.request.Request(c["orig"], headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        im = Image.open(io.BytesIO(r.read())).convert("RGB")
    im.thumbnail((larg, larg))
    im.save(dest, quality=85, optimize=True)
    lic = f'[{c["lic"]}]({c["licurl"]})' if c["licurl"] else c["lic"]
    print(f'Photo: [{c["autor"]}]({c["page"]}), {lic}, via Wikimedia Commons.')


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "busca":
        n = int(a[a.index("--n") + 1]) if "--n" in a else 8
        busca(a[1], n)
    elif a and a[0] == "baixa":
        larg = int(a[a.index("--larg") + 1]) if "--larg" in a else 1200
        baixa(a[1], a[2], larg)
    else:
        print(__doc__)
