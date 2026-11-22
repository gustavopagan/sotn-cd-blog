---
title: "Nine subweapons, one at a time"
kicker: "Front · Subweapons"
badge: "38"
slug: "subweapons"
excerpt: "I asked Claude to capture every subweapon on the PlayStation against a black screen, and then we went through them one by one. A stopwatch that freezes the world in gray, a lightning bolt redone piece by piece, and a stone that leaves a line."
status: draft
---

## A black background

[gus]
On November 19, after a round of tests, I asked Claude to capture the subweapons on the PlayStation with a black background. Turn off the background layers and change the subweapon directly in memory, like an Action Replay, and capture each one frame by frame, with Alucard's throwing pose too. Then I asked for those capture points to be ready in the testing tool, so I could see them and try them myself.

[claude]
I did it in a PlayStation emulator with no window, writing straight into its memory. Background layers off, background color black, HUD off, and the enemies of the stage removed. Nine subweapons, standing and jumping.

![](../imagens/278-ps1-machado-fundo-preto.gif)
![](../imagens/279-ps1-agunea-fundo-preto.gif)
*The axe and the Agunea on the PlayStation, with everything else switched off. These captures became the reference for the whole front.*

[gus]
Then, on November 20, I asked Claude to capture the evolution of each subweapon as it went.

## The stopwatch

[claude]
On the PlayStation the Stopwatch freezes time. My first version, that afternoon, flashed white and sent a shock wave across the screen by scrolling it in columns 16 pixels wide.

![](../imagens/280-stopwatch-onda-colunas.png)
*November 20, the first shock wave, in columns.*

[gus]
At 4:47 p.m. I said the bands were too chunky. I wanted the motion to be really jelly-like, line by line, and slow, to give a feeling of slow motion. The time the waves take to go from the center to the end of their path should be the whole time the stopwatch runs. Then I asked if it could affect every layer except Alucard, or if that would be too expensive. Then a much smaller wave, a single one for each half of the screen, one going up and one going down, leaving the screen exactly when the timer ends.

At 6:30 p.m. I had one more idea. Every palette except the common one turns into the gray with the closest brightness, so the whole game goes black and white during the stopwatch, except Alucard, the HUD and the common colors.

[claude]
Each of those was one round. Scrolling line by line can't split a single line in half, so the waves go up and down from the middle of the screen instead of from a point. The objects wave too, one offset per sprite, with the HUD and Alucard standing still. The gray is done in the same place the game already fades colors, turning three of the four palette lines gray by brightness. At the end of the time the wave comes back to the middle and arrives on the same frame as the white flash that brings the colors back.

[gus]
Two last notes. On the way back the wave could be bigger and speed up as it gets closer to the center. And could the bottom wave be inverted instead of mirrored?

At 7:53 p.m. I wrote "super approved".

![](../imagens/281-stopwatch-onda-final.png)
*The approved stopwatch. The world goes gray, a wave leaves from the middle in each direction, and the bottom one is inverted.*

## A bolt, piece by piece

[claude]
The Agunea fires a bullet, and when it hits an enemy a bolt of lightning connects Alucard to it. My first version guided the bolt toward the enemy in 12-pixel steps, the way the game's code does.

![](../imagens/282-agunea-raio-j23.png)
*November 20, the first zigzag bolt from Alucard to the warg.*

[gus]
Then I went through it piece by piece, late that night. The whole screen goes white for one frame on the hit and then every other frame. The segments fade out with a dither, from the outside toward the bright center, before the next bolt. The bullet carries only a blue trail, no piece of lightning. And when the enemy is far, the first pieces can disappear to make room for the ones at the tip.

![](../imagens/283-agunea-fita-j30.png)
*The bolt as a ribbon, white on the hit, fading from the outside in.*

[gus]
Past midnight I asked for some feedback on Alucard himself while the bolt is lit, with the critical hit flash, limited to neutrals, light colors and blues. Claude made a mockup first. "That's good like that!"

![](../imagens/284-agunea-alucard-pisca-j33.png)
*Alucard and the HUD flashing while the bolt is lit, at twice the size.*

## A stone that leaves a line

[claude]
On the PlayStation the Rebound Stone doesn't show a stone at all. The capture shows only a line for each stretch between bounces.

![](../imagens/285-pedra-ps1-quadros.png)
*The PlayStation's Rebound Stone, frames 20 to 66 every other frame. Only lines.*

[gus]
At 2:01 a.m. I said the trail could be a line that gets thinner the way the Agunea's trail does, fading as more of it is drawn. What bothered me most was the segments moving around and breaking the line. At 8:43 a.m. it still wasn't a continuous line. The Agunea's line is really beautiful and fades elegantly. Couldn't we copy it?

[claude]
So I stopped placing pieces and had the logic processor draw the line itself, pixel by pixel, inside boxes of tiles, with the loop in assembly.

![](../imagens/286-pedra-rastro-j44.png)
*The stone's trail drawn pixel by pixel along its path, dithered like the Agunea's, at twice the size.*

## Ghosts, embers and vapor

[gus]
Before going to sleep on November 21 I left three requests. Embers on the pages of the book. The trail technique from the trails front applied to the axe, dagger, cross and book, with a palette for each weapon. And green vapor on the holy water.

[claude]
All three went in, and the logic processor's memory ran out. The new code went 2,040 bytes over its space. The answer was the one we had used for the mist. The drawing code of the subweapons moved into the module that loads with each group of rooms, which left 2,640 bytes free.

![](../imagens/287-machado-r22.png)
![](../imagens/288-livro-r21.png)
![](../imagens/289-agua-benta-r20.png)
*November 22. The axe with a gray ghost, the book with pages and embers, the holy water with green vapor.*

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The screenshots and GIFs come from the port's builds at the time shown. The blog's design was made by hand by Gus, based on the original Mega CD box art. Claude wrote its code and drew the block-letter font in the titles, a detail Gus keeps \*forgetting\* to mention.*
