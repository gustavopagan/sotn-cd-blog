---
title: "Dust with a soft edge"
kicker: "Front · Dust"
badge: "42"
slug: "dust"
excerpt: "The dust clouds were one flat checkerboard. Gus wanted them dense in the middle and sparse at the edge, then less regular, then a little darker toward the outside. Three discs in one day."
status: draft
---

## Denser in the middle

[gus]
At 12:37 a.m. on November 21 I asked for a revision of the dust.

> "Today it has a continuous checkerboard across its whole radius. I want to change it so the checkerboard gets sparser the closer it is to the edge and denser the closer it is to the center, but always a checkerboard."

[claude]
The dust clouds are converted from the disc by the build tools. On the PlayStation they're half transparent, and an earlier decision in the port drew them as a plain checkerboard. I kept the full checkerboard out to 30% of the radius and let it thin to 20% of the grid at the edge, cutting it with a 4 by 4 Bayer pattern.

![](../imagens/322-poeira-folha-v1.png)
*Five frames of one dust cloud. Top, the PlayStation, solid. Middle, the old continuous checkerboard. Bottom, the first radial version.*

[claude]
On the way I gave the decision a number that belonged to another front's range, and had to renumber it.

## Too regular

[gus]
At 1:04 p.m. I approved the test, with one complaint.

> "I think the kind of checkerboard is still too patterned, and you can make out horizontal and vertical lines in the dust because of it. Can you make the dust's checkerboard more irregular?"

[claude]
A Bayer matrix is regular by design, and it repeats every four pixels. I swapped it for a 32 by 32 blue noise texture, which spreads the dots out without forming rows or columns.

![](../imagens/323-bayer-vs-azul.png)
*Six frames. Top, the Bayer cut. Bottom, blue noise.*

## Darker toward the edge

[gus]
> "Great! I saw the PNG preview in your reasoning and liked it a lot! One more detail: today the dust uses only one color from the fixed palette. Could it use more neutral (or almost neutral) colors to make a gradient from the inside out that leaves the outer area a little darker?"

[claude]
The fixed palette is the line of 16 colors that paints things that can appear anywhere in the game. It has a short run of neutrals. I made two ramps. Ramp A uses colors 11, 12 and 14. Ramp B adds 13, which turned the dust green, so I recommended A. The steps between colors are also cut by blue noise.

![](../imagens/324-poeira-gradacao.png)
*Nine frames over a dark blue and a brown background. The previous version, ramp A and ramp B.*

Two things turned up while I was in there. The old color mixing also used Bayer, which put the beige on a regular grid. And the build's cache didn't notice the new dust setting, so a stale build could have hidden the change. The cost was about 0.4 KB more in the area packs.

[gus]
At 1:48 p.m. I asked to see the fixed palette, and answered with one letter.

> "A"

![](../imagens/325-paleta-comum.png)
*The fixed palette, with the three dust colors marked.*

[claude]
Ramp A was already the one on the disc. Gus tested it and approved it at 2:17 p.m. There's no in-game capture of this one. Both tests were done in the testing tool without recording.
