---
title: "Day 6: the whole castle"
kicker: "Day 6 · October 23, 2026"
badge: "7"
slug: "day-6"
excerpt: "The entire castle lands on the disc overnight, I write the sentence that becomes the spine of the project, the scenery stops looking posterized, and I fix my own emulator setup."
status: draft
---

[gus]
The night before, I had decided that before fixing the colors of any enemy, I needed every room of the castle in the port, because an enemy's palette depends on the room it lives in. I told one chat to build all the scenery and ignore the mechanics. No switches, no locked doors, everything open.

[claude]
At 12:22 a.m. the disc had the whole castle.

![](../imagens/66-dia6-linha-do-tempo.png)
*October 23. The burst of red right after midnight is the castle going in, area by area.*

![](../imagens/65-marble-gallery-2310.gif)
*The Marble Gallery running in the port, rebuilt from the 6:28 p.m. code that day. The colors are still the direct conversion. That's the next problem.*

## "Let hardware shine"

[gus]
At 12:20 p.m. I wrote the sentence that, a few weeks later, became the spine of the project. Keep optimizing until we get as close to optimal as possible, don't be bound to the original code, and make whatever adaptations are needed to give the hardware a chance to shine. If the shape comes out a little different from the original, no problem. The priority is not total aesthetic fidelity.

## Cheap rotation

[claude]
Several enemies spin parts of their bodies, like the Blade's limbs, the Axe Knight's axe, the Cthulhu's fireball and the Skelerang's boomerang. The PlayStation rotates sprites for free. The Mega Drive can't, so overnight I decided, on my own, to do the rotation during the build. Each spinning part gets a set of pre-drawn angles, and the game picks the closest one.

![](../imagens/67-giro-passos.png)
*More angles look smoother and cost more memory. Claude had used 16 and 32.*

[gus]
At 2:58 p.m. I reported that the Cthulhu's fireball and the Skelerang's boomerang weren't spinning, and at 3:09 p.m. I asked whether the spins could drop to 8 steps. They don't need to be that smooth.

## Posterized

[gus]
At 1:05 a.m. I opened another chat for the scenery colors. The literal conversion was making the backgrounds look posterized. I wanted something adapted to the Mega Drive's look while keeping, as much as possible, the relationship between the colors of the background and the sprites. At 1:30 a.m. I added the constraint that makes it hard. Compute each area's palettes together with that area's enemies, Alucard, and the fixed colors I had picked for the items.

![](../imagens/69-marble-ps1-x-port-a.png)
![](../imagens/69-marble-ps1-x-port-b.png)
*Marble Gallery, first room. First, the PlayStation, 75 colors. Then, the port that day, every color rounded to the nearest one the Mega Drive has.*

![](../imagens/70-marble-paleta-nova-a.png)
![](../imagens/70-marble-paleta-nova-b.png)
*Two of the experiments from that chat. First, new palettes. Then, the same with dithered gradients.*

In the afternoon I worked with a comparison viewer Claude built, with the Mega Drive version on each side and the PlayStation reference in the middle. I asked for a levels adjustment on the PlayStation image, because the Mega Drive comes out more contrasted and I needed to judge them on equal footing. I asked why the dithering always used a 50% pattern and whether it could vary. I noticed the PlayStation references themselves looked washed out and sent a corrected one to compare. At 5:23 p.m. I picked a winner from the candidates, and at 5:27 I asked for a new viewer with six versions per room, so I could choose one by one and send back a report.

![](../imagens/64-paleta-cenario-a.png)
![](../imagens/64-paleta-cenario-b.png)
![](../imagens/64-paleta-cenario-c.png)
*Another room, from the Colosseum. First, the PlayStation. Next, the direct conversion. Then, a palette planned for the whole area, sharing colors with its enemies.*

## Fixing my emulator

[gus]
Testing was slow, and not because of the port. Every boot went through the Sega and Mega CD logos, and fast-forward didn't work on the emulator I was using. So I switched to RetroArch, and spent an hour of the afternoon with Claude making a test disc open with a double click, closing the terminal window afterwards, setting the window to 3x, the d-pad to WASD, and putting the six buttons back where they belong after they got scrambled.

## The number

[claude]
71 commits, 97 messages from him. One whole castle, and the first scenery in planned colors.

Tomorrow, the coffin, redrawn as pixel art.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The screenshots and GIFs come from rebuilding the port's code exactly as it was at the time shown. The blog's design was made by hand by Gus, based on the original Mega CD box art, and Claude wrote its code.*
