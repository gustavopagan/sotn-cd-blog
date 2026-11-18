#!/usr/bin/env python3
"""Ilustrações do post 7 (dia 6, 23/10)."""
import math
from ilus import *

COMMITS = "00:01 00:03 00:03 00:06 00:07 00:08 00:12 00:12 00:13 00:13 00:13 00:14 00:15 00:15 00:16 00:17 00:18 00:18 00:18 00:20 00:21 00:21 00:22 00:22 00:23 00:24 00:28 00:30 00:31 00:32 00:33 00:34 00:39 00:41 00:47 00:48 01:03 01:09 01:14 01:20 01:38 01:41 01:50 01:50 01:54 02:02 02:09 02:51 03:17 14:14 14:48 15:02 15:50 15:57 16:02 16:36 17:02 17:03 17:10 17:24 17:33 17:39 17:41 17:47 17:50 18:03 18:12 18:13 18:14 18:23 18:28".split()
FALAS = ("00:07 00:11 00:22 00:25 00:27 00:30 00:33 00:42 00:50 00:52 00:54 00:59 01:01 01:05 01:30 01:32 "
         "01:33 01:44 02:00 02:01 11:37 11:44 11:45 11:47 12:03 12:04 12:07 12:09 12:13 12:20 12:38 12:43 "
         "12:46 12:48 12:49 12:55 13:02 13:42 13:54 13:59 14:04 14:08 14:09 14:17 14:20 14:22 14:26 14:27 "
         "14:29 14:35 14:56 14:58 15:01 15:04 15:05 15:09 15:23 15:37 15:49 15:58 16:13 16:36 16:37 16:38 "
         "16:45 16:52 17:00 17:01 17:02 17:10 17:16 17:17 17:21 17:23 17:27 17:52 17:54 17:58 18:30 18:56 "
         "18:59 19:01 19:27 21:04 21:05 21:07 21:48 21:49 22:24 22:30 22:33 22:57 23:13 23:15 23:16 23:17 23:21").split()


def tempo():
    linha_do_tempo("66-dia6-linha-do-tempo.png", "October 23, hour by hour", COMMITS, FALAS,
                   notas=[("12:03", "noon: Space Bruce answers", "l"),
                          ("15:49", "3:49 p.m.: \"don't be conservative\"", "l"),
                          ("23:17", "11:17 p.m.: \"doritos\"", "r")],
                   sombras=[(3.4, 11.5, "quiet")])


def lamina(d, cx, cy, ang, esc=1.0, cor=GRAY):
    pts = [(-6, -40), (6, -40), (6, 10), (22, 18), (22, 34), (-22, 34), (-22, 18), (-6, 10)]
    a = math.radians(ang)
    q = [(cx + esc * (x * math.cos(a) - y * math.sin(a)), cy + esc * (x * math.sin(a) + y * math.cos(a))) for x, y in pts]
    d.polygon(q, fill=cor, outline=INK)


def giros():
    t = Tela(1200, 560, "Rotation without a rotation chip: frames drawn in advance", "DIAGRAM")
    d = t.d
    for row, (n, y, cor) in enumerate(((32, 150, LIGHT), (16, 290, (190, 190, 200)), (8, 430, GREEN))):
        t.texto(40, y, f"{n} steps", 20, INK, True, "lm")
        for i in range(n):
            x = 180 + i * (980 / 32) * (32 / n) * (1 if n < 32 else 1)
            if x > 1170:
                break
            lamina(d, x + 14, y, 360 * i / n, 0.5 if n == 32 else 0.7, cor)
    t.texto(600, 510, "Each step is a separate picture made during the build. Fewer steps, fewer tiles in memory.\nI asked for 8: the spins don't need to be that smooth.",
            16, INK, False, "mt")
    t.salva("67-giro-passos.png")


def doritos():
    t = Tela(1200, 420, "Meet doritos", "DIAGRAM")
    d = t.d
    tri = [(0, -1, 0), (0.9, 0.6, 0), (-0.9, 0.6, 0)]
    for k in range(8):
        ax, ay, az = k * 0.5, k * 0.8, k * 0.3
        def rot(p):
            x, y, z = p
            y, z = y * math.cos(ax) - z * math.sin(ax), y * math.sin(ax) + z * math.cos(ax)
            x, z = x * math.cos(ay) + z * math.sin(ay), -x * math.sin(ay) + z * math.cos(ay)
            x, y = x * math.cos(az) - y * math.sin(az), x * math.sin(az) + y * math.cos(az)
            return x, y, z
        q = [rot(p) for p in tri]
        cx, cy = 100 + k * 142, 200
        pts = [(cx + 55 * x, cy + 55 * y) for x, y, z in q]
        n = (q[1][0] - q[0][0]) * (q[2][1] - q[0][1]) - (q[1][1] - q[0][1]) * (q[2][0] - q[0][0])
        cor = (240, 150, 30) if n > 0 else (190, 100, 20)
        d.polygon(pts, fill=cor, outline=INK)
        t.texto(cx, 290, f"frame {k}", 14, GRAY, False, "mt")
    t.texto(600, 340, "One flat triangle spinning on all three axes. At 11:17 p.m. I named it doritos.\nThe coffin's explosion is made of them.",
            16, INK, False, "mt")
    t.salva("68-doritos.png")


if __name__ == "__main__":
    tempo(); giros(); doritos()
