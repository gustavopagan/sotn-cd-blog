---
title: "Day 10: cleaning up the mess"
kicker: "Day 10 · October 27, 2026"
badge: "11"
slug: "day-10"
excerpt: "Every compressor in the book gets measured on the whole castle, the sprites still flicker, and after a week of six chats at once I stop everything to take inventory."
status: draft
---

A week of parallel chats had produced a lot of work and a lot of confusion. October 27 is the day I started cleaning it up. The chat I opened for that has the title "ARRUMANDO A BAGUNÇA", which is Portuguese for exactly what you'd guess.

![](../imagens/95-dia10-linha-do-tempo.png)
*October 27. The commits before dawn are the compression measurements; the messages after 4 p.m. are the cleanup.*

## Squeezing the castle

Overnight, the optimization chat I had opened the day before measured something no one had measured yet: how much every piece of the castle shrinks with each compression format, and how long each one takes to unpack. It ran all the data of all sixteen areas through five formats.

![](../imagens/96-compressao.png)
*The biggest category, every object frame in the game. The format in use took half the raw size; the best one took about a third.*

Smaller data also means more rooms fit in each group of rooms kept in memory, and fewer groups means fewer pauses to read the CD. With the smallest format, the whole castle went from 153 groups to 134.

The catch is time. The smallest formats are slower to unpack, and some things get unpacked in the middle of gameplay. At 8:14 a.m. I told Claude to go ahead with one of the candidates; by noon it had become the only format in the game; and at 2:51 p.m. part of that was undone. Whatever gets unpacked mid-game, like enemy frames and Alucard himself, went back to the faster format. The smaller one stayed for loading.

## Flicker

At 1:46 p.m. I wrote that with one warg and two zombies on screen, the sprites blinked. At 4:22 p.m. the game was much more fluid, but with Alucard, a warg and two zombies at the same height, there was a lot of flicker. That's the sixteen-sprites-per-line limit again, and the rotation that makes the leftover sprite blink instead of disappearing. It was the safety net working as designed, and it still looked bad.

![](../imagens/99-espada-2710.gif)
*Alucard swinging the prologue sword in the first room, in the 2:51 p.m. build rebuilt from that commit.*

![](../imagens/98-sala0-20-x-27-a.png)
![](../imagens/98-sala0-20-x-27-b.png)
*The first room a week apart. First: October 20, colors rounded one by one. Then: October 27, with the area's color plan. Not the same spot: the starting position changed between builds.*

## Inventory, nothing else

At 4:27 p.m. I opened a new chat with a single instruction: "Don't develop anything. Just make an inventory of the documents in this Claude project." (Translated from Portuguese.) Then I sent the same opening prompt to every chat that might have something pending, collected their answers, and pasted them back, part by part.

Some answers surprised me. At 6:16 p.m. I asked whether we could switch the music to streaming from the CD. In my memory that was what we had decided, since the buffer test had played without interruptions. Three days earlier, at 12:57 a.m., I had concluded the opposite, that rewriting the songs for the FM chip was the better way. Moments like that are why the cleanup existed.

At 7:24 p.m. one loose end got tied: the 3D coffin wasn't going away. I'll use it in some save rooms; I just haven't decided which.

## Too many codes

At 11:50 p.m. I wrote what had been bothering me all week: the chat names and the way Claude names everything automatically. There were many codes, and I still didn't understand the naming.

![](../imagens/97-codigos.png)
*Each chat had been numbering its own decisions and tests. These are real codes from that week.*

Then I asked for the thing I really wanted: reorganize the entire project folder with the codes in front of the names, throw away tests that were already done and merged into the main build, and generally organize and clean. That night the project got its first audit and its first backlog, items B-001 to B-004. There are more than six hundred today.

## The number

13 commits, 15 messages from me. 153 groups of rooms became 134, and one folder became a project.

*How this is made: I decide what the port should be, draw and pick colors, and test every build. The code, tools and measurements are written by Claude (Anthropic's AI). This post was drafted by Claude from my chat messages and the project's commit history, and reviewed by me. The screenshots and GIFs come from rebuilding the port's code exactly as it was at the time shown.*
