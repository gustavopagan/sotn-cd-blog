---
title: "Day 27: Zero stutters"
kicker: "Day 27 · November 13, 2026"
badge: "28"
slug: "day-27"
excerpt: "I ask for zero stutters, zero slowdown and zero missing sprites, and by morning the Castle Entrance skips a ninth of the frames it used to. I also start taking Alucard's cape off with help from AI, and direct a video that refuses to show blood."
status: draft
---

[gus]
At 12:02 a.m. on November 13 the giants were merging into the main branch. I told the performance chat it was its turn now, and at 12:10 I said what I wanted.

> "I want maximum performance in the game, perfect smoothness and no loss in the sprites. Zero stutters, zero slowdown and zero sprite cuts."
>
> (Translated from Portuguese.)

![](../imagens/187-dia27-linha-do-tempo.png)
*November 13. The block before dawn is that request being worked on while Gus slept.*

## The spike

[gus]
The night before, testing, I had saved a comment in the tester on one moment, writing "What was that spike? It was quite noticeable in the game." The comment saves the last 60 seconds of the processors' load, frame by frame.

![](../imagens/183-pico.png)
*The load around the moment Gus flagged, from the file his comment saved.*

[claude]
The answer was a Bloody Zombie dying. On the PS1 its death creates about 18 blood entities and 20 drawing pieces, which the port doesn't even draw. The game's logic sat at 184% for 25 frames, calculating something nobody would see. I removed it, along with the sparks of every hit, which weren't drawn either.

## By morning

[claude]
The rest of the night was the same kind of work. The enemies' drawings live on a small shelf in video memory; when it ran out of room, it emptied a big piece at once and then had to fetch back what it had thrown away. Now it works like a ring, removing only what's in the way and unused for a while, and the wargs, the biggest drawings, have a corner of their own. The game also stopped recalculating, every frame, things whose result doesn't change, like the drawing order, where the HUD goes in the sprite list, and the look-up for enemies that didn't change pose.

One finding was his to approve. When Alucard gets knocked back by a hit, the game was checking his collision with the room four times per frame, even in midair with nothing nearby, and that alone took about 40% of the logic's time. I made it check only at the start and end of the movement when the path is clear.

[gus]
At 8:24 a.m. I asked the obvious question, and asked Claude not to touch anything, just answer. If that happens with Alucard against a wall, does he go through?

[claude]
The shortcut only applies when the whole area his sensors cover is free; with a wall in reach, all four checks still run. And 178 frame-by-frame comparisons between the two versions came out identical.

[gus]
At 8:38 I wrote "Good solution!"

[claude]
Across 13 Entrance rooms and 76,000 frames, skipped frames went from 19.3 per 1,000 to 2.2. Frames where the drawing didn't fit went from 979 to 11, and frames where the logic didn't fit, from 508 to 64.

![](../imagens/188-pulados-manha.png)
*Skipped frames per 1,000. The day before, the same task had taken them from 17 to 13.7 in ten rooms.*

Part of that drop, in the giants' room, came from the giants' own task. Not zero, as he'd asked. What's left is mostly the logic during hits, and enemies taking an instant to change drawing in the mermen room.

[gus]
> "Incredible results! It doesn't apply to the whole castle yet, but we have the blueprint for that now, right? That's the most important thing."
>
> (Translated from Portuguese.)

## What's still missing

[gus]
Then I listed what worried me. The numbers were good, but three kinds of things weren't fully in the game yet. Alucard's weapons, especially special attacks like the Shield Rod or the Moon Rod; items like Heart Refresh or Power of Sire, which also have big effects on screen; and the Sword familiar, a large rotating sprite that's on screen all the time.

At 8:53 I asked which way to go. Implement every missing playable element first and optimize afterward, or open room in the resources first and implement later?

![](../imagens/184-dois-caminhos.png)
*The choice Gus put to Claude.*

At 9:03 I caught myself. "I have the feeling I've started piling tasks on top of each other in this chat." I asked for a prompt to take it elsewhere.

## Taking off the cape

[gus]
At 1:11 a.m. I had opened a separate chat about AI image tools for sprites, for my RTX 3080. By 1:19 we had a first challenge, removing Alucard's cape from his sprites, by upscaling, generating and downscaling. I knew the hard part.

> "The hardest will be the downscale, keeping the original pixels that didn't need to change, in this case every pixel that wasn't part of the cape, intact in the final product."
>
> (Translated from Portuguese.)

I had tried removing the cape with a script back on November 4, and it hadn't worked. At 1:37 I explained why. The cape has two colors of known indices, but its trim and the chest ornaments use light colors that also appear in other white areas, like the hair. "You can't just erase every pixel of color X."

At 11:11 a.m. one frame looked wrong to me. "LS100 in particular is strange. There's a set of golden pixels forming two horizontal lines that I find odd, but I could be wrong too!" At 12:58, comparing with the PS1 original, I wrote "Yes, they really seem to be the wrists! So it's working correctly." My doubt was wrong.

![](../imagens/182-ls100-a.png)
![](../imagens/182-ls100-b.png)
![](../imagens/182-ls100-c.png)
*Frame LS100, with the PS1 original first. The golden lines Gus doubted are the wrists.*

At 1:05 p.m. I explained what happens to the ornaments. They're the cape's collar and a chain that holds its ends across the chest. Without the cape they go. But maybe we could reuse the collar, recolored gold. I had started that in a LibreSprite file and pointed Claude to it. At 2:28 I proposed the method.

> "I think we can make a script with human support. Frame by frame, I click and say what's collar and should go gold, starting from the original."
>
> (Translated from Portuguese.)

![](../imagens/181-gola.png)
*Eight frames, four versions each. The original, the cape removed, the mask (magenta is cape, green is collar), and the collar recolored gold.*

## Video without bleed

[gus]
From 4:31 to 5:30 p.m. I was in another chat, directing generated video for the prologue, Dracula on his throne, line by line. Claude wrote the prompts and I corrected them. At 4:38 I asked it not to describe the character so much, because he came out with short hair and a modern beard. At 4:41 I warned that negative prompts sometimes hurt more than they help. At 4:44 I asked for much more prominent fangs.

At 5:09 I asked for the shot from the knees down. He rises, the goblet falls and breaks, and the wine spreads with the consistency of blood. At 5:14 the video tool didn't accept the blood, and at 5:15 it still flagged the prompt as harmful content. At 5:17 we swapped it for plain wine. At 5:30 the problem was that every time he stood, he turned to face the camera, when he should stay facing Richter, off screen to the right.

![](../imagens/186-storyboard.png)
*The shots of that afternoon. The video isn't shown here.*

## Phone, properly

[gus]
At 11:38 p.m. I described a problem. Every night there are tests for me from tasks I left running, and often I'm not at the computer. I connect with Moonlight and use the on-screen joypad, but the screen is too small to read the test descriptions well, and I need a mouse to navigate the tester. I asked for a plan, nothing built yet, for real access to the tester from the phone.

![](../imagens/150-moonlight.png)
*How Gus had been testing from the phone since the week before.*

## The number

[claude]
66 commits, 59 messages from him, one of them a merge prompt I wrote and he pasted. The performance work merged at 6:52 p.m.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The images are measurements from the tester, the cape pipeline's own previews, and diagrams. The blog's design was made by hand by Gus, based on the original Mega CD box art, and Claude wrote its code.*
