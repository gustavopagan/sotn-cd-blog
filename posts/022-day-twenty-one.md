---
title: "Day 21: Development by Pagan."
kicker: "Day 21 · November 7, 2026"
badge: "22"
slug: "day-21"
excerpt: "The title screen gets its credit line and its period, the Konami logo becomes the one from Sega cartridges, I lose a file I worked hard on, and the damage numbers get a font three pixels wide."
status: draft
---

The title screen was finished at 12:12 a.m. on November 7. Twenty-seven minutes later I thought I had lost it.

![](../imagens/144-dia21-linha-do-tempo.png)
*November 7. Title screen after midnight, effects and fonts in the evening.*

## The credit line

At 12:07 a.m. I asked for the credit line in a five-pixel-tall font I had brought, in the same color, with a drop shadow to the southwest. At 12:08: on a single line, if it fits. At 12:10: there's a period missing after "PAGAN". At 12:12: done, we have the title screen.

![](../imagens/141-titulo-cores-a.png)
![](../imagens/141-titulo-cores-b.png)
*The title screen before and after a color pass, from the title's history folder. The credit line at the bottom ends with the period I asked for.*

## A period Konami logo

The PlayStation version opens with a Konami video before the title. At 12:31 a.m. I asked to swap it for something more fitting for the era: the Konami logo animation they used on their Sega Genesis games. At 12:34: careful not to leave out the green beam that draws the logo's shadow. Claude recorded it from one of my cartridges, Tiny Toon Adventures: Buster's Hidden Treasure, frame by frame and with its sound.

![](../imagens/143-vinheta-konami.gif)
*The Konami logo animation from the Tiny Toon Adventures cartridge, recorded in an emulator for the port.*

## The file I lost

At 12:39 a.m.: "Something went very wrong! That was the edit I had made on the title screen! It took a lot of work, but I think I lost the file! I had cleaned up a lot of dirt..." A minute later I worked out what happened: I hadn't saved, then opened the version without my work and saved over it. What I had left was a screenshot I had taken of it. (Translated from Portuguese.)

## Watching instead of describing

At 1:01 a.m. I used the live editor for the warg's slowdown spikes: "see comment logica ce1". Then I asked the question that made the tool worth it: when I leave a comment like this, can you watch the gameplay and see the metrics? I had just waited for the intro and let the warg attack Alucard, nothing else. At 1:57 a.m. I noted that the HP orb sometimes doesn't blink, but maybe because Alucard, at level 99 in the first area, sometimes takes no damage at all.

## Sparks, blood and fonts

In the afternoon the effects. At 10:15 a.m. I asked for a general cleanup of invisible sparks, and to see them on screen first. At 12:43 p.m., about the orb's bubbles: this kind of particle effect could be used a lot, even replacing the blood particles on damage, if we can make it cheap. At 1:36 p.m.: it has to be programmed so particles don't pile up on the same line. At 7:23 p.m. I guessed that some blue sparks I'd seen were the Alucard Sword's effect.

At 7:30 p.m. I asked Claude to narrow the pixel font I had sent for the title: the letters wider than three pixels could be thinner, to save space. At 7:34, let's try it for the damage numbers. At 7:43: great, we saved more pixels with that size.

![](../imagens/142-fonte-pixel.png)
*The font, three ways: gray, the original; white and blue, narrowed versions. Two of the lines show credit wordings we tried.*

At 10:49 p.m. I identified the font the original uses for "LIFE MAX UP", the area titles and "NOW LOADING": Canto Brush, italic, probably bold, likely customized by Konami. At 11:05 I asked for something like the original's wavy "Now Loading", which the player can play with by holding the d-pad, and at 11:14, after seeing the preview: it looks a bit clumsy while it waves; try it without copying the original.

At 11:50 p.m. I noticed something about the tooling itself: all those waits in Claude's commands were eating the time we had gained by running builds on my machine. I asked for that to be written into the project, not left as an improvement only that chat knew about.

## The number

64 commits, 58 messages from me. One credit line, with its period.

*How this is made: I decide what the port should be, draw and pick colors, and test every build. The code, tools and measurements are written by Claude (Anthropic's AI). This post was drafted by Claude from my chat messages and the project's commit history, and reviewed by me.*
