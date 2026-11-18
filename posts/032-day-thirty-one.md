---
title: "Day 31: It didn't resist"
kicker: "Day 31 · November 17, 2026"
badge: "32"
slug: "day-31"
excerpt: "The assembly rewrite I was afraid Claude would resist runs all night and frees almost 5 KB, I catch a merge that left the new menu switched off, and I suspend the FM music until I'm ready for it."
status: draft
---

The night before, I had worried out loud that the assembly chat would resist the idea of rewriting our code by hand. It didn't. It worked through the night, and by morning there was a report.

![](../imagens/208-dia31-linha-do-tempo.png)
*November 17. My message record for this day ends mid-afternoon; the evening tests show up only in the commits.*

## A night of assembly

The goal was memory, and the measure was bytes. Claude rewrote by hand the parts of the logic program that are ours and that the compiler left bigger than they needed to be: the damage numbers, the text of the warnings and speech bubbles, the object drawing swaps, the drawing list, Alucard's colors, the sound requests. Each one has a switch that goes back to the C. And Claude built an automatic checker: it runs the old and new versions side by side with tens of thousands of random inputs, and the disc doesn't come out if any answer differs. In each file it planted 2 to 7 bugs by hand to make sure the checker caught them.

The variant with FM music had 24 bytes left in the logic program. After the night, 4,496.

In the afternoon came a second idea, not a rewrite but a change in how the code is compiled: the 21 most-cited variables went into one block, with a processor register always pointing at it, so each mention costs 2 bytes instead of 4. Then the drawing program got the same kind of treatment.

![](../imagens/209-bytes-sub.png)
*Free space in the logic program across the day. The dip in the middle is other tasks' merges taking their share.*

![](../imagens/210-bytes-ipx.png)
*The drawing program, the tighter side, back above the project's goal.*

Speed stayed the same or got slightly better. In each step, 20 of 20 recordings had the game's state identical frame by frame. The report also listed Claude's own mistakes: a routine for Alucard's colors used by another one it hadn't seen, a sign error in a comparison caught by the checker on the first run, and later a measurement of 712 bytes saved that turned out to be false, taken before linking. Measured properly, it was 92.

## A menu left behind

The native menu merged into the main branch overnight. At 11:31 a.m. I tested it:

> "Tests done, everything works, but does this test include all of the native menu task's work? The menu still has the old design."
>
> (Translated from Portuguese.)

At 11:32, in the menu chat: "Take a look at the merge result. It seems very little of the native menu's work went over there. I found that strange." At 1:58 p.m. the second merge made the native pause menu the default.

![](../imagens/211-menu-nativo-a.png)
![](../imagens/211-menu-nativo-b.png)
*The native menu running in the emulator: the main screen at 12:52 p.m. that day, and the Familiars screen from the evening before.*

At 11:34 I asked what was on the Time Attack screen. At 11:40: go ahead, it's simple, we already have the base art and it only needs text. Approved at 12:12. At 12:26 I asked for the elemental icons: send me options, and use the available colors to shade and gradient inside the icons' tiny space. At 12:32: the version with shadow, approved.

![](../imagens/212-elementos.png)
*The three options for the elemental icons. I picked the middle row, symbols with a shadow.*

## FM, on hold

At 1:25 p.m. I saw the queue building the FM music variant again:

> "Why are we compiling the FM version every time? It'll still be a while until I actually implement it. When we get there, we resume the tests. For now you can disregard it."
>
> (Translated from Portuguese.)

It became a rule: the FM music code stays in the repository, but no task compiles it, measures it or uses it as a space limit until I pick it up again. That evening it already mattered: one of the assembly tests froze only in the FM variant, and the same freeze happened on the main branch without the rewrite. It went on the shelf with the FM.

At 2:40 I asked for an image conversion tool that gives any picture the same style Claude had applied to the familiars' portraits. At 2:51: is it exactly the same dither calculation you did for the familiars? Those came out so well.

## The number

72 commits, 16 messages from me in the record. More than 10 KB freed in the logic program and 700 bytes in the drawing one, without changing what the player sees.

*How this is made: I decide what the port should be, draw and pick colors, and test every build. The code, tools and measurements are written by Claude (Anthropic's AI). This post was drafted by Claude from my chat messages, the project's commit history and that day's report, and reviewed by me. The images are measurements, captures of the port, and Claude's icon options.*
