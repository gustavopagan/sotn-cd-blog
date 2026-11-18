---
title: "Day 14: my money bags"
kicker: "Day 14 · October 31, 2026"
badge: "15"
slug: "day-14"
excerpt: "213 commits, most of them while I slept. I redraw the money bags myself, ask for two more colors and get them, the bridge learns to wave, and the build queue has its first outage."
status: draft
---

Before going to bed on the night of the 30th, I handed out the night's work. To the music chat, at 1:07 a.m.: work on this alone until 10 a.m. if you need to; the final goal is music that continues across rooms, with the sound effects. To the menu chat, at 1:13: full autonomy to optimize the menu until it's completely fluid and functional. Then I went to sleep.

![](../imagens/113-dia14-linha-do-tempo.png)
*October 31. The wall of red before 5 a.m. is the night shift, several chats committing at once. 213 commits in one day.*

## Remembering why

One of the chats I left working was the color chat for the Castle Entrance. At 1:14 a.m. I asked where we had left it, and six minutes later I remembered myself: we had stopped at the warg because it took too much space, and the only solution at the time was cutting its frames. That's why the compression chat existed in the first place.

## Testing over coffee

In the afternoon I went through the night's results, one test at a time. The menu had improved a lot: scrolling no longer redrew every text. One thing still blinked, the item where the cursor was. For the drawbridge I asked for something different: keep it fixed at one level, but shaking up and down with a lot of amplitude, picking a level where Alucard doesn't collide with it. That evening it was in, as a wave that runs along the bridge column by column.

![](../imagens/115-espada-azul.gif)
*Alucard's sword in the build from 9:39 p.m. that night. At 6:20 p.m. I had asked for the sword's trail in the darker of our blues.*

## My money bags

The color work had reached the items: money bags, hearts, candles, subweapons, food. All of them drawn with the same small set of fixed colors, so they look right in every room. At 4:49 p.m. I changed the background of Claude's preview sheet to light blue and the purple to a more vivid one, to see the sprites properly. At 5:51 p.m. I looked at the version with the shared colors and wrote that the bottom row was unacceptable.

![](../imagens/111-premios-claude.png)
*Claude's sheet that afternoon. In the bottom row, on magenta, the version with the shared colors: red bags where they should be purple and silver.*

So I redrew them. At 6:49 p.m. I pointed out that the bags in three test builds didn't match my drawing, and at 7:59 p.m. I sent my corrections to the money bags. In between, at 6:53 p.m., I set a rule: the common items need to be safe. They must be protected in any circumstance; nothing else in the game is allowed to change their colors.

![](../imagens/112-premios-meus.png)
*My sheet, same layout, with my corrections to the bags. At the bottom, the twelve shared colors everything had to fit in.*

## Twelve colors

At 7:54 p.m. I said what everyone working on those sprites already knew: some items can be done nicely, artistically, but twelve colors for everything is really hard. Could we gain one or two more?

![](../imagens/114-doze-cores.png)
*The shared palette, approximately, and the problem with it.*

At 8:05 p.m. I understood how the capes change color: it's the palette that changes, so a cape would also change the shared colors, and with them the items. At 8:11 I asked whether the capes could use fixed indices, and at 8:18 I asked for a deep search for more colors without hurting anything else. By 10 p.m. the answer was in: two of the cape's slots became fixed colors, picked by me in the comparison tool. Twelve became fourteen.

## The queue goes down

At 6:06 p.m. I asked Claude to check whether the Linux machine on my PC was online. It wasn't: the build queue from the day before had its first outage. I restarted the scheduled task myself at 6:10 p.m., and at 6:14 everything was online again.

## The number

213 commits, 60 messages from me. Two more colors, and the money bags I drew.

*How this is made: I decide what the port should be, draw and pick colors, and test every build. The code, tools and measurements are written by Claude (Anthropic's AI). This post was drafted by Claude from my chat messages and the project's commit history, and reviewed by me. The sprite sheets are working files from that day; the GIF comes from rebuilding the port's code as it was at the time shown.*
