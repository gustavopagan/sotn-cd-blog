---
title: "Day 20: the title I painted"
kicker: "Day 20 · November 6, 2026"
badge: "21"
slug: "day-20"
excerpt: "The live editor gets its first real comment, I narrow the HUD myself, and the title screen borrows the Castlevania lettering and red banner from Bloodlines, repainted by hand."
status: draft
---

November 6 is the day the title screen started becoming the one I showed in an earlier post. It's also the day I started talking to Claude through my own tool.

![](../imagens/140-dia20-linha-do-tempo.png)
*November 6. Night and morning on the live editor, afternoon on the HUD, evening on the title screen.*

## The tester

At 2:15 a.m. I asked to switch the editor work to Claude Opus for a long stretch, and went to sleep at 2:17 with a "see you at 10". In the morning I tested while Claude worked; at 11:12 a.m. I apologized for playing while it tested, in case I was getting in the way. At 11:03 I had asked for a small thing I loved: the columns that show how full each line of sprites is should have their names on top. When a line saturates, they turn red on screen.

At 11:58 a.m. I described the workflow I wanted: I mark the problem in the editor, name and save a comment, and tell the responsible chat directly; it goes and reads the comment. At 12:04 p.m. I wrote the first one: "see comment test comment". It worked.

![](../imagens/135-live-editor.png)
*The editor that morning. On the right, the sprites-per-line columns I asked to have labeled.*

## A narrower HUD

At 3:34 p.m. I wrote two words in the HUD chat: "estreitei bastante", I narrowed it a lot. I had redrawn the frame myself. Then the orb: at 3:41 I asked whether PixelLab could make the liquid inside it within the game's palette and size, and asked Claude for a prompt so I could generate it there myself. At 3:50 it refused, saying the request was against policy. At 4:10 I came back with what it did give me, plus another version from a different tool that I liked. Moving particles inside the orb would be nice, but only if they were practically free. At 4:11: the orb's background transparent, and when HP drops, the white reflection stays where it is. At 4:14: remove the "HP" text and the crosshair-like lines on the edges. At 4:46 p.m. I saved my work as a layered file.

![](../imagens/139-hud-moldura.png)
*The HUD files from that day, five times larger. Left: the complete reference, with the orb full of red, the MP bar, the heart counter and the subweapon. Right: the frame alone.*

At 7:33 p.m. I noticed the new HUD cost more than the old one and asked to optimize it back to the previous numbers.

## The title

In the evening I opened a chat for the opening screens. At 5:38 p.m. I asked for the Bloodlines title screen, from the cartridge in the project folder, as layers I could edit. At 5:48, the PlayStation's background as a PNG. At 6:41 p.m. I made the decision: use the "Castlevania" lettering and the red banner from Bloodlines for Symphony.

![](../imagens/138-bloodlines-x-titulo-a.png)
![](../imagens/138-bloodlines-x-titulo-b.png)
*First: Castlevania Bloodlines' title, captured from the cartridge. Then: the port's title as it is today, with that lettering and banner, repainted.*

Then the corrections, one after another. At 7:35 p.m.: the red banner has a red glow underneath in Bloodlines; remove it and make it darker than the top. At 7:38: the "Castlevania" lettering has the same red light underneath, because in Bloodlines the whole set sits above a river of lava. Remove it too. At 7:46: it's still red; for the bottom edge of the banner, mirror the metal edge from the top. At 7:53: put the background in shadow mode, or darken its palette if that's safer.

At 11:04 p.m. I asked for the title in a format I could edit in LibreSprite. At 11:56 p.m.: done, edited and saved. That's the screen I wrote about in "What AI can't do", and the part of it I did by hand.

![](../imagens/17-logo.png)
*The lettering on the final title, enlarged. Repainted by hand from Bloodlines' red banner and logo.*

## The number

82 commits, 55 messages from me. One title screen, mine.

*How this is made: I decide what the port should be, draw and pick colors, and test every build. The code, tools and measurements are written by Claude (Anthropic's AI). This post was drafted by Claude from my chat messages and the project's commit history, and reviewed by me.*
