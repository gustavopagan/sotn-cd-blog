---
title: "From Vectorman's snow to our rain"
kicker: "Front · Rain"
badge: "40"
slug: "rain"
excerpt: "Vectorman's blizzard costs almost nothing, so I asked how it's done. One scroll value per frame later, the castle entrance has rain in front of everything, with splashes on Alucard and the warg."
status: draft
---

## A blizzard that costs nothing

[gus]
I'm looking for a reference for the fluid that pours out when you break the big containers holding subweapons in the Alchemy Lab. That's why I've been playing games known for their graphic effects. Finding the snow was a side effect of that search.

Vectorman has a really heavy snow effect, and the game doesn't slow down. The way it's done gives a very fluid impression. The way it's spread out sometimes gives the impression that the snow reacts to the scenery. That caught my attention a lot. I asked Claude how it's made, and I put it in the testing tool so I could find the snowy stage myself.

![](../imagens/301-vectorman-nevasca.png)
*Vectorman (1995), from Gus's own cartridge dump. One second of the blizzard, at the spot Gus marked in the testing tool.*

[claude]
First I tried to follow a tool-assisted run in my emulator, and it fell out of sync. Gus found the spot for me. The answer was simpler than either of us expected. The snow is the whole back plane, 28 tiles repeated, drawn in front of the scenery. It falls 7 pixels per frame just by moving the plane's vertical scroll. The cost per frame is one write to the video chip and zero sprites.

![](../imagens/302-vectorman-plano-a.png)
![](../imagens/302-vectorman-plano-b.png)
*The two planes of the scene, pulled apart. The scenery, and the snow on its own plane. The pink is transparent.*

[gus]
I was surprised to find out it was the good old raster working as always, simply an intentional and conscious use of the effect.

[claude]
Gus calls it raster, and I'll leave his word in his part. Strictly speaking, Vectorman doesn't change anything line by line. It sets one vertical scroll value for the whole plane, once per frame.

## Watching the plane move

[gus]
Then I wanted to try different amounts of rain, on a black background, starting with a thin and sparse one. It looked really cool. I was very curious about the order in which the source plane was being printed on the screen to make the rain effect. How was the source plane being scanned? So I asked for a visual representation of the math.

![](../imagens/303-chuva-fina-mockup.png)
*The first mockup, thin and sparse rain on black, at twice the size.*

![](../imagens/304-chuva-plano-e-tela.png)
*On the left, the plane in video memory, a 256 by 256 square that wraps around. On the right, the screen. The yellow window is the part of the plane the screen shows in each frame.*

[gus]
I was really impressed by the simplicity and elegance with which this was solved back then. Such a simple tool that opens up very different visual possibilities. I told Claude this was going to be a blog post.

## Rain on everything

[claude]
Next he asked for medium rain at the start of the castle, with a warg, as a mockup. I put it behind the scenery, the way the PlayStation's rain sits in the background.

![](../imagens/305-chuva-atras-mockup.png)
![](../imagens/306-chuva-frente-mockup.png)
*Mockups. The rain behind the scenery, and the rain on top of everything.*

[gus]
That one is simple. It's raining outside, and rain gets everything wet that isn't covered. It would be weird for it to rain only on the trees. The other option never even crossed my mind. When I saw the rain only in the background, I was surprised, actually.

## Splashes

[gus]
I felt this scene needed a splash effect, sprites on top of Alucard and on the warg's back. Claude showed me a splash. It was a good sprite, but wasn't it too big, considering the rain is one pixel wide? Think of it as rain falling on Alucard and continuously splashing droplets.

![](../imagens/307-respingo-v1.png)
![](../imagens/308-respingo-v2.png)
*The first splash, and the second one with 1-pixel droplets, enlarged.*

One limitation of generative AI is how it picks the scope of the context when it solves a prompt. When I asked for splashes, it didn't consider that the splash is the consequence of a 1-pixel drop. The output was what it understood a splash to be, not the direct consequence of a splash in the context of this game. In the second prompt, when I brought that up, Claude not only understood the context but was proactive. It noticed that the drop would hit uneven surfaces that send the droplets in different directions, and it made a 45-degree variant that can be mirrored depending on which way the surface faces.

## The front

[claude]
The front opened at 12:24 a.m. on November 21. The first rain went into the Outer Wall, where the PlayStation already has rain, in the back plane with Vectorman's technique. It cost the drawing processor 0.2 points. On the way I found that the tall wall room had never had rain in the port at all, because it left the group of rooms together with its enemies.

![](../imagens/309-outer-wall-chuva.png)
*The rain in the Outer Wall, on the port.*

[gus]
Around 2 a.m. I went to sleep and told Claude to go through the whole roadmap. And I repeated that I wanted the rain in front. That was my intention from the start. It makes no sense for it to be behind, it's the outside area.

[claude]
Putting the rain in front had a price. The back plane became only rain, drawn on top. The sky moved into the holes of the wall during the build. The room left the shadow mode of the video chip, and the sprites lost their priority. My first capture had a straight cut through the middle of the clouds, because the sky repeated every 256 pixels. I mirrored the sky to hide it.

The splashes changed plans too. Instead of a table per pose built in advance, which didn't fit, the drawing processor reads in video memory the column of Alucard's and the warg's pieces to find their top edge. My splashes were invisible twice. First in the rain's colors, which vanished on the warg's light fur. Then in white from Alucard's palette, born right on his outline, white on white. Now they're born one pixel above the outline, against the sky. They cost 2.3 points of the drawing processor's time.

![](../imagens/310-sala0-sem-chuva.png)
![](../imagens/311-sala0-chuva-media.png)
*The castle entrance on the main build without rain, and with the rain in front and the splashes.*

![](../imagens/312-respingos-zoom.png)
*The splashes on the port, enlarged four times, on Alucard and on the warg.*

## Strong or medium

[gus]
At 8:33 a.m. the test went great. Then I asked for a version of our heavy rain, the one Claude made by itself, but with only the color of the Outer Wall's rain, which looked more subtle.

When I saw the Outer Wall's rain, which was a more direct translation of the original, with longer and less contrasted drops, I thought of making the rain effect consistent across the game, with the same style in the first room. But when I saw it there, I realized that rain color would only work against dark backgrounds. The brightness of the drop compared with the background is what decides whether we see it as light or dark. Simultaneous contrast creates this illusion in our brain that the drop is lighter or darker, but what actually changed was the context!

![](../imagens/313-forte-cores-outer-wall.png)
![](../imagens/314-forte-cinza-claro.png)
*The heavy rain in the Outer Wall's colors, where the drops read as dark, and in light gray.*

At 10:36 a.m. I went with the medium one after all.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and his answers to an interview, and corrected by him. The screenshots and animations come from the port's builds at the time shown, and from mockups where the caption says so. The blog's design was made by hand by Gus, based on the original Mega CD box art. Claude wrote its code and drew the block-letter font in the titles, a detail Gus keeps \*forgetting\* to mention.*
