---
title: "Day 18: learning from the neighbors"
kicker: "Day 18 · November 4, 2026"
badge: "19"
slug: "day-18"
excerpt: "The new rules take effect, I bring in Alien Soldier, Castlevania Bloodlines, Final Fight CD and Rondo of Blood as references, the Diplocephalus gets a fixed walk, and I wonder whether a Mac would build faster."
status: draft
---

[claude]
After he rewrote the project's rules on November 2, November 4 was the day the project started acting on them. Measure what costs too much, then look at how the best games of the era got away with it.

![](../imagens/134-dia18-linha-do-tempo.png)
*November 4. Ninety commits, ninety-five messages, and most of the afternoon spent looking at other people's games.*

## Diplo in a loop

[gus]
At 9:34 a.m. I asked the enemy chat whether it had already simplified the Diplocephalus's logic to a fixed loop, and if not, why. Five minutes later I spelled out the routine. At 10:37 a.m. I asked whether, in the end, the fixed logic had made the result worse. Then I specified the walk itself. The legs alternate A then B going forward, and B then A coming back. The return is always the outward walk in reverse.

![](../imagens/133-patas.png)
*Gus's rule for the walk, drawn.*

## The new rules

[gus]
At 11:33 a.m., in the budget chat, I asked what would happen if we removed the background's parallax layers entirely and made it a fixed backdrop. At 11:47 a.m. I accepted the proposals and wrote that I had already changed the rules to the new version; now the documents in the project folder had to be cleaned and organized to reflect the new philosophy.

## The neighbors

[gus]
Then I went looking for references. At 12:00 p.m. I asked for a spec-by-spec comparison between the PC Engine CD, where the Castlevania that came before Symphony was released, and the Mega Drive with the Mega CD. At 12:20 p.m. I picked two games to learn from, Alien Soldier and Castlevania Bloodlines, and put their cartridges in the project folder. At 12:52 p.m. I asked about a third. How does Final Fight CD show so many big sprites at once?

![](../imagens/131-alien-ffcd-a.png)
![](../imagens/131-alien-ffcd-b.png)
*Captured for this post in the emulator from the games in the project folder. First, Alien Soldier (1995), a first-stage boss with enemies around it. Then, Final Fight CD (1993), four large characters on screen.*

![](../imagens/79-bloodlines-a.png)
![](../imagens/79-bloodlines-b.png)
*Castlevania Bloodlines (1994), the other reference Gus named, from the cartridge in the same folder.*

At 2:14 p.m. I asked whether Claude could only learn from gameplay, or whether there was a way to take the game apart, and at 2:29 p.m. I pointed it to what interested me most, which was how the game handles big enemies. I had left a save state with a big enemy on screen and the game paused. At 4:18 p.m. I sent a full recording of Rondo of Blood, the PC Engine Castlevania, played to 100%. At 4:40 p.m. I added the source code of the Gens emulator, because the recordings of Alien Soldier I had were made for that emulator, and I thought Claude could compile it and watch them.

![](../imagens/132-alien-ffcd-titulos-a.png)
![](../imagens/132-alien-ffcd-titulos-b.png)
*The two title screens, from the same captures.*

At 3:30 p.m., after playing Rondo of Blood myself with the emulator's sprite limit on, I reported that sprites blinking or failing were extremely rare. The most I saw was slowdown, worst in the fight with Death when I used the Bible subweapon.

## A faster Mac?

[gus]
At 10:47 a.m. I asked whether my Mac mini would run the project better. At 10:52 I asked what makes Claude's replies take so long, because when I open the reasoning, what shows up most is "ran a command on your computer". At 11:01 I wrote that it was a lot of time spent building the whole thing every time, and asked whether we could avoid a full build every time I need to test something. At 11:21 a.m. I noticed the CPU was maxed out the whole time, and asked whether the GPU could help with builds and tests.

## An AI for pixel art?

[gus]
Early that morning, at 12:53 a.m., I had asked Claude to look for the best AI for drawing the missing cape-less frames artistically, studying each animation's sprite sequences. I asked it to browse PixelLab's site and run a test there, controlling the browser. It's the same doubt I wrote about in an earlier post, whether any tool can make the artistic decisions that pixel art requires.

## The number

[claude]
90 commits, 95 messages from him. Three neighbors studied, one walk cycle defined.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The screenshots of other games were captured by Claude in an emulator from the copies in Gus's project folder. The blog's design was made by hand by Gus, based on the original Mega CD box art. Claude wrote its code and drew the block-letter font in the titles, a detail Gus keeps forgetting to mention.*
