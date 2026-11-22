---
title: "Speech balloons"
kicker: "Death scene · Part 3 of 4"
badge: "35"
slug: "death-balloons"
excerpt: "The PlayStation's see-through dialog box with portraits can't be done on a Mega Drive. A Comix Zone placeholder grew on me, then turned into a balloon that waits for the voice."
status: draft
---

## A silent scene

[claude]
On the PlayStation the conversation with Death runs in a blue, see-through box at the bottom of the screen, with a portrait of whoever is talking, a name, the text typed letter by letter and a recorded voice. The box and the portraits are polygons and picture copies the port doesn't draw. When the scene first ran on the Mega CD, on October 22, you heard the voices and read nothing.

![](../imagens/250-ps1-caixa-dialogo.png)
*The PlayStation's dialog box, with Death's portrait.*

## Like Comix Zone

[gus]
The original has transparency in its text windows, and a portrait of the character. Not having transparency is already a compromise. Portraits squeezed into whatever palette is free, I could see that being too hard a pill to swallow. On top of that, the screen resolution is lower, so the portraits would look more pixelated and the text would be cramped in the boxes.

So at 3:08 p.m. that day I asked if Claude could do speech balloons like in Comix Zone, if I gave it a dump of the game. Later I told it to use the Comix Zone font too, so it would match the balloon.

![](../imagens/251-comix-zone-balao-a.png)
![](../imagens/251-comix-zone-balao-b.png)
*Comix Zone (1995), from Gus's own cartridge dump. The balloons that started it.*

[claude]
I didn't have the font as a file, so I cut it out of the game itself, running in an emulator. Each letter got the shape that came up most often across the screenshots. The logic processor draws the balloon, and the drawing processor puts it in front of everything as sprites.

## Who's talking to whom

[gus]
It worked, and I had three notes. The balloon can't cover the speaker's face, and it has to follow the sprite as it moves. When someone talks in a direction, the balloon shows it, so Alucard's balloon should sit a little to the right of his head, with the tail pointing back at him. And the balloons should come in half a second late.

[claude]
I measured where each face and the top of each head were in the emulator and made the balloon point toward whoever is listening. On the way I found a bug of mine. A balloon that didn't fit in its tiles stayed on screen walking along with Death, and the loop that kept retrying could freeze the logic processor.

![](../imagens/252-baloes-2210-centrado.png)
![](../imagens/253-baloes-2210-apontando.png)
*October 22. At 7:23 p.m. the balloon sits centered over Death's head. At 9:41 p.m. it stays clear of the face and points at the speaker. The two discs don't run in sync.*

[gus]
At 9:40 p.m. I told Claude it was REALLY cool and to put it in the main build.

## Our own balloon

[gus]
The Comix Zone idea was more of a placeholder than a final answer, but as time went by it grew on me. On November 1 I still wanted to change the style. The balloon was white, with the face of Comix Zone, and I wanted it to have the face of our port. The same style as the item and enemy name notices, with rounded corners, and the game's own font. I asked to see a preview before the build.

Out of Claude's previews I picked the one with the black border on the left. Cutscenes are scripted and controlled, so there's no problem using the resources we have.

[claude]
The balloon took the frame of the item notice, rounded the corners, drew the tail with the same frame and switched to the font of the game's menu. Dropping the Comix Zone font also freed 1,340 bytes on the logic processor.

## Wait for the voice

[gus]
At 1:46 p.m. I said the balloons were coming in a little early, and asked if Claude could find the moment the audio starts making voice and sync them to it.

[claude]
The logic processor now asks the Mega CD's system software whether the drive is playing. The balloon comes in when a new line has been requested and the drive is playing, or after three seconds if it never starts. Before, in three of the five lines, the balloon showed up 41 to 46 frames before the voice. After, it shows up 1 to 7 frames before.

![](../imagens/254-baloes-0111-janela.png)
![](../imagens/255-md-balao-hoje.png)
*The balloon in the style of the game's own windows. Left, the November 1 merge, rebuilt from that commit. Right, the port today.*

[gus]
It's there for now, but I'm still going to try the dialog box with the text.

## Still open

[claude]
Two things came later. In mid-November the text in notices and balloons started being drawn five letters per frame and turned into tiles in the drawing processor's spare time, because Gus noticed a hitch whenever a notice that hadn't been loaded yet appeared. He also redrew the menu font himself, which is the font the balloons use. And one bug is still open. Death loses the lower half of its body while a balloon is open.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The screenshots and GIFs come from rebuilding the port's code exactly as it was at the time shown. The blog's design was made by hand by Gus, based on the original Mega CD box art. Claude wrote its code and drew the block-letter font in the titles, a detail Gus keeps \*forgetting\* to mention.*
