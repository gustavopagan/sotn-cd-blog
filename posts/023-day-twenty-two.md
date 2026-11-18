---
title: "Day 22: I have the sensors"
kicker: "Day 22 · November 8, 2026"
badge: "23"
slug: "day-22"
excerpt: "Builds shrink to one area at a time, five chats work through the night on the wolf, the mist, the doors and the mermen's rocks, I start testing from my phone, and I remind Claude what a human tester is for."
status: draft
---

November 8 had 212 commits, most of them between 2 and 6 in the morning, while I slept. Five chats were working in parallel, each with its own range of decision numbers so they wouldn't collide.

![](../imagens/151-dia22-linha-do-tempo.png)
*November 8. The wall before dawn is the night shift; the evening block is me testing and approving.*

## One area at a time

At 12:04 a.m. I pointed out why builds had gotten so big: every area of the game was going into every build, and that didn't need to happen. From then on, I wanted each build to contain only the area being worked on.

![](../imagens/149-builds-por-area.png)
*The change I asked for. Each test disc carries just the area under test.*

## The night shift

At around 3 a.m. I opened the night's chats one after another, each with the same postscript: work continuously until 10 a.m., I'll be away until then, get as far as you can. One was for the shadows in the mermen room, where I had also noticed that every time the water appears on screen, the game hitches. The others were for Alucard's wolf form, the mist, and the doors.

![](../imagens/146-nevoa-gas.png)
*The mist as a gas, from the mist task's previews: a dithered cloud instead of the PlayStation's transparent one.*

![](../imagens/148-pedras-sombra.png)
*Two versions of the rocks in the mermen room with the VDP's shadow mode, side by side in the comparison tool.*

## From my phone

At 9:34 a.m. I mentioned how I'd been testing some builds: Moonlight on my phone, streaming the PC's screen, with on-screen controls that Windows sees as an Xbox 360 controller. A week later that became its own task, so the tester would work properly from a phone.

![](../imagens/150-moonlight.png)
*How I test from the couch, roughly. Not a screenshot.*

## The sensors

At 11:55 a.m., in the live editor chat, I wrote: "No problem, that's what my tests are for! As a human, I have the sensors needed to do this very efficiently, and I can help you." (Translated from Portuguese.)

## Colors, by comparison

At 4:24 p.m. I asked for options using Alucard's colors, in a comparison tool, with different conversion methods. At 4:37 I asked to see Floyd-Steinberg error diffusion with palette 0, and at 4:39 to compare it with what the ditherit.com site produces.

![](../imagens/145-lobo-cores.png)
*The wolf comparison, labels in Portuguese. First column: the PlayStation's purple wolf. The others: the wolf redone with Alucard's palette, by different methods.*

![](../imagens/147-porta-floyd.png)
*The same question for a door: different ways of reducing its colors, side by side.*

At 4:54 p.m. I asked for a switch to turn a shader on and off, remembering the choice every time I close and open it.

## Borrowing the music's buffer

At 10:43 p.m. I had an idea for the wolf's graphics. We have the room-loading buffer in the music. We could use it to load the wolf's assets. The worst that can happen is the buffer running out and the music cutting out for a moment.

## The number

212 commits, 39 messages from me. Five tasks overnight, one human with sensors.

*How this is made: I decide what the port should be, draw and pick colors, and test every build. The code, tools and measurements are written by Claude (Anthropic's AI). This post was drafted by Claude from my chat messages and the project's commit history, and reviewed by me. The images are previews and comparisons Claude made during that work.*
