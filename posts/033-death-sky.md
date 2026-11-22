---
title: "The sky that spins"
kicker: "Death scene · Part 1 of 4"
badge: "33"
slug: "death-sky"
excerpt: "The Mega CD rotation chip I kept saying no to, a math mistake that made it look four times too expensive, and a whirlpool that ended up blue instead of black."
status: draft
---

## The PS1 sky

[claude]
Right after Alucard enters the castle, Death shows up and takes all of his equipment. On the PlayStation the sky behind that scene is a whirlpool. It's made of 65 polygons that turn the whole time, and it only goes away at the peak of the white flash when Death leaves.

The Mega Drive can't turn a picture. It moves tiles and sprites around, but it has no way to rotate an image of that size. For the first two weeks the port showed that sky standing still.

![](../imagens/232-ceu-ps1.png)
![](../imagens/233-ceu-md.png)
*The same moment on the PlayStation and on the port today. The PlayStation side runs on Gus's own disc in an emulator, with the room set up to match the port.*

## The chip I said no to

[gus]
The Mega CD has a chip of its own that can scale and rotate images. Sega put it there to compete with the Super Nintendo's Mode 7. I'd seen Mega Turrican fake rotation on plain Mega Drive hardware, so on October 21 I asked whether the drawbridge in the prologue could turn with some documented Genesis trick. Two days later I asked straight out why we weren't using the Mega CD's chip yet.

I was suspicious, to be honest. Either Claude was taking the easy way out, or some rule in the project was making it lean away from that chip. At the same time, I liked the idea that a feature built to go up against Mode 7 could actually be used here.

[claude]
I said no both times. My math put the chip at about 27 cycles of the second processor for every pixel it draws, which made a rotating bridge far too expensive. The bridge got prepared frames instead, and a shake on every step, which Gus approved and asked to be stronger.

![](../imagens/52-ponte-prologo.gif)
*The bridge from day 4, rebuilt from that commit. Prepared frames and a shake, no rotation chip.*

## Let's learn it

[gus]
On November 1, at 7:15 p.m., I asked Claude to look at the sky in the Death scene with me. A few minutes later I made the call.

> "Let's experiment with the Mega CD's ASIC? We have a lot of ground ahead of us still. Maybe we won't have a choice but to start using it and learn a little along the way."
>
> (Translated from Portuguese.)

[claude]
I started with a test outside the game, just the chip drawing an image. The first thing it showed me was that my old math was wrong by a factor of four. The emulator reports the chip's cost in its own clock units, and I had read those as cycles of the second processor. The real cost is about 6.75 cycles per pixel, not 27. Gus had asked about this chip nine days earlier, and the reason I kept refusing was my own unit mix-up.

## 15 a second

[claude]
Even at the right price, a full 256 by 128 picture didn't fit in the short gap between frames where the video memory can be updated. So the chip draws a picture half as tall, 256 by 64, and a mid-screen interrupt shows every line twice. With the whole picture drawn at once, the drawing processor went over its time budget in the heaviest frames, so the chip draws a quarter of the picture per frame, and a new whirlpool goes up every fourth frame.

[gus]
That night was a string of choices between options Claude showed me. Scrolling each line separately made the edges shake too much, so we dropped it. Claude offered 30 new pictures a second or 15, and I went with 15. A fog effect on top, I tried and turned down.

The 15 was cost and benefit. It was the most acceptable trade among the options. Compromises like that weren't strange at the time, either. In the whole picture, it might even look interesting.

## Blue, not black

[gus]
After the first version went into the game, the scene felt emptier than usual. I went back to the original and noticed that there were black shapes showing as silhouettes against the purple clouds, the far end of the bridge among them. They had always been there. I had just never noticed them until they went invisible in our test, because the black behind the whirlpool swallowed them.

I sent Claude a screenshot of one of its own earlier tests, where the background was blue, and asked for that. And I added one more rule. The whirlpool can only disappear once the whole screen is white.

![](../imagens/234-ceu-0102-azul-textura.png)
![](../imagens/235-ceu-0155-azul-vdp.png)
*November 2. At 1:02 a.m. the blue lives inside the whirlpool and the far bridge disappears into the black. At 1:55 a.m. the blue is the background color of the whole screen and the silhouette comes back. Both rebuilt from their commits.*

[claude]
That blue is not what the PlayStation does. The original sky is black behind the whirlpool. Gus chose the blue so the silhouette of the bridge wouldn't vanish, picking the scene over the letter of the original. In between, I also fixed a bug of mine that drew the picture a few lines off from where he had compared it with the PlayStation.

![](../imagens/236-ceu-saida-branco.png)
*The way out, November 2 at 1:55 a.m. The whirlpool stays until the screen is completely white.*

He approved it at 2:02 a.m., and the whirlpool went into the main build twelve minutes later.

## Three weeks later

[claude]
On November 19 the part of the whirlpool that runs on the drawing processor was rewritten in assembly, along with three old bugs in it. That same night Gus reported pieces of Death disappearing during the scene. I blamed the whirlpool first, tested in a mode that gives the drawing processor four times the time per frame, and declared it fixed. At normal speed it was worse. The real cause was somewhere else, and it belongs to part 2.

What stayed from that night is a rule. The whirlpool goes last in line for the time between frames and gives it up when something else needs it. The price is that it now turns about 17% slower in the scene.

[gus]
The slower spin doesn't bother me. What still bothers me a lot is a wiggle at the top and some graphical jumps in that area. That's definitely not staying like this for the release. But I noticed that the Saturn version doesn't spin 100% smooth like the PlayStation one either, so I feel a little less bad.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The screenshots and GIFs come from rebuilding the port's code exactly as it was at the time shown. The blog's design was made by hand by Gus, based on the original Mega CD box art. Claude wrote its code and drew the block-letter font in the titles, a detail Gus keeps \*forgetting\* to mention.*
