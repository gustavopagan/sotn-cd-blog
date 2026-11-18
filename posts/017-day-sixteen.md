---
title: "Day 16: the rules were too rigid"
kicker: "Day 16 · November 2, 2026"
badge: "17"
slug: "day-16"
excerpt: "I draw 47 frames of Alucard without a cape by hand, the game logic tries running at 30 Hz, the Diplocephalus becomes the first truly heavy enemy, and at 10 p.m. I tell Claude the project's rules are too timid."
status: draft
---

This is the day the project changed its philosophy, although it took until 10 p.m. to say so.

![](../imagens/125-dia16-linha-do-tempo.png)
*November 2. A long night of art, a quiet afternoon, and an evening about one enemy.*

## Frames 34 to 80

At 1:37 a.m. I wrote: I've done 34 through 80, test it on your side. Those were frames of Alucard without his cape, redrawn by hand in LibreSprite from the sheet Claude had given me the day before. Claude started writing a script to handle the rest; what I had in mind was filling in the frames between the ones I'd finished. At 2:05 a.m. I explained the goal: reducing the colossal work of redrawing everything by hand. At 2:16 a.m. I added my doubt: a script doesn't make artistic decisions, and pixel art is very symbolic. The gold sash, the buttons and the collar show up in some sprites and not in others, because the cape covers the front of his shoulders.

![](../imagens/122-sem-capa.gif)
*The cape-less sheet in progress, every frame cycling, from the project's art folder.*

At 3:00 a.m. I asked the question that tells you how much work this is: would it be ideal if I drew at least half the frames, around a hundred? At 12:59 p.m. I came back to it with the fear behind it: that's hours and hours of work, and I'm afraid of getting there and having it not work.

## Clean transitions

The map got the same treatment as the HUD the day before. At 12:46 a.m. I described what I expected when it opens: everything darkens at the same time, and the map is drawn with a dither from top to bottom, with no rough edges.

That night one chat also reported that Claude's own workspace was out of disk space. Cleaning it was risky with several chats working at once, so I ran the same cleanup script in every chat myself, one by one.

## A concession I didn't accept

At 4:52 a.m. I caught something in a report: with the full map, the music buffer would stop working. "Wait, that's a concession I did not accept." (Translated from Portuguese.) I wasn't going to trade the music away quietly.

## 30 Hz

One of the night's experiments ran the game logic at 30 updates per second instead of 60, with the screen still at 60. At 12:53 p.m. I tested it: apart from some slowdowns noticeable on a first playthrough, the lost sprites around the wargs had improved.

![](../imagens/123-diplo-60-x-30-a.png)
![](../imagens/123-diplo-60-x-30-b.png)
*The Diplocephalus room in the Marble Gallery, two recordings Claude made for the comparison. First: logic at 60 Hz. Then: logic at 30 Hz. Same frame number; the two runs drift apart, so the poses differ. Note the new HUD in the top left.*

## The first heavy enemy

The Diplocephalus is a two-headed beast made of many separate pieces, and in the evening it became the test case. At 8:19 p.m. I asked what was making it slow. Then: did it need to be built from so many separate entities? Couldn't we record its movements and rebuild them with fewer?

At 8:24 p.m. I proposed something simpler: two steps forward, spit fire, two steps back, spit fire. Would that be lighter? Two minutes later I explained why I thought so: if the logic is a fixed cycle, the sprite's tiles can be planned in advance, without depending on what the player does.

![](../imagens/126-diplo-ciclo.png)
*My proposal, drawn. A routine that never reacts can be prepared entirely ahead of time.*

The project's rules at the time didn't allow changing an enemy's behavior. At 8:27 p.m. I asked to test it anyway, and said that if it worked, the rule would have to be relaxed at the source, because we were going to hit this problem again and again. At 8:49 p.m.: rule changed. If the potential gain is big, fixing the routine is worth it. At 9:27 p.m. I explained why I kept insisting: the Diplocephalus is probably the first really heavy enemy we'd meet.

![](../imagens/124-diplo.gif)
*The Diplocephalus in the 30 Hz recording, from the same comparison.*

## 10 p.m.

Then I opened a new chat with a different kind of request. I wrote that I felt the project was too rigid in its rules, and that I wanted it to be bolder with optimizations. That chat started the rewrite of the rules this port runs on today: the PlayStation's code is a reference, not a base; enemies and bosses are rebuilt as Mega Drive objects; and changes the player would notice go into an approved plan per area instead of being forbidden.

Two minutes later, I reported a freeze: room 0, kill the warg, open the map, close it, open the menu with Start, close it with Start. Stuck.

## The number

74 commits, 86 messages from me. Forty-seven frames drawn by hand, one rulebook to rewrite.

*How this is made: I decide what the port should be, draw and pick colors, and test every build. The code, tools and measurements are written by Claude (Anthropic's AI). This post was drafted by Claude from my chat messages and the project's commit history, and reviewed by me. The images are recordings and previews Claude made during that work.*
