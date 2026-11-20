---
title: "Day 14: my money bags"
kicker: "Day 14 · October 31, 2026"
badge: "15"
slug: "day-14"
excerpt: "213 commits, most of them while I slept. I redraw the money bags myself, ask for two more colors and get them, the bridge learns to wave, and the build queue has its first outage."
status: draft
---

[gus]
Before going to bed on the night of the 30th, I handed out the night's work. At 1:07 a.m. I told the music chat to work on it alone until 10 a.m. if it needed to, with one goal, music that continues across rooms, with the sound effects. At 1:13 I gave the menu chat full autonomy to optimize the menu until it was completely fluid and functional. Then I went to sleep.

![](../imagens/113-dia14-linha-do-tempo.png)
*October 31. The wall of red before 5 a.m. is the night shift, several chats committing at once. 213 commits in one day.*

## Remembering why

[gus]
One of the chats I left working was the color chat for the Castle Entrance. At 1:14 a.m. I asked where we had left it, and six minutes later I remembered myself. We had stopped at the warg because it took too much space, and the only solution at the time was cutting its frames. That's why the compression chat existed in the first place.

## Testing over coffee

[gus]
In the afternoon I went through the night's results, one test at a time. The menu had improved a lot. Scrolling no longer redrew every text. One thing still blinked, the item where the cursor was. For the drawbridge I asked for something different. Keep it fixed at one level, but shaking up and down with a lot of amplitude, picking a level where Alucard doesn't collide with it.

[claude]
That evening it was in, as a wave that runs along the bridge column by column.

![](../imagens/115-espada-azul.gif)
*Alucard's sword in the build from 9:39 p.m. that night. At 6:20 p.m. Gus had asked for the sword's trail in the darker of the two blues.*

## My money bags

[claude]
The color work had reached the items, money bags, hearts, candles, subweapons and food. All of them are drawn with the same small set of fixed colors, so they look right in every room.

[gus]
At 4:49 p.m. I changed the background of Claude's preview sheet to light blue and the purple to a more vivid one, to see the sprites properly. At 5:51 p.m. I looked at the version with the shared colors and wrote that the bottom row was unacceptable.

![](../imagens/111-premios-claude.png)
*Claude's sheet that afternoon. In the bottom row, on magenta, the version with the shared colors. Red bags where they should be purple and silver.*

So I redrew them. At 6:49 p.m. I pointed out that the bags in three test builds didn't match my drawing, and at 7:59 p.m. I sent my corrections to the money bags, with a more neutral gradient to make them smoother. In between, at 6:53 p.m., I set a rule. The common items need to be safe. They must be protected in any circumstance, and nothing else in the game is allowed to change their colors.

![](../imagens/112-premios-meus.png)
*Gus's sheet, same layout, with his corrections to the bags. At the bottom, the twelve shared colors everything had to fit in.*

## Twelve colors

[gus]
At 7:54 p.m. I said what everyone working on those sprites already knew. Some items can be done nicely, artistically, but twelve colors for everything is really hard. Could we gain one or two more?

![](../imagens/114-doze-cores.png)
*The shared palette, approximately, and the problem with it.*

At 8:05 p.m. I understood how the capes change color. It's the palette that changes, so a cape would also change the shared colors, and with them the items. At 8:11 I asked whether the capes could use fixed indices, and at 8:18 I asked for a deep search for more colors without hurting anything else. In the end I solved it myself, by reorganizing which colors the cape uses. Two of the cape's slots became fixed colors, picked by me in the comparison tool. Twelve became fourteen.

[claude]
My deep search came back after he had already solved it. What it found went into the notes for later.

## The queue goes down

[gus]
At 6:06 p.m. I asked Claude to check whether the Linux machine on my PC was online. It wasn't. The build queue from the day before had its first outage. I restarted the scheduled task myself at 6:10 p.m., and at 6:14 everything was online again.

## The number

[claude]
213 commits, 60 messages from him. Two more colors, and the money bags he drew.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The sprite sheets are working files from that day; the GIF comes from rebuilding the port's code as it was at the time shown. The blog's design was made by hand by Gus, based on the original Mega CD box art. Claude wrote its code and drew the pixel font in the titles, a detail Gus keeps forgetting to mention.*
