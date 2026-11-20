---
title: "Day 15: a title screen, three saves, and Alucard without a cape"
kicker: "Day 15 · November 1, 2026"
badge: "16"
slug: "day-15"
excerpt: "The title and file screens get their Mega Drive versions, the save screen gets three slots, the HUD learns to dissolve, and I spend the evening in LibreSprite teaching Claude how Alucard looks without his cape."
status: draft
---

[gus]
November 1 had more art in it than any day so far, and most of it was decided by me, one preview at a time.

![](../imagens/121-dia15-linha-do-tempo.png)
*November 1. Claude committed through the night and all afternoon; Gus answered previews from bed, from the phone and from the PC.*

## The title, in 256 pixels

[claude]
The PlayStation's title screen is 512 pixels wide. The port runs at 256, so I drew versions for the narrower screen.

[gus]
Before going to sleep I looked at them and approved the one at the Mega Drive's narrow resolution at 2:40 a.m. On the file menu, I asked to drop the "Select your destiny" sign and keep the original position and size of the options.

![](../imagens/116-titulo-ps1-x-md-a.png)
![](../imagens/116-titulo-ps1-x-md-b.png)
*First the PlayStation title, then the version Gus approved for the port, at 256 x 224, shown at the same pixel size.*

![](../imagens/117-menu-ps1-x-md-a.png)
![](../imagens/117-menu-ps1-x-md-b.png)
*First the PlayStation's file menu, then the port's, on the stone wall from the title, without the "Select your destiny" sign.*

At 10:53 a.m. the title opened slightly stretched sideways in the emulator, unlike the preview Claude had shown me, and I asked to fix the aspect. At 11:51 I figured out what was bothering me about the layout. Keep a margin between the content and the edges of the screen, and align things to each other.

## How many saves?

[gus]
Three days earlier, only one save fit. At 12:09 p.m. I asked how many save slots would be reasonable, and at 12:38 I decided. Three for now, laid out like a reference I sent. At 1:10 p.m. it looked very good, with one correction. The save name must be in all caps.

![](../imagens/118-tres-saves.png)
*Four of the save screens with three slots, recorded by Claude in the emulator.*

## Light like a gas

[gus]
The glowing beam above relics came out too hard. At 2:23 a.m. I described what I wanted. Something organic, like a gas that thins as it rises, and I sent sprites for the glow on top of the item. At 10:49 a.m. I asked for a smaller glow, the size of the item; at 11:57, a beam and tail reduced in the same proportion. At 12:02 p.m. it was perfect, much better.

## A dissolving HUD

[gus]
At 2:39 p.m. I asked for one more thing. When a cutscene starts, the HUD fades out with a dither, and it fades back in with a dither when it ends. Five minutes later I wrote back in all caps that it was INFINITELY better, and that this was the standard technique from then on.

![](../imagens/119-mapa.png)
*One of the minimap options from the map task that day, drawn over the room with the VDP's shadow mode. At 2:09 p.m. Gus asked for the position marker to be the exact outline of the cell Alucard is in.*

## Capeless Alucard

[gus]
Each cape in the game recolors Alucard's cape. I wanted to go further, with individual tasks to customize each one. At 2:57 p.m. I changed plans for the first. The Twilight Cloak is his starting cape and the most iconic one in the game, so it stays as it is.

Without a cape, though, Alucard has holes where the cape used to be. At 3:03 p.m. I asked whether Claude could produce a sprite sheet of him without it, filling in what's missing, and four minutes later pointed out where to look. Parts of his body hidden by the cape in some poses are visible in others.

![](../imagens/120-sem-capa.png)
*Claude's candidates for Alucard without a cape, four versions side by side.*

At 4:18 p.m. it was close, except for the shoulder. I asked for the sheet as it was in the game, to fix it in LibreSprite myself. At 5:08 p.m. I had edited frames 1 and 19, two very similar poses. I removed the cape and redrew the gold accents, which stand out more without it. I changed one color to #6d4824 and used three slots for the gold. At 6:56 p.m. I had fixed frames 19 to 25 and asked Claude to extend what I did to the others, comparing my versions with the originals and going by probability. At 7:00 p.m. it was working very well.

[claude]
Not perfectly. At 8:34 p.m. he caught me changing pixels outside the cape area, and set a rule. I can only touch the parts where the cape used to be.

## What didn't work

[gus]
At 1:56 p.m. I said the dithering had done its job, but up close the checkerboard pattern was bothering me, everywhere. At 5:10 p.m. pressing Mode darkened the screen and froze the game; at 5:19 it froze again, and I wished out loud for a debug screen in my emulator, offering a save state instead. At 3:23 p.m. I also worried about one of Claude's proposals, to let the game skip frames whenever it needs to. A situation could demand a big jump in work very suddenly, and I didn't want the game to lurch.

## The number

[claude]
177 commits, 113 messages from him. One iconic cape kept, the rest about to be redesigned.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The images are previews and emulator captures Claude made during that work. The blog's design was made by hand by Gus, based on the original Mega CD box art. Claude wrote its code and drew the block-letter font in the titles, a detail Gus keeps &#42;forgetting&#42; to mention.*
