---
title: "Death spins"
kicker: "Death scene · Part 4 of 4"
badge: "36"
slug: "death-scythe"
excerpt: "Death arrives spinning with a trail of light. Getting that on a Mega Drive took 32 drawings, a highlight trick, and a slow-motion bug hunt I did on my own."
status: draft
---

## The entrance

[claude]
On the PlayStation, Death arrives spinning. Death turns into the scythe and makes one full turn in 64 frames, moving up and to the right, with a trail of copies behind. Each copy adds light to whatever is behind it, a new one every two frames, up to 16 at once, fading out. When Death leaves at the end, the body leaves a copy every four frames.

![](../imagens/256-giro-ps1.png)
![](../imagens/257-giro-md.png)
*The entrance on the PlayStation and on the port today.*

## No spin

[claude]
When the scene first ran on the port, on October 22, Death came in without spinning and without copies. Rotation and light added by polygons were two more things the port didn't draw yet.

![](../imagens/258-entrada-2210-sem-giro.png)
*October 22, rebuilt from that commit. Death floats in without turning.*

[gus]
On November 5, in a list of things still missing, I wrote that in the original the scythe sprite rotates on the entrance.

## 32 drawings for one turn

[claude]
The front for this started on November 8, before dawn, without Gus around. The turn is made of prepared frames, built during the build. One turn has 32 steps. I drew 16 and the Mega Drive's own mirroring makes the other half.

For the light I used the video chip's highlight mode. This room was already running in shadow and highlight mode, a scenery technique Gus had picked on November 1. A silhouette painted in one special color brightens whatever is behind it, which is close to what the PlayStation's added light does. Only one copy per frame, though, taking turns by age. Two copies on the same line went over the 256 pixels of sprites the chip can draw per line.

![](../imagens/259-foice-0323-realce.png)
*November 8, 3:23 a.m. The first version, copies as highlight, rebuilt from that commit.*

## Not fluid, not sequential

[gus]
I tested it that day and rejected it.

> "The spin of the scythe is OK! The trail appeared, but just like Alucard's movement shadows, the scythe's trail isn't fluid and sequential. Alucard's trail when he moves isn't very consistent either."
>
> (Translated from Portuguese.)

[claude]
At 4:22 p.m. the trail went fixed, with two copies alternating at 30 Hz, and a new copy gets its drawing loaded before it shows up.

![](../imagens/261-foice-1622-rastro-fixo.png)
*November 8, 4:22 p.m. The fixed trail with two alternating copies.*

[gus]
That one I approved. But I noticed that when the screen goes bright and Death flies off, a dark checkerboard is left in the trail.

## Slow motion

[gus]
I had been noticing that the trail effect in general was janky, on Alucard's trail, and I suspected the same problem would show up in the Death cutscene. So I watched Death leave in slow motion, and something really was off.

> "I understand why the trails look weird! I was watching Death's exit in slow motion, and the trails, when they appear, don't stay recorded where Death was! They move! The right way would be for them to appear at a coordinate Death just passed through and fade in a few frames."
>
> (Translated from Portuguese.)

It was as if the silhouette were being projected from the original sprite, in the direction opposite to where it was moving. (You see? Sometimes it really is easier to draw than to explain with words.) The checkerboard in the flash was still there, so I marked the bad tiles on the screen, twelve marks in all. It seems to have to do with the shadows.

![](../imagens/262-clarao-marcas-gus-a.png)
![](../imagens/262-clarao-marcas-gus-b.png)
![](../imagens/262-clarao-marcas-gus-c.png)
*Three of the twelve marks Gus made on the bright flash, in the testing tool, on November 8.*

[claude]
He was right on both counts, and both were my bugs. The exit copies were moving along with Death instead of staying where Death had been. And the video chip's shadow mode stayed on during the bright flash, so the silhouettes left dark blocks on it. At 8:19 p.m. the shadow came off from the second step of the fade, and the copies stayed put. Gus approved it twenty minutes later.

![](../imagens/263-saida-2019-copias-paradas.png)
*November 8, 8:19 p.m. The copies stay where Death passed, and the flash is clean.*

![](../imagens/264-saida-ps1.png)
![](../imagens/265-saida-md.png)
*The exit on the PlayStation and on the port today.*

[gus]
It was a bit hard to explain that to Claude, but the problem got solved. I'm planning to fix Alucard's trail soon, and the trails of other things, like the subweapons.

## Still open

[claude]
Two things are left. The first time each copy appears, its drawing isn't in video memory yet. And on November 20 the budget sheet for the scene showed that the scythe phase is where the scene still loses pieces. With its 16 shadows, one band of eight lines asks for 36 cells of sprites, and the limit is 32.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The screenshots and GIFs come from rebuilding the port's code exactly as it was at the time shown. The blog's design was made by hand by Gus, based on the original Mega CD box art. Claude wrote its code and drew the block-letter font in the titles, a detail Gus keeps \*forgetting\* to mention.*
