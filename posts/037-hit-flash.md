---
title: "Flashing without new colors"
kicker: "Front · Hit flash"
badge: "37"
slug: "hit-flash"
excerpt: "On the PlayStation an enemy you hit changes its whole palette every frame. The Mega Drive can't afford that, so we borrowed a trick from Castlevania Bloodlines and pushed it further."
status: draft
---

## A flash I never noticed

[gus]
I was testing the subweapons front with the axe when I noticed that the damage feedback was very different from the original. I had never paid attention to the original effect before! And it woke up in me the wish to do something like it on the Mega CD, even knowing there would be difficulties. That kind of adaptation is what gives the port its flavor.

On November 19, at 2:04 p.m., I recorded the same moments on both consoles in the testing tool and asked Claude to compare them frame by frame.

![](../imagens/266-ps1-warg-golpe.png)
![](../imagens/271-mcd-warg-golpe-antes.png)
*The killing blow on a warg. On the PlayStation, frame by frame, the warg swaps between a red palette and a dark one, with the drawing still visible inside. On the port as it was, it just disappears and comes back.*

[claude]
I called what the PlayStation does a red and black silhouette. Gus corrected me at 2:31 p.m. Those silhouettes have drawing inside them, and it looked like a radical palette change from frame to frame. He was right. The PlayStation keeps special palettes for damage, red, dark and a rainbow one for critical hits, and the game rotates the colors inside them as it goes.

![](../imagens/267-ps1-paletas-dano.png)
*The PlayStation's damage palettes as they come off the disc, and on the right the closest colors the Mega Drive can show.*

## No one else changes color

[claude]
My first idea was to rewrite a few colors of the enemies' palette line every frame.

[gus]
When Claude said it would be easy to make the indexes walk along the palette, the first thing that came to my mind was that the Mega Drive already has very few colors, and all of them are being used at the same time by whatever is on screen. If we touch that, we touch everything at once. It seemed obvious. So I said what I didn't want to happen. No other object can change color.

That rule ended up guiding the whole front.

## A puzzle

[gus]
At 2:42 p.m. I asked something else. What if we don't change the drawing, and just give the warg's color indexes a different match in the fixed palette each frame?

Sometimes the solution is like a puzzle. We know the pieces we have and how they can fit. The problem is that here I usually have no idea what those fits imply. I thought the information about which color each pixel of a sprite points to would be something small, probably a few bytes. But I know that's very naive math on my part. Once again, the cartridge in the ISA slot. Sometimes you pay for ignorance, and sometimes it pays off.

[claude]
On the Mega Drive, the match between a pixel's index and its color lives in the palette line the sprite uses. Rewriting the pixels in the game costs too much. What can change for free, every frame, is which of the four palette lines a sprite points to. His question was very close to the answer. I just didn't see it yet.

## Two games that already did it

[gus]
I vaguely remembered that Contra: Hard Corps had a damage effect in rainbow colors or something like that, and I decided to investigate. I had the ROM in the folder.

[claude]
I played back a tool-assisted run of Contra: Hard Corps in an emulator and captured it frame by frame. When the first boss is destroyed, the game swaps its whole palette. The red robot that comes right after cycles four tones only on its colored plates.

![](../imagens/268-contra-hc-chefe-lento.gif)
![](../imagens/269-contra-hc-robo-lento.gif)
*Contra: Hard Corps (Japanese version), from a TASVideos run played back in Gens, slowed down. The first boss blowing up, and the robot taking shots.*

[gus]
Then I remembered Castlevania: Bloodlines too. The zombie wolf boss in stage 1-5 has it, and the skeleton in 1-7, and others through the game.

[claude]
That one was the answer. Reading the sprite table in the emulator, frame by frame, the wolf's sprites go through palette lines 3, 2, 1 and 0, one per frame, while the palette itself never changes. Bloodlines doesn't touch a single color. It just switches which line the sprite reads from.

![](../imagens/270-bloodlines-lobo-lento.gif)
*Castlevania: Bloodlines (USA), the stage 1-5 wolf getting hit, slowed down. Same palette, four different lines.*

## Further than Bloodlines

[claude]
Done raw, it didn't work in our rooms. In the dark corridor, two of the room's lines are mostly black and the warg disappears in them.

![](../imagens/273-ciclo-cru-corredor.png)
*The warg in the four palette lines, without any preparation, in the corridor with the light still off.*

[gus]
At 7:34 p.m. I picked the second of Claude's options, the Bloodlines trick with colors prepared for each room. Then I wrote "but wait", and asked for something more.

> "Could we start from the Bloodlines effect and go further? I understand we'll have to make concessions in a lot of places in this game, but I'd be happy to at least have a standard damage feedback and a critical one that cover these styles of effect. Here we even have some control, because we know which enemies will be in which places."
>
> (Translated from Portuguese.)

[claude]
That turned it into a job for the build. The converter reorders the colors of each room according to the enemies in it, so that when an enemy switches lines, one line gives a dark version of it, another a light one, and the line of colors that never change gives the strong colors. Two effects came out of it. The standard hit goes normal, dark, normal, light. The critical one is shorter and brighter.

[gus]
The critical needed to be more rainbow. When I saw the palettes, I felt there was too little difference between the normal hit and the critical one, which on the PlayStation goes through a sequence of vibrant rainbow colors.

[claude]
On the way I made one mistake worth telling. The corridor seemed full of free colors, all black, so I used them. Gus pointed out that the light was still off, and it turns on halfway down the corridor. Those blacks were the lamps, waiting.

![](../imagens/276-previa-pisca-padrao.png)
![](../imagens/277-previa-pisca-critico.png)
*The approved preview, at the game's real speed. The standard hit and the critical one.*

## Sixty a second

[gus]
The previews were GIFs, and something looked off. I didn't know GIFs top out at 50 frames per second until Claude told me, and that was making the preview janky. I wanted to see it at 60 to be sure of how it would look in the game. Claude first made me a video at 60 frames per second, and then switched to animated PNG, which is the format of every animation on this blog since.

At 10:56 p.m. I approved it.

## Strange at first

[claude]
That night the effect went into the game itself, and Gus approved the three tests at 1:13 a.m. on November 20.

![](../imagens/271-mcd-warg-golpe-antes.png)
![](../imagens/272-mcd-warg-golpe-padrao.png)
*The same hit on the same warg, in the game. Before, it disappears. After, normal, dark, normal, light.*

[gus]
Testing it in the game, I felt a bit odd at first, even though it was exactly as planned. I think it's because I'd been playing for almost a month without it. Lately I even find it strange when I play the original. Now, after a while with the new feedback, there are still fronts that haven't been merged with it, and it looks strange to me to see how it was before. Humans may be creatures of habit, but we also get used to change pretty easily.

## The number that broke

[gus]
Four minutes after approving, I noticed the damage number was scrambled. I asked whether it came from this front or was already like that in the main build.

![](../imagens/274-numero-dano-embaralhado.png)
*"124" showing up as "1_42", frame by frame.*

[claude]
It was this front, but the bug was old and had been hiding. The routine that assembles the number found where each line of its drawing ended by looking at memory addresses. The flash added 34 bytes, everything after it moved by two, and the number came out shuffled. I fixed it by counting the bytes of each line. Then I gave Gus a wrong answer from memory about what it would cost to make the whole build respect memory alignment. Measured, it was a few dozen bytes.

![](../imagens/275-numero-dano-corrigido.png)
*The same number after the fix.*

## What's next

[gus]
The warg's silhouette when it dies and the colors of the Bone Scimitars were things I noticed in the same test where I noticed the damage feedback. It just happened that I picked this one to attack first.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The screenshots and GIFs come from rebuilding the port's code exactly as it was at the time shown. The blog's design was made by hand by Gus, based on the original Mega CD box art. Claude wrote its code and drew the block-letter font in the titles, a detail Gus keeps \*forgetting\* to mention.*
