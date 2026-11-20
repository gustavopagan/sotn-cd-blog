#!/usr/bin/env python3
"""Confere a grade do blog: em cada página de public/, em várias larguras de janela, todo bloco
tem de começar numa linha do quadriculado de 24 px, a grade tem de ter um número inteiro de casas
e nada pode depender do calço de emergência do navegador. Sai com erro se algo estiver fora.
Uso: python3 src/grade_test.py [largura ...]"""
import glob, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LARGURAS = [int(a) for a in sys.argv[1:] if a.isdigit()] or [320, 390, 701, 1000, 1263, 1280, 1920]
JS = """() => {
  const g = document.querySelector('.grade'), r = g.getBoundingClientRect(), s = window.sotnGrade();
  const fx = [...g.querySelectorAll('.quem, .cap .num, .secr, .w720, figure, .hdr, .badge')]
    .filter(e => { const d = (e.getBoundingClientRect().left - r.left) % 24; return d > 0.01 && d < 23.99; }).length;
  const vaza = [...g.querySelectorAll('h1.ttl, .wordmark')].filter(e => e.scrollWidth > e.clientWidth + 1).length;
  return { fora: s.fora, calcos: s.calcos, w: r.width, x: r.left, fx, vaza,
           h: document.documentElement.scrollWidth > document.documentElement.clientWidth };
}"""


def main():
    from playwright.sync_api import sync_playwright
    paginas = [os.path.join(ROOT, "public", "index.html")] + sorted(glob.glob(os.path.join(ROOT, "public", "posts", "*.html")))
    ruins = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        for w in LARGURAS:
            pg.set_viewport_size({"width": w, "height": 900})
            for f in paginas:
                pg.goto("file://" + f, wait_until="load")
                pg.evaluate("document.fonts.ready")
                o = pg.evaluate(JS)
                passo = 24 if w <= 700 else 48
                if (o["fora"] or o["calcos"] or o["fx"] or o["vaza"] or o["h"] or o["w"] % passo
                        or o["x"] != int(o["x"])):
                    ruins.append((os.path.basename(f), w, o))
        b.close()
    for r in ruins[:30]:
        print("GRADE FORA:", *r)
    print(f"grade: {len(paginas)} páginas x {len(LARGURAS)} larguras, {len(ruins)} fora")
    return 1 if ruins else 0


if __name__ == "__main__":
    sys.exit(main())
