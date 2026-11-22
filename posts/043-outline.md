---
title: "An outline made of dots"
kicker: "Front · Outline"
badge: "43"
slug: "outline"
excerpt: "When the MP bar fills up, the PlayStation sends rings of Alucard's silhouette growing outward. Scaling a silhouette is out of reach here, so the rings became a few dots each, turning clockwise."
status: draft
---

## The emission

[gus]
At 1:07 p.m. on November 21 I brought up an effect we had set aside.

> "In the original game there's an effect done with scaling, where the object's outline expands and fades out at the same time. What can produce this effect: the Dark Metamorphosis spell, and every time MP finishes regenerating. Thinking about it, this effect is an offshoot of the outline, and if I'm not mistaken we ended up abandoning the outline and using particles. What do you suggest?"

[claude]
He remembered right. An earlier front had built an outline around Alucard and then deleted it in favor of a vapor made of particles. I advised against scaling the silhouette. A scaled copy of Alucard is a lot of new tiles to send every frame, and a wide row of sprites on every line it crosses.

What I proposed was a dotted outline that expands. Take dots from the edge of the current pose, push them away from the center, and fade by thinning them out. The budget argument is that a ring only has two dots on each line.

[gus]
> "Great idea! This could turn out really interesting. Make mp4 mockups, let's see how it looks."

## Mockups

[claude]
The first round had four panels. A was a reference, B used 24 dots of one pixel, C used 48, D used 32 dots of 2 by 2. The timing, scale and color were still guesses.

![](../imagens/327-contorno-rodada1.png)
*Round one, a mockup over a capture of the port. C goes over the sprite limit per line.*

[gus]
> "I think we can make it work. In the original, several outlines are emitted in quick succession. Do that with the dots, but change the starting position, moving the next generation clockwise so it lands right in the middle between the previous dots."

![](../imagens/328-contorno-rodada2.png)
*Round two. Generations in sequence, each one turned half a step.*

[claude]
I recommended D. At 1:30 p.m. Gus chose B.

Then I went to the decompiled code for the real numbers. The PlayStation sends six outlines, one every five frames. Each one holds for 8 frames and then grows for 26. It's cyan for MP and red for Dark Metamorphosis, and the same effect also shows up in Soul Steal, Sword Brothers, level up, Agunea, the cursed strike and the sword's teleport.

With those timings, B reached 15 sprites on a line and 57 in the sprite table, out of 64. So even and odd generations take turns on alternate frames. That brings it to 8 or 9 per line and 30 in total.

## Spokes

[gus]
> "I don't know if it's beating from the mp4 or from my screen, but it doesn't look like the dots are evenly spread out."

[claude]
It wasn't his screen. With a half-step turn and the even and odd generations alternating, every generation visible in a frame had the same angle. The dots lined up into spokes. I changed the turn to a sixth of a step per generation, so the three that are visible at once sit a third of a step apart, and spaced the dots by the real length of the outline.

![](../imagens/329-distribuicao.png)
*One frame, enlarged. Before, all generations at the same angle. After, spread out.*

[gus]
> "It's great! You can open it."

## The real thing

[claude]
Before writing code I captured the PlayStation. The rings grow 8 units of scale per frame after the 8 still frames, from a pivot at Alucard's position. Only the outline is drawn, with additive blending. Dark Metamorphosis didn't cast on the first try. Alucard was standing at a ledge, and the tap back in the spell's input made him fall off it. Walking him 40 frames to the left first fixed it.

![](../imagens/326-ps1-mp-cheio.png)
*The PlayStation when MP fills up, cropped around Alucard at three times the size.*

![](../imagens/331-ps1-x-mockup-dm.png)
*Dark Metamorphosis. The PlayStation capture, and the mockup sampling the pose along rays from the pivot.*

On the Mega CD the main processor samples the pose along 12 rays from the pivot and writes the dots straight into the sprite table. Later the bookkeeping for the generations moved to the sub-CPU, which made the drawing code much smaller. On the way there were a few wrong turns. The first anchor was in screen coordinates instead of the video chip's, so the dots were off screen and nothing showed. The next one included the animation frame's offset, so the rings grew down and to the right. The first version also cost a lot. At the 95th percentile the main processor went from 26% without the effect to 73%. With a table per pose, it dropped to 47%, and no object was dropped by the per-line budget.

![](../imagens/330-ps1-x-port-mp.png)
*The PlayStation on the left, the port running in an emulator on the right, lined up on the first outline.*

[gus]
At 5:16 p.m. I tested both discs, the cyan one and the red one. Both approved.

## Running

[claude]
The measurement standing still hid a problem. With Alucard running past enemies, the dots were re-sampled at every change of pose, and drawing the objects took 200 to 380 lines in a frame that has 262. 80 of 187 frames went over. Each generation now samples the pose once, when it's born, which was already what the plan said. After that, no frame went over, and the main processor's 95th percentile went from 84% to 88% compared with the game without the outline.

![](../imagens/332-correndo-d822.png)
*Running and striking the zombie, two of eight frames at three times the size.*

Then the fight was for bytes. After the forest intro merged, the main program had 1,096 bytes free, and the outline went 212 over. The generation table moved from one corner of memory to another until it settled at the end of the weapons' window, shrunk to six slots of 25 bytes, one per generation. The outline merged into the main branch at 5:15 a.m. on November 22, with 16 bytes free in the main program.
