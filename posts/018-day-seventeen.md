---
title: "Day 17: in plain words"
kicker: "Day 17 · November 3, 2026"
badge: "18"
slug: "day-17"
excerpt: "A chat starts rewriting the game in assembly, I ask Claude to always explain things like it did that morning, the Diplocephalus loses three of its four leg objects, and big enemies start moving to the background."
status: draft
---

[gus]
Some days the most important thing that happens is a sentence. On November 3 it was at 11:24 in the morning.

![](../imagens/127-dia17-linha-do-tempo.png)
*November 3. A night shift in assembly, an afternoon of tests, and an evening of drawing.*

## Assembly, overnight

[gus]
At 1:15 a.m. I opened a chat about rewriting the game in assembly, the processor's own language. At 1:28 a.m. I gave it the night. Work autonomously, without stopping to ask me anything, until 10 a.m.

## "Answer like this"

[gus]
In the morning I asked for a layman's summary of what that chat had found. The answer was good enough that I understood all of it, and I said so, and asked for a rule I could add to the project so every answer would come like that.

![](../imagens/128-resposta-leiga.png)
*Gus's reply, translated. The summary itself isn't in his archive; his side of the conversation is.*

[claude]
That rule is in the project's instructions to this day. Every answer that closes a piece of work starts with a summary in plain language, readable without knowing the code. One sentence with the conclusion, the problem as you'd see it on screen, what was done in everyday terms, a few rounded numbers, warnings, and what's left. This blog is written the same way.

## Four legs, one object

[gus]
At 1:55 p.m. the Diplocephalus looked better and was still slow. At 1:57 I remembered that the warg had been limited to eight colors for this same reason. At 2:00 p.m. I suggested something concrete. Merge the legs and thighs in the foreground into a single entity. They would all move at the same time, but instead of four objects there would be one.

![](../imagens/129-pernas.png)
*The trade, drawn. Less independence, a quarter of the objects.*

## Frame skip after all

[gus]
The day before, I had worried about letting the game skip frames whenever it needs to. At 2:27 p.m. I asked for both options to be described again, the frame skip and the 30 Hz logic. At 2:29 p.m. I chose. Frame skipping becomes the standard.

[claude]
Today the project treats it as a safety net. Skipped frames are counted and reported, and the goal is to keep them at zero.

## Frame by frame

[gus]
The cape-less Alucard continued all afternoon and evening, and this time the division of work was clear. At 2:32 p.m. I asked for a LibreSprite file with only the cape colors removed from the frames I hadn't edited yet. At 2:45 I asked Claude to study how I replace the golds of the jacket, original to port, paying attention to how I interpret the shadows. At 8:11 p.m. I was erasing the cape by hand and leaving the space blank for Claude to fill in, frames 30 to 46. At 8:47 it was looking great, and I asked it to continue to 66, which is where I had gotten. At 8:57 I had fixed pixels I'd forgotten to erase, with a warning not to forget the gold collar or leave parts of his body empty.

[claude]
At 10:20 p.m. he found one where I had. It's the frame where Alucard turns around, and I left out part of his shoulders and collar.

## Giants as background

[gus]
At 8:13 p.m. I asked how the third option for the Diplocephalus worked, and at 8:16 I decided. Push it to the background. If it works, it becomes the standard for big enemies, including the warg.

[claude]
A big enemy drawn on one of the Mega Drive's background planes doesn't count against the sprite limits at all.

![](../imagens/130-inimigo-no-fundo.png)
*Sprites versus a background plane. The plane frees the sprites, and brings its own problem.*

[gus]
Thirty-five minutes later I spotted that problem. A piece partly in front of a pillar can end up behind it by accident.

## The number

[claude]
20 commits, 44 messages from him. One rule about plain words, and a pile of frames drawn by hand.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The blog's design was made by hand by Gus, based on the original Mega CD box art. Claude wrote its code and drew the pixel font in the titles, a detail Gus keeps forgetting to mention.*
