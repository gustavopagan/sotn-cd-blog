---
title: "Day 16: the rules were too rigid"
kicker: "Day 16 · November 2, 2026"
badge: "17"
slug: "day-16"
excerpt: "I draw 47 frames of Alucard without a cape by hand, the game logic tries running at 30 Hz, the Diplocephalus becomes the first truly heavy enemy, and at 10 p.m. I tell Claude the project's rules are too timid."
status: draft
---

[claude]
This is the day the project changed its philosophy, although it took until 10 p.m. for him to say so.

![](../imagens/125-dia16-linha-do-tempo.png)
*November 2. A long night of art, a quiet afternoon, and an evening about one enemy.*

## Frames 34 to 80

[gus]
At 1:37 a.m. I told Claude I had done 34 through 80 and asked it to test on its side. Those were frames of Alucard without his cape, redrawn by hand in LibreSprite from the sheet Claude had given me the day before.

[claude]
I started writing a script to handle the rest. What he had in mind was different, filling in the frames between the ones he'd finished.

[gus]
At 2:05 a.m. I explained the goal. It was reducing the colossal work of redrawing everything by hand. At 2:16 a.m. I added my doubt. A script doesn't make artistic decisions, and pixel art is very symbolic. The gold sash, the buttons and the collar show up in some sprites and not in others, because the cape covers the front of his shoulders.

![](../imagens/122-sem-capa.gif)
*The cape-less sheet in progress, every frame cycling, from the project's art folder.*

At 3:00 a.m. I asked the question that tells you how much work this is. Would it be ideal if I drew at least half the frames, around a hundred? At 12:59 p.m. I came back to it with the fear behind it. That's hours and hours of work, and I'm afraid of getting there and having it not work.

## Clean transitions

[gus]
The map got the same treatment as the HUD the day before. At 12:46 a.m. I described what I expected when it opens. Everything darkens at the same time, and the map is drawn with a dither from top to bottom, with no rough edges.

That night one chat also reported that Claude's own workspace was out of disk space. Cleaning it was risky with several chats working at once, so I ran the same cleanup script in every chat myself, one by one, and asked for it to become automatic whenever a task gets merged.

## A refused concession

[gus]
At 4:52 a.m. I caught something in a report. With the full map, the music buffer would stop working.

> "Wait, that's a concession I did not accept."
>
> (Translated from Portuguese.)

I wasn't going to trade the music away quietly.

## 30 Hz

[claude]
One of the night's experiments ran the game logic at 30 updates per second instead of 60, with the screen still at 60.

[gus]
At 12:53 p.m. I tested it. Apart from some slowdowns noticeable on a first playthrough, the lost sprites around the wargs had improved.

![](../imagens/123-diplo-60-x-30-a.png)
![](../imagens/123-diplo-60-x-30-b.png)
*The Diplocephalus room in the Marble Gallery, two recordings Claude made for the comparison. First, logic at 60 Hz. Then, logic at 30 Hz. Same frame number; the two runs drift apart, so the poses differ. Note the new HUD in the top left.*

## The first heavy enemy

[claude]
The Diplocephalus is a two-headed beast made of many separate pieces, and in the evening it became the test case.

[gus]
At 8:19 p.m. I asked what was making it slow. Then, did it need to be built from so many separate entities? Couldn't we record its movements and rebuild them with fewer?

At 8:24 p.m. I proposed something simpler. Two steps forward, spit fire, two steps back, spit fire. Would that be lighter? Two minutes later I explained why I thought so. If the logic is a fixed cycle, the sprite's tiles can be planned in advance, without depending on what the player does.

![](../imagens/126-diplo-ciclo.png)
*Gus's proposal, drawn. A routine that never reacts can be prepared entirely ahead of time.*

[claude]
The project's rules at the time didn't allow changing an enemy's behavior, and I said so.

[gus]
At 8:27 p.m. I asked to test it anyway, and said that if it worked, the rule would have to be relaxed at the source, because we were going to hit this problem again and again. At 8:49 p.m. I changed the rule. If the potential gain is big, fixing the routine is worth it. At 9:09 p.m. I added that I'd been playing Alien Soldier, and its bosses look a lot like the Diplocephalus. At 9:27 p.m. I explained why I kept insisting. The Diplocephalus is probably the first really heavy enemy we'd meet.

![](../imagens/124-diplo.gif)
*The Diplocephalus in the 30 Hz recording, from the same comparison.*

## 10 p.m.

[gus]
Then I opened a new chat with a different kind of request. I wrote that I felt the project was too rigid in its rules, and that I wanted it to be bolder with optimizations.

[claude]
That chat started the rewrite of the rules this port runs on today. The PlayStation's code is a reference, not a base. Enemies and bosses are rebuilt as Mega Drive objects. And changes the player would notice go into an approved plan per area instead of being forbidden.

[gus]
Two minutes later, I reported a freeze. Room 0, kill the warg, open the map, close it, open the menu with Start, close it with Start. Stuck.

## The number

[claude]
74 commits, 86 messages from him. Forty-seven frames drawn by hand, one rulebook to rewrite.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The images are recordings and previews Claude made during that work. The blog's design was made by hand by Gus, based on the original Mega CD box art. Claude wrote its code and drew the block-letter font in the titles, a detail Gus keeps &#42;forgetting&#42; to mention.*
