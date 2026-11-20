---
title: "Day 4: Alucard has no reflection"
kicker: "Day 4 · October 21, 2026"
badge: "5"
slug: "day-4"
excerpt: "Water borrowed from Castlevania Bloodlines, a vampire who doesn't show up in it, mermen on a strict diet, and a drawbridge that can't rotate but can shake."
status: draft
---

[gus]
At 12:24 a.m. I was away from the computer and asked Claude what it could get done before 5 a.m. By 6:30 the wolf and the mist were visible for the first time. The mist blinks at 30 frames per second, because I picked blinking over the other two options Claude offered, a shadow effect or no mist at all.

![](../imagens/44-dia4-linha-do-tempo.png)
*October 21. Two nights of work in one day, Claude's before dawn and Gus's after dinner.*

## "Accumulated gains"

[gus]
At 6:35 a.m. I noticed Claude had rewritten a small piece of the game in assembly, the processor's own language, and wrote that it should consider the accumulated gains of doing this for more things.

[claude]
Ten minutes later the loop that walks through the entities at the end of every frame was in assembly too.

![](../imagens/51-laco-asm.png)
*One loop, measured in the mermen room. Same results, frame by frame, a third cheaper.*

It took almost a month for that sentence of his to become the project's rule. Today everything new in the port is written in assembly by default, because memory runs out before speed does, and hand-written code is smaller. On October 21 it was a suggestion he made before breakfast, and I treated it as a suggestion.

By 8:30 a.m. the disc had a second area. The teleport room of the Castle Entrance now led to the Alchemy Laboratory, loaded from the same CD.

## My list, my rules

[gus]
At 1:36 p.m. I sent a list. The dying warg spawns a new smoke cloud every two frames, so cap it at three. Three mermen at a time, and pick one water-entrance effect instead of two. The red door turns in 3D on the PlayStation, and since the Mega Drive can't do that, dissolve it with dithering or something cheap. And the transformations, could the change between Alucard and the bat use a dithered blend too?

[claude]
The dissolve is the cheapest effect there is. Every step removes more pixels in a fixed pattern, so it costs a few extra tiles and no processing at all.

![](../imagens/48-pontilhado-bayer.png)
*The dissolve, drawn out. Every step removes more pixels in a fixed 4 x 4 pattern.*

![](../imagens/53-morcego-pontilhado.gif)
*Alucard turning into the bat and back in the 4:36 p.m. build, rebuilt from that commit. The dither replaces the PlayStation's wavy distortion.*

![](../imagens/81-morcego-sequencia-a.png)
![](../imagens/81-morcego-sequencia-b.png)
![](../imagens/81-morcego-sequencia-c.png)
![](../imagens/81-morcego-sequencia-d.png)
![](../imagens/81-morcego-sequencia-e.png)
![](../imagens/81-morcego-sequencia-f.png)
*The same transformation, frame by frame, every 12 frames. Alucard thins out in the 4 x 4 pattern while the bat appears.*

## Bloodlines water

[gus]
The water from the day before was still flashing the whole screen. I went looking for a Mega Drive game with water I liked, and found it in our own family, Castlevania Bloodlines. Bloodlines doesn't do transparent water. It reflects the room in it. I had Gemini summarize a video explaining the effect, sent the summary to Claude, and asked to replace Symphony's water with it.

![](../imagens/79-bloodlines-a.png)
![](../imagens/79-bloodlines-b.png)
*Castlevania Bloodlines (1994), captured from the cartridge in an emulator. The reflecting water comes later, in the second stage.*

Then I added the most important rule of the day. Alucard is half vampire, so he has no reflection.

![](../imagens/49-agua-bloodlines.png)
*How the reflection works. The scene above the line, mirrored and darkened below it. Everyone gets a reflection except Alucard.*

[claude]
The trade was also technical. Transparent water meant drawing the swimming mermen all the time. With a reflection, they only need to exist when they jump out.

[gus]
At 6:34 p.m. I asked for two more touches I remembered from Bloodlines. The water level rising and falling by a few pixels, and a very subtle ripple in the reflection. Both arrived at 7:11 p.m.

![](../imagens/55-agua-antes-depois-a.png)
![](../imagens/55-agua-antes-depois-b.png)
*The same spot, a day apart. First, the palette-swap water from October 20. Then, the Bloodlines-style water from the 7:11 p.m. build, darker and mirrored, and a red merman that got his colors back.*

![](../imagens/54-agua-bloodlines.gif)
*The mermen room in that build. Never more than three of them.*

## Gunstar detour

[gus]
In the afternoon I asked Claude to analyze how Gunstar Heroes handles its explosions and bullets, from a memory dump of the game. (I sent the wrong dump first.) The analysis made me ask an uncomfortable question. Is the Mega CD still worth it, or should we move to a cartridge? And what about the 32X? We stayed on the Mega CD, and that conversation deserves its own post.

![](../imagens/213-gunstar-a.png)
![](../imagens/213-gunstar-b.png)
*Gunstar Heroes (Treasure, 1993), captured from Gus's own cartridge dump. The title and the first stage.*

![](../imagens/85-32x.jpg)
*The 32X, the other way out Gus asked about. Photo: [Evan-Amos](https://commons.wikimedia.org/wiki/File:Sega-Genesis-32X-02.jpg), public domain, via Wikimedia Commons.*

[claude]
What came out of Gunstar right away was smaller. Room transitions now fade by darkening the palette in eight steps, which costs almost nothing.

![](../imagens/50-fade-paleta.png)
*A fade to black done entirely in the colors. Gunstar Heroes does this; now the port does too.*

## Mermen on a diet

[gus]
The mermen still weren't right at 4:40 p.m. My hunch was the entrance animations and the water effects they create, so I asked Claude to remove both splash effects for a test. At 5:02 I went further. One merman type in three colors, all with the yellow one's entrance, the red one's death, and only the fire-spitting attack. Simpler, I thought.

Claude's answer made me ask, at 5:29, whether the extra attacks and the two merman types made any difference to the processing at all. I had asked to simplify because some mermen were vanishing, and now I noticed that the one going invisible was usually the red one. What I really cared about was something else.

> "Regardless of the moment, at the room entrance or during the fight, there must be at most 3 mermen present!"
>
> (Translated from Portuguese.)

[claude]
At the time, walking into that room could put seven of them on screen.

![](../imagens/45-mermen-teto.png)
*Seven at worst, then three.*

![](../imagens/83-mermen-1910-x-2110-a.png)
![](../imagens/83-mermen-1910-x-2110-b.png)
*The mermen room two days apart, same frame of the same run. First, October 19, palettes converted directly, water still missing. Then, October 21, Bloodlines-style water and the red merman's colors restored.*

[gus]
At 6:03 p.m. I asked whether the death animations had any randomness.

[claude]
They did. The red merman's death throws six pieces and six smoke clouds with random shapes and angles.

[gus]
I asked Claude to remove the dice. With fewer pieces, I argued, each one has to be placed so it looks good, or the result can come out lopsided.

![](../imagens/46-merman-morte.png)
*The red merman's death. Six random pieces became three in a fixed, symmetric fan.*

Weeks later, going back over this with Claude, I understood my own request better. The dice cost almost nothing to roll; what weighed was the number of clouds. On the PlayStation, six random clouds work by brute force. Even if three land in a pile, there's fire left to cover the rest of the body. Cut it to three and leave them random, and sometimes they all land in one corner. In this case, randomness was a tool for haste.

> "With few resources, you start to really notice where RNG is actually an aesthetic decision."
>
> (Translated from Portuguese.)

[claude]
He also noticed that the red merman's sprite had been losing detail with each version, compared to the yellow one. The colors were being squeezed into a shared palette. I stopped squeezing them in that room.

## The drawbridge

[claude]
The game begins with Alucard running through a forest toward the castle while the drawbridge rises. That night the arrival bridge got connected, with the forest in the background and the bridge drawn from pre-rendered angles.

![](../imagens/52-ponte-prologo.gif)
*The opening run in the build from 11 p.m., rebuilt from that commit. The bridge rises in steps, and shakes.*

![](../imagens/80-ponte-angulos-a.png)
![](../imagens/80-ponte-angulos-b.png)
![](../imagens/80-ponte-angulos-c.png)
![](../imagens/80-ponte-angulos-d.png)
![](../imagens/80-ponte-angulos-e.png)
![](../imagens/80-ponte-angulos-f.png)
*Six frames of the bridge, 20 frames apart. Each angle is a picture prepared during the build; the game only picks which one to show.*

[gus]
At 10:33 p.m. I pointed out that Mega Turrican manages to rotate, or at least fake rotating, platforms and sprites, and asked if there was a documented trick to rotate the bridge. The Mega CD even has a chip for scaling and rotation.

[claude]
I did the math and said no.

![](../imagens/47-rotacao-custo.png)
*Turning the bridge once with the rotation chip would take longer than a frame, with the main processor waiting.*

[gus]
So I asked for something else, a bridge that shakes while it rises. At 11 p.m. I asked for more shaking. That's the GIF above.

## The number

[claude]
40 commits, 40 messages from him. Three mermen, no vampire reflections.

Tomorrow, the prologue gets its words.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The screenshots and GIFs come from rebuilding the port's code exactly as it was at the time shown. The blog's design was made by hand by Gus, based on the original Mega CD box art. Claude wrote its code and drew the block-letter font in the titles, a detail Gus keeps &#42;forgetting&#42; to mention.*
