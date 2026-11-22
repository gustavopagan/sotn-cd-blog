---
title: "Teleported by a laser"
kicker: "Death scene · Part 2 of 4"
badge: "34"
slug: "death-items"
excerpt: "Death takes Alucard's six items. On the PlayStation they stretch and fly off. On the Mega CD a column of light takes them, an idea borrowed from Sonic 3 & Knuckles, with a glow I drew myself."
status: draft
---

## What Death takes

[claude]
When Death takes Alucard's equipment, six items leave his body. On the PlayStation each one grows from its center, flies to its spot, blinks red while it waits its turn and then leaves in a stretch, pulled up and out of the screen over 24 frames. All of that is drawn with polygons that the Mega Drive doesn't have.

![](../imagens/237-itens-ps1.png)
![](../imagens/238-itens-md.png)
*The items leaving, on the PlayStation and on the port today.*

## Icons that vanish

[claude]
When the scene first ran on the port, on October 22, I put the items in as the inventory icons, standing still. No growing, no red, no stretch. When their time came they simply disappeared.

![](../imagens/239-itens-2210-icones.png)
*October 22, rebuilt from that commit. The items are plain icons, and they just vanish.*

## A column of light

[gus]
On October 31, at 11:35 p.m., I asked for three things. The items should get the effect I had asked for on relics a week earlier, a blinking 1-pixel outline and particles rising like the smoke of a campfire, only in red instead of white. Then each item should leave in a vertical column of light, as if it were being teleported by a laser, with red sides and a light pink center. One at a time.

I didn't remember how the original did it. I only remembered that the motion carried the items up in some kind of beam. That's when I thought of the animation that materializes the Super Emeralds in Sonic 3 & Knuckles, the first time Sonic jumps into a special ring in Mushroom Hill. That's where the idea came from, and it evolved from there to where it is now.

![](../imagens/246-s3k-argola.png)
![](../imagens/247-s3k-feixes.png)
*Sonic 3 & Knuckles, from Gus's own cartridge dump, played from a save with all seven emeralds. Sonic jumps into the giant ring, and in the shrine a beam of light comes down on each pedestal and leaves a Super Emerald.*

[claude]
When I recorded that scene, on November 20, Gus pointed out what he had meant all along. In Sonic the columns of light bring the emeralds. He imagined them taking the items away. The Death scene is the Sonic scene played in reverse.

My first version went in at 12:41 a.m. on November 1. A red outline blinking at 15 Hz, red vapor, and a straight column of light.

![](../imagens/240-itens-0041-coluna.png)
*November 1, 12:41 a.m. The first column of light, rebuilt from that commit.*

## What I had in mind

[gus]
It wasn't what I had in my head. At 1:40 a.m. I sent Claude a link to an animation I'd made in another chat, just to give it an idea. It was too slow and not pixel art, but the movement was right. Each item gets taken by one of the lights and thrown up the map by the beam. Not very far up, just enough to stay clear of the HUD.

![](../imagens/241-feixe-rubro-referencia.gif)
*Gus's reference, made in a browser in another chat on November 1. A red and white flash, a beam with a bright tip, and particles that fade behind it.*

[claude]
Three minutes later I had a version built from his reference. The flash and the beam, with the item riding up on the tip.

![](../imagens/242-itens-0143-feixe.png)
*November 1, 1:43 a.m. The version based on Gus's reference.*

## I drew it myself

[gus]
At 2:23 a.m. I told Claude the beam was too stiff. It had to be organic, like a gas that gets thinner the higher it goes. And for the glow on top of the item, I sent sprites.

It was easier to draw what I was thinking than to explain it. We could have stayed there playing cat and mouse, but sometimes a drawing is worth much more than a description.

![](../imagens/243-brilho-desenhado-por-gus.png)
*The eight frames of the glow, as Gus drew them, enlarged ten times. The pink is a dither of red and white.*

[claude]
I put his glow in and made the beam a gas that thins out and wavers. Then I had to make it fit. The drawing processor keeps a small cache of the shapes it's showing, and the effect didn't fit as it was. So the glow is stored as one quarter and shown as four mirrored copies, and the beam uses eight fixed frames that waver by flipping every four frames. The shape of the beam, the mirrors and the fixed frames were my calls. The request, the reference, the glow and everything that came next were his.

![](../imagens/244-itens-0227-gas.png)
*November 1, 2:27 a.m. Gus's glow and the beam as a gas.*

## The size of the item

[gus]
That morning, at 10:49, I asked for the glow to shrink to the size of the item. The item doesn't need to fly up white. It just disappears under the glow, in the frame where the glow covers it the most. At 11:57 I asked to shrink the beam and the rising tail in the same proportion. At 12:34 p.m. it was done.

> "That turned out incredible!! Really good."
>
> (Translated from Portuguese.)

![](../imagens/245-itens-1051-tamanho.png)
*November 1, 10:51 a.m. The glow the size of the item, which disappears on the glow's fourth frame.*

## The pieces that went missing

[gus]
On November 19 I noticed pieces of Death, and of the glow that takes the items, going missing during the scene.

[claude]
I made a mess of the first night on it. I blamed the whirlpool and the cache, measured in a test mode that gives the drawing processor four times the time per frame, and thought it was fixed. At normal speed it was worse. The cause turned out to be the items themselves. Each of the six was going through the drawing cache as if it were an enemy, and the glow and the vapor kept asking for new shapes that didn't fit.

The next night started with the budget sheet for the scene, which is where it should have started. It also showed two of my numbers from the night before were wrong. I had said the draw list held close to a hundred entries, and it never went above 33. The "16 items" I'd been chasing were the 16 shadows of Death's scythe. There are six items.

The fix treats the effect the way a Mega Drive game would. The 30 tiles it needs stay in video memory from the moment the items appear, and each frame the logic only says where to place each piece. One visible change was my call. The vapor became three red dots rising from each item. Before, there were around nine that almost never got drawn.

![](../imagens/248-itens-antes-2011.png)
![](../imagens/249-itens-depois-2011.png)
*November 20, before and after, lined up on the same game frame.*

The numbers, in three runs of the scene. Objects that went undrawn dropped from somewhere between 300 and 600 to between 20 and 35. Skipped frames went from 14 to 19 per thousand down to 8 to 12. Gus approved it at 2:25 a.m. and asked to merge it that morning.

[gus]
The vapor was a side effect of reusing the animation I had pictured for the relics. Since we were reusing their outline, only in red, I thought we could try the particles too.

## Borrowed by an angel

[gus]
On November 14 the same glow went to another place. When the Ophan familiar judges an enemy, I asked for the glow that takes Alucard's items, recolored. First in blue and green, then in fire colors, which felt more like the character.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The screenshots and GIFs come from rebuilding the port's code exactly as it was at the time shown. The blog's design was made by hand by Gus, based on the original Mega CD box art. Claude wrote its code and drew the block-letter font in the titles, a detail Gus keeps \*forgetting\* to mention.*
