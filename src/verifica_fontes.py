#!/usr/bin/env python3
"""Abre as páginas geradas num Chrome sem tela, servidas por HTTP como no Netlify, e confere se
cada fonte do blog baixa, é válida e cobre o texto que vai mostrar. Sai com erro se alguma falhar.

  python3 src/verifica_fontes.py            (depois do build)
"""
import functools, http.server, json, os, re, socketserver, subprocess, sys, tempfile, threading

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PUB = os.path.join(ROOT, "public")
TESTES = [("CD Drive", "SYMPHONY OF THE NIGHT 0123456789?:'"), ("monoMMM5", "DAY 23 · NOVEMBER 9, 2026"),
          ("Archivo", "Body text, ação, ünïcödé"), ("Noto Sans JP", "メガCD移植・開発日誌")]
JS = """<script>(async()=>{const r={};for(const [f,t] of %s){try{const l=await document.fonts.load('900 24px "'+f+'"',t);
r[f]={faces:l.length,ok:document.fonts.check('900 24px "'+f+'"',t)}}catch(e){r[f]={err:String(e)}}}
document.title='RES'+JSON.stringify(r)})()</script>""" % json.dumps(TESTES)


def main():
    pages = ["index.html"] + ["posts/" + f for f in sorted(os.listdir(os.path.join(PUB, "posts")))][:3]
    tmp = tempfile.mkdtemp()
    os.symlink(os.path.join(PUB, "fonts"), os.path.join(tmp, "fonts"))
    os.makedirs(os.path.join(tmp, "posts"))
    for p in pages:
        s = open(os.path.join(PUB, p), encoding="utf-8").read().replace("</body>", JS + "</body>")
        open(os.path.join(tmp, p), "w", encoding="utf-8").write(s)
    class Quieto(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass
    handler = functools.partial(Quieto, directory=tmp)
    srv = socketserver.TCPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    port, falhou = srv.server_address[1], False
    for p in pages:
        out = subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--virtual-time-budget=8000",
                              "--dump-dom", f"http://127.0.0.1:{port}/{p}"], capture_output=True, text=True).stdout
        m = re.search(r"<title>RES(.*?)</title>", out)
        res = json.loads(m.group(1).replace("&quot;", '"')) if m else {"página": {"err": "não respondeu"}}
        for fam, r in res.items():
            ok = r.get("ok") and r.get("faces", 0) > 0
            falhou |= not ok
            print(f"{'ok ' if ok else 'ERRO'} {p:28s} {fam:13s} {r}")
    srv.shutdown()
    sys.exit(1 if falhou else 0)


if __name__ == "__main__":
    main()
