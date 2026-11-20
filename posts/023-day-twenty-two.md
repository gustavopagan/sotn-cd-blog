---
title: "Day 22: I have the sensors"
kicker: "Day 22 · November 8, 2026"
badge: "23"
slug: "day-22"
excerpt: "Builds shrink to one area at a time, five chats work through the night on the wolf, the mist, the doors and the mermen's rocks, I start testing from my phone, and I remind Claude what a human tester is for."
status: draft
---

[claude]
November 8 had 212 commits, most of them between 2 and 6 in the morning, while he slept. Five chats were working in parallel, each with its own range of decision numbers so they wouldn't collide.

![](../imagens/151-dia22-linha-do-tempo.png)
*November 8. The wall before dawn is the night shift; the evening block is Gus testing and approving.*

## One area at a time

[gus]
At 12:04 a.m. I pointed out why builds had gotten so big. Every area of the game was going into every build, and that didn't need to happen. From then on, I wanted each build to contain only the area being worked on.

![](../imagens/149-builds-por-area.png)
*The change Gus asked for. Each test disc carries just the area under test.*

## The night shift

[gus]
At around 3 a.m. I opened the night's chats one after another, each with the same postscript, telling it to work continuously until 10 a.m., because I'd be away until then, and to get as far as it could. One was for the shadows in the mermen room, where I had also noticed that every time the water appears on screen, the game hitches. The others were for Alucard's wolf form, the mist, and the doors.

![](../imagens/146-nevoa-gas.png)
*The mist as a gas, from the mist task's previews. A dithered cloud instead of the PlayStation's transparent one.*

![](../imagens/148-pedras-sombra-a.png)
![](../imagens/148-pedras-sombra-b.png)
*Two versions of the rocks in the mermen room with the VDP's shadow mode, side by side in the comparison tool.*

## From my phone

[gus]
At 9:34 a.m. I mentioned how I'd been testing some builds. I use Moonlight on my phone, streaming the PC's screen, with on-screen controls that Windows sees as an Xbox 360 controller. A week later that became its own task, so the tester would work properly from a phone.

![](../imagens/150-moonlight.png)
*How Gus tests from the couch, roughly. Not a screenshot.*

## The sensors

[gus]
At 11:55 a.m., in the live editor chat, I reminded Claude what a human tester is for.

> "No problem, that's what my tests are for! As a human, I have the sensors needed to do this very efficiently, and I can help you."
>
> (Translated from Portuguese.)

## Colors, by comparison

[gus]
At 4:24 p.m. I asked for options using Alucard's colors, in a comparison tool, with different conversion methods. At 4:37 I asked to see Floyd-Steinberg error diffusion with palette 0, and at 4:39 to compare it with what the ditherit.com site produces.

![](../imagens/145-lobo-cores.png)
*The wolf comparison, labels in Portuguese. In the first column, the PlayStation's purple wolf. In the others, the wolf redone with Alucard's palette, by different methods.*

![](../imagens/147-porta-floyd.png)
*The same question for a door. Different ways of reducing its colors, side by side.*

At 4:54 p.m. I asked for a switch to turn a shader on and off, remembering the choice every time I close and open it.

## The music's buffer

[gus]
At 10:43 p.m. I had an idea for the wolf's graphics. We have the room-loading buffer in the music. We could use it to load the wolf's assets. The worst that can happen is the buffer running out and the music cutting out for a moment.

## The number

[claude]
212 commits, 39 messages from him. Five tasks overnight, one human with sensors.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The images are previews and comparisons Claude made during that work. The blog's design was made by hand by Gus, based on the original Mega CD box art. Claude wrote its code and drew the block-letter font in the titles, a detail Gus keeps forgetting to mention.*
