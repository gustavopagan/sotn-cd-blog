#!/usr/bin/env python3
from ilus import *
from PIL import Image
C = "12:03 12:04 12:06 12:07 12:12 12:15 12:19 12:22 12:37 12:37 12:44 12:46 12:48 12:48 12:54 12:55 13:11 13:13 13:15 13:18 13:38 13:51 14:02 14:05 14:06 14:21 14:24 14:34 14:48 14:54 15:00 15:08 15:13 15:13 15:17 15:25 15:30 15:35 15:39 16:21 16:24 16:29 16:30 16:32 16:32 16:32 16:34 16:38 16:46 16:53 16:55 16:57 16:58 17:01 17:02 17:08 17:12 17:24 17:41 17:42 17:52 17:55 18:08 18:19 18:20 18:20 18:20 18:20 18:20 18:23 18:23 18:24 18:25 18:26 18:27 18:29 18:31 18:44 18:46 18:46 18:50 18:51 18:51 18:51 18:53 18:54 18:59 18:59 19:00 19:20 19:20 19:24 19:28 19:31 19:46 19:47 19:48 19:54 19:58 19:59 19:59 20:08 20:11 20:12 20:12 20:12 20:15 20:17 20:17 20:28 20:29 20:40 20:50 20:50 20:57 20:58 21:02 21:02 21:08 21:18 21:21 21:24 21:25 21:26 21:28 21:28 21:29 21:30 21:42 21:43 22:07 22:08 22:15 22:32 22:32 22:34 22:34 22:35 22:37 22:39 22:40 22:40 22:40 22:41 22:43 22:45 22:45 22:54 23:04 23:09 23:11 23:20 23:24 23:31 23:34 23:34 23:37 23:38 23:54".split()
F = "12:02 12:03 12:04 12:05 12:09 12:22 12:27 13:03 13:04 13:05 13:32 14:46 14:49 14:49 14:49 14:50 14:50 14:50 14:50 14:51 14:51 14:52 14:53 14:59 15:11 15:38 15:41 15:45 15:48 15:49 15:59 16:05 16:10 16:12 16:13 16:14 16:14 16:16 16:16 16:16 16:16 16:16 16:16 16:17 16:17 16:17 16:19 16:40 16:41 20:14 20:16 20:16 20:16 20:16 20:16 20:16 20:16 20:16 20:18 20:18 20:18 20:28 20:28 20:28 20:30 20:31 20:36 20:38 21:26 21:26 21:28 21:28 21:30 21:52 22:27 22:31 22:31 22:32 22:34 22:35 22:37 22:39 22:40 22:40 22:40 22:40 22:40 22:40 22:40 22:40 22:41 23:06 23:09 23:10".split()
PREV = "/mnt/user-data/uploads/SOTN CD/50-previas/"


def portao():
    """Nine fronts, one gate. Who waits for whom."""
    t = Tela(1200, 640, "Nine chats, one traffic light", "DIAGRAM")
    t.caixa(40, 120, 290, 250, "ferramentas2", GREEN, ["emulator tools", "may merge alone"])
    t.caixa(420, 120, 670, 250, "limites", RED, ["frees code space", "may merge alone"])
    t.seta(295, 185, 415, 185, rotulo="merged\n(or stopped)")
    xs = [40, 280, 520, 760]
    nomes = [("poses-inimigos", "enemy poses"), ("sub-nativo", "wolf, collision"), ("orcamento-no3", "area budget"),
             ("efeitos-leves2", "light effects"), ("colheita-motor", "old branch harvest"), ("cores-ce2", "Entrance colors"),
             ("menus-som", "menu sounds")]
    for i, (n, s) in enumerate(nomes):
        x = 40 + (i % 4) * 285
        y = 360 if i < 4 else 500
        cor = YELLOW if n == "menus-som" else BLUE
        t.caixa(x, y, x + 250, y + 100, n, cor if cor != YELLOW else (180, 140, 0), [s])
    t.seta(545, 255, 545, 350, rotulo="before the\ntest disc")
    t.texto(890, 130, "Each chat checks the light,\nleaves a note and comes back\nby itself 20 minutes later.", 18, INK, False)
    t.texto(890, 540, "menus-som could not even\nstart coding before limites.", 16, INK, False)
    t.salva("153-nove-chats.png")


def vm():
    barras("154-vm-espaco.png", "The VM disk, one chat's cleanup",
           ["chat's space before", "chat's space after", "VM free before", "VM free after"],
           [2000, 7, 1000, 3000], [RED, GREEN, RED, GREEN], " MB", w=1100, h=440, selo="MEASURED")


def colar():
    t = Tela(1100, 520, "The same message, pasted into every chat", "DIAGRAM")
    t.caixa(40, 200, 270, 330, "me", BLUE, ["Ctrl+V", "x 9 or 10"])
    msgs = [("2:49 p.m.", "run the VM cleanup script", 10), ("8:16 p.m.", "put the tests in the tester", 9),
            ("10:40 p.m.", "Entrance + Alchemy Lab only", 9)]
    for i, (h, m, n) in enumerate(msgs):
        y = 110 + i * 130
        t.caixa(520, y, 1060, y + 100, h, GRAY, [m, f"{n} chats"])
        t.seta(275, 265, 515, y + 50)
    t.salva("160-colar.png")


def comp(a, b, out, s=2, gap=16):
    A = Image.open(a).convert("RGB"); B = Image.open(b).convert("RGB")
    im = Image.new("RGB", (A.width + B.width + gap, max(A.height, B.height)), (20, 20, 20))
    im.paste(A, (0, 0)); im.paste(B, (A.width + gap, 0))
    if s != 1:
        im = im.resize((im.width * s, im.height * s), Image.NEAREST)
    im.save(OUT + "/" + out, optimize=True); print("ok", out)


def capturas():
    c = PREV + "comparadores/comparador_ce2_b194/src/"
    comp(c + "base/NO3_portao7.png", c + "rec/NO3_portao7.png", "155-portao.png", 3)
    A = Image.open(c + "base/NP3_slogra.png").convert("RGB").crop((0, 0, 720, 160))
    B = Image.open(c + "rec/NP3_slogra.png").convert("RGB").crop((0, 0, 720, 160))
    im = Image.new("RGB", (720, 336), (20, 20, 20)); im.paste(A, (0, 0)); im.paste(B, (0, 176))
    im.save(OUT + "/156-slogra.png", optimize=True)
    Image.open(PREV + "comparadores/comparador_ce2_b191/imagens/NO3_08.png").convert("RGB").save(OUT + "/157-sala8-sombra.png", optimize=True)
    r = Image.open(PREV + "menus-som/relampago_ps1_4.png").convert("RGB")
    tiras = [r.crop((0, i * 240, 512, i * 240 + 240)) for i in range(4)]
    im = Image.new("RGB", (512 * 2 + 12, 240 * 2 + 12), (20, 20, 20))
    for i, tt in enumerate(tiras):
        im.paste(tt, ((i % 2) * 524, (i // 2) * 252))
    im.save(OUT + "/158-relampago-ps1.png", optimize=True)
    Image.open(PREV + "soma-ln/rr3/f02150.png").convert("RGB").save(OUT + "/159-lobo-porta.png", optimize=True)
    print("ok capturas")


if __name__ == "__main__":
    print(len(C), len(F))
    linha_do_tempo("152-dia23-linha-do-tempo.png", "November 9, hour by hour", C, F,
                   notas=[("15:45", "3:45 p.m.: wait for each other?", "l"),
                          ("22:40", "10:40 p.m.: 2 areas", "r")],
                   sombras=[(16.7, 20.2, "I'm away")])
    portao(); vm(); colar(); capturas()
