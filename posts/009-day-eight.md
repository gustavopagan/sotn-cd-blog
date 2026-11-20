---
title: "Day 8: Sunday colors"
kicker: "Day 8 · October 25, 2026"
badge: "9"
slug: "day-8"
excerpt: "A quieter day: an organ riff rebuilt with a sound borrowed from Sonic 3D Blast, the Castle Entrance gets its color plan, and every pickup in the castle has to fit in Alucard's palette."
status: draft
---

[claude]
Sunday. Eight commits and twenty-three messages, most of them after midnight or after dinner. It's the first day where the port mostly waited for him instead of the other way around.

![](../imagens/86-dia8-linha-do-tempo.png)
*October 25. Two short sessions, a whole day off in between.*

## A borrowed organ

[gus]
After midnight I was working on the Mega Drive version of one of the songs, in a tracker. The organ riff that opens it didn't sound right, and I had a reference in mind, the riff at the start of Rusty Ruin, Act 2, in Sonic 3D Blast. At 12:53 a.m. I asked Claude to pull that instrument's sound out of the music file I had sent, to use in place of the organ.

![](../imagens/216-sonic3d.png)
*Sonic 3D Blast, from the Director's Cut version in Gus's dumps folder. Its first zone, not Rusty Ruin.*

The riff needs several notes at once, and the Mega Drive's sound chip only has six channels. One of the instruments I was looking at played two notes from a single key, and at 12:59 a.m. I asked how.

[claude]
The answer is in how FM works. An FM instrument is built from four oscillators, and when two of them sound at frequencies in a 4 to 3 ratio, you hear two notes a fourth apart.

![](../imagens/87-fm-duas-vozes.png)
*Why one key can play two notes. The ratio between the oscillators is the interval.*

[gus]
A minute later I had the plan. List the intervals the riff uses and build one instrument for each. At 1:38 a.m. I asked for exactly that, plus an echo on the organ.

## Entrance colors

[claude]
The color work he started on the 23rd reached its first area. Each room of the Castle Entrance got a color plan calculated together with the enemies that appear in it, Alucard and the fixed item colors, instead of every color being rounded on its own.

[gus]
The first room exists twice in the game, once for each visit. At 8:09 p.m. I asked for the first-visit room to use the same color plan as the return visit's. At 8:14 p.m. the tests were done and approved, and at 8:21 the plan was in the main build.

![](../imagens/89-entrada-antes-depois-a.png)
![](../imagens/89-entrada-antes-depois-b.png)
*The opening forest, which belongs to the Castle Entrance, four days apart. First, October 21, colors rounded one by one, with the debug readout still on top and Alucard not yet on screen. Then, October 25, with the area's color plan and more depth between the rows of trees.*

![](../imagens/90-corredor-antes-depois-a.png)
![](../imagens/90-corredor-antes-depois-b.png)
*The dark hallway, same frame of the same run, three days apart. First, October 22, with the plain white text box. Then, October 25. The enemy's name now sits in a box drawn with the pause menu's frame, which Gus had asked for the day before, and the dust under Alucard's feet is dithered.*

## 1 palette, all pickups

[gus]
At 9:04 p.m. the scenery was done and the enemies of the Castle Entrance were next. Reviewing the first round, I noticed how many assets repeat between areas, items, candles, the same small things in every room. I asked for a shared set, and at 11:27 p.m. I made sure of one thing. Every collectible in the map, not just weapons and armor but hearts, money and power-ups, has to be drawn with Alucard's fixed colors as much as possible.

![](../imagens/88-itens-cores-fixas.png)
*The rule, drawn with generic shapes. One set of colors for everything you can pick up.*

Then I asked whether Claude had a better idea, and to see examples of the options before deciding. Going through them backwards, I liked the violet candles, but the glow around them needed a dither, or only the halo should shimmer, or blink at 30 Hz.

## The number

[claude]
8 commits, 23 messages. One borrowed riff, one area in its own colors.

Tomorrow, Monday, and the enemies of the Castle Entrance, one by one.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The screenshots and GIFs come from rebuilding the port's code exactly as it was at the time shown. The blog's design was made by hand by Gus, based on the original Mega CD box art, and Claude wrote its code.*
