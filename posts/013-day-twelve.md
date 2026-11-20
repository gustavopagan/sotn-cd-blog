---
title: "Day 12: one save, and a battery that died"
kicker: "Day 12 · October 29, 2026"
badge: "13"
slug: "day-12"
excerpt: "The port learns to save in the Mega CD's own memory, the pause menu stops reloading itself, two chats claim the same backlog number, and the project moves to a bigger computer."
status: draft
---

[claude]
October 29 is the day the backlog numbers started mattering, mostly because two of them collided.

![](../imagens/103-dia12-linha-do-tempo.png)
*October 29. Morning cleanup, afternoon fixes, and at the end of the night, a move.*

## A crazy question

[gus]
At 1:02 a.m. I asked what I called a crazy question. How much space is there in the Backup RAM?

[claude]
The Mega CD has a small memory inside the console where every game keeps its saves. The PlayStation version saves to a memory card. He wanted the port to save like a real Mega CD game.

![](../imagens/104-bram.png)
*The two ways of saving, side by side.*

By 12:29 p.m. the port had a provisional title with NEW GAME and CONTINUE, and loaded the save from the Backup RAM.

[gus]
At 2:05 p.m. I checked what goes into it besides HP, the saved room, the open doors, the level and the gold.

[claude]
The answer was that it covers everything; the only difference from the original is that just one save fits.

## The battery

[gus]
That night I had opened two new tasks, one for the save and one for a pause menu that was slow to respond. At 10:18 a.m. I found out something had gone wrong. My laptop's battery died in the middle of the prompt for the second one, and both tasks had ended up using the same backlog number. At 10:25 I sent the correction. The save keeps B-063, since three commits already cite it, and the menu becomes B-066. Twenty minutes later I added that the Windows clock was wrong, so Claude would have to rely on its own history to know when it lost access to the laptop.

## A self-reloading menu

[gus]
At 1:55 p.m. I was testing the menu, and it still wasn't right, especially in the relics list. Any movement of the cursor redrew the whole list.

[claude]
Half an hour later, at 2:25 p.m., the list only scrolled a whole line when the cursor left the eleven visible lines.

![](../imagens/106-menu-2910.png)
*The pause menu in the 2:25 p.m. build, rebuilt from that commit. The layout and frames follow the design Gus attached on October 24, with the original game's fonts.*

![](../imagens/107-menu-cursor.gif)
*Opening the menu and moving the cursor, same build.*

## Mike Tyson

[gus]
At 2:03 p.m. I asked Claude to explain something as if it were Mike Tyson.

[claude]
His archive keeps only his side of the conversations, so my answer is lost.

![](../imagens/105-tyson.png)
*The question survived. The answer didn't.*

## Hardware question

[gus]
At 6:55 p.m. I asked what Space Bruce meant by a tweet about games that tell you not to use the Kega emulator. His point was that they're probably exploiting the hardware in a way that emulator doesn't support. Then the bigger questions. What is our main technical difficulty with this hardware? Would the solution be rewriting the logic in assembly?

[claude]
Three weeks later, that became the project's rule.

## Moving

[gus]
At 10:47 p.m. I mentioned that I also have a desktop computer. Five minutes later I asked Claude to pause, because I was moving the project to the more powerful machine. I dragged the whole project folder to an external drive and asked if anything outside it needed copying. And at 11:04 p.m. I asked Claude to write down something it apparently still didn't know. I had stopped using BlastEm a long time before. I test on RetroArch, with the same emulator core Claude uses for its captures.

## The number

[claude]
18 commits, 46 messages from him. One save slot, one battery, one move.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The screenshots and GIFs come from rebuilding the port's code exactly as it was at the time shown. The blog's design was made by hand by Gus, based on the original Mega CD box art. Claude wrote its code and drew the pixel font in the titles, a detail Gus keeps forgetting to mention.*
