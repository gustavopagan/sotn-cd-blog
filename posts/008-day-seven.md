---
title: "Day 7: the coffin, by hand"
kicker: "Day 7 · October 24, 2026"
badge: "8"
slug: "day-7"
excerpt: "I stay up until six redesigning the save room, try Gemini for the coffin, end up pushing pixels myself, and at 2 p.m. five tasks land in one disc."
status: draft
---

[gus]
This one is a long night. My first message went out at ten past midnight and the last before a break at 5:52 a.m. In between I worked on three things at once, the music, the pause menu and the coffin in the save room.

![](../imagens/76-dia7-linha-do-tempo.png)
*October 24. The dots before six in the morning are Gus. The block of red after them is Claude, carrying on.*

## Music without gaps

[gus]
At 12:28 a.m. I'd been listening to Sega CD soundtracks and noticed some games play audio files through the Mega CD's sound chip. Could that give us the original soundtrack without the music stopping between rooms? Loads are short, two seconds at most. A two-second buffer might be enough.

I was specific about what I didn't want. Silence is better than a song that jumps to a different part. When the drive is done loading, the music has to continue exactly where the buffer ended. Then, while we talked it through, I worked out the catch myself. If the sound chip is busy streaming the music, who plays the sound effects?

![](../imagens/77-som-dois-modos.png)
*The trade, schematically. The sound chip can't do both jobs.*

At 12:57 a.m. I said it out loud. The best way out is still rewriting the music for the Mega Drive's FM chip and keeping the Mega CD's sample chip for all the effects. We tested the stream anyway. At 3:46 a.m., after seeing how few channels were left for effects in that mode, I wrote this.

> "Are we really that limited for sound effects?? That's a huge problem."
>
> (Translated from Portuguese.)

## A new coffin

[gus]
The save room has a coffin, and at 3:41 a.m., after looking at the original again, I decided how ours would be.

> "No, the original save coffin is really ugly. Let's go with pixel art."
>
> (Translated from Portuguese.)

## Pixel art, three ways

[claude]
I drew a first coffin that opens and closes. He said it had come out too different from the model, with too few details. The second was much better, but the inside was flat. It needed buttoned velvet, with more shading so it looks padded.

![](../imagens/72-caixao-v1-v3.png)
*On top, the first pixel-art coffin. At the bottom, the third, with the buttoned velvet Gus asked for.*

[gus]
At 4 a.m. I made one myself that I thought looked good. I also tried Gemini. My first attempt, a video of Alucard lying down in the coffin, modernized everything. Later it drew the first poses of him lying down well, and I asked Claude to fix the proportions of three where Alucard grew taller with each frame, using one of his own sprites, laid down, as the reference.

Then I described the whole sequence. Alucard walks in. Press up and the coffin opens, with the save menu. Choose to save and he jumps; at the top of the jump he changes pose and floats down into the coffin, which closes.

![](../imagens/71-save-isometrico.gif)
*The first assembled sequence, a preview Claude rendered that morning. Note the coffin's angle.*

At 10:59 a.m., back at it, I saw the problem. The coffin was drawn in an isometric view that doesn't match the room's perspective. From where the camera is, you should only see its side.

[claude]
I redrew it from the side, reusing the lid animation.

![](../imagens/74-caixao-lateral.png)
*The side view, opening and closing, on a green background for checking.*

[gus]
At 11:32 a.m. I changed the effect of the descent. Instead of after-images, it gets the same treatment as the relics, a blinking white outline on Alucard and white particles floating from his body until the lid closes. Twenty minutes later I sent Claude a sheet I had put together myself showing exactly how I wanted it. Alucard comes down in slow motion, as if floating, switching to the next pose at certain heights, with the outline disappearing on the third pose.

![](../imagens/73-caixao-descida.png)
*The descent, keyframe by keyframe, in the save room. Outline and particles, no after-images.*

One more rule at 12:29 p.m. Choosing not to save still restores HP and MP.

When the coffin went into the game, it had too few colors; the conversion didn't translate it well. I asked for options that used the save room's palette and the colors normally reserved for enemies, since no enemy will ever appear there. At 2 p.m. I picked the fifth option.

![](../imagens/75-caixao-paletas.png)
*Some of the color options, inside the room. Labels in Portuguese.*

## The menu I drew

[gus]
At 2:26 a.m., in another chat, I asked for the pause menu to open with Start during gameplay, using a design I attached, but keeping the original game's fonts. At 12:30 p.m. I asked to reuse the menu's dialog boxes for the item and enemy name notices, instead of the plain white box from two days earlier. The pause menu deserves its own post, and will get one.

## Black trees

[gus]
At 12:33 p.m. I found a problem in the opening. The trees in the forest had a black background that covered the scenery behind them. Claude suggested options. At 1:44 p.m. I settled it. Just remove the background behind the trees and leave it black.

## The first big merge

[gus]
At 2:04 p.m. I asked every chat to put its finished work in a folder called "build final". At 2:22 p.m. I opened a new chat with one job, to find those folders and add everything to the main build.

[claude]
Between 2:36 and 2:39 p.m. it did.

![](../imagens/78-soma-24-10.png)
*Five tasks, one disc. The streamed music went in switched off, as an experiment.*

## The number

[claude]
54 commits, 82 messages from him. One coffin, drawn three times.

Tomorrow is Sunday, with fewer messages.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The coffin images are previews Claude rendered during that work. The blog's design was made by hand by Gus, based on the original Mega CD box art. Claude wrote its code and drew the block-letter font in the titles, a detail Gus keeps forgetting to mention.*
