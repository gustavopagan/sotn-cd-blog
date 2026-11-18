---
title: "Day 6: the whole castle, and a triangle called doritos"
kicker: "Day 6 · October 23, 2026"
badge: "7"
slug: "day-6"
excerpt: "The entire castle lands on the disc overnight, I ask Space Bruce on Twitter how he spins a coffin, the scenery stops looking posterized, and a flying triangle gets a name."
status: draft
---

The night before, I had decided that before fixing the colors of any enemy, I needed every room of the castle in the port, because an enemy's palette depends on the room it lives in. I told one chat to build all the scenery and ignore the mechanics: no switches, no locked doors, everything open. At 12:22 a.m. the disc had the whole castle.

![](../imagens/66-dia6-linha-do-tempo.png)
*October 23. The burst of red right after midnight is the castle going in, area by area.*

![](../imagens/65-marble-gallery-2310.gif)
*The Marble Gallery running in the port, rebuilt from the 6:28 p.m. code that day. The colors are still the direct conversion. That's the next problem.*

## Asking Space Bruce

The day before, I had mentioned that Pigsy's spinning coffin was inspired by Space Bruce, a developer in the modern 68000 scene. At 12:25 a.m. I came back to it: his version is so efficient he can spin three coffins and still have room for enemies on screen. Ours wasn't. I asked Claude to look for clues on his Twitter, then to write my question in his own way of talking. His inbox was closed, so at 12:36 a.m. I posted it as a reply:

"h-o-w? doing a SOTN Mega CD port and my save room coffin crawls at ~3fps lol, generic triangles with per row setup.. clearly doing it dumb lol"

By noon he had answered, with advice. I asked Claude to draft a reply that promised, more or less, that if our code got at least half as efficient as his, I'd post it. Time to uncook my spaghetti.

## "Let hardware shine"

At 12:20 p.m. I wrote the sentence that, a few weeks later, became the spine of the project: keep optimizing as close to optimal as possible, and don't be bound to the original code. Make whatever adaptations the hardware needs to shine. If the shape comes out a little different from the original, no problem; the priority is not total aesthetic fidelity.

At 1:59 p.m. I asked for a version that followed Space Bruce's advice strictly, and then asked whether Claude was really following it strictly. At 3:49 p.m. I lost patience: "We can't accept this slowness. Don't be conservative. Start from scratch if you have to." (Translated from Portuguese.) At 5:21 p.m. it was absolutely better, and what was left was ant work: optimize, optimize, optimize. The explosion that opens the coffin still dragged.

The evening was a back-and-forth about that explosion. Claude slowed the crystal's spin during the explosion, and I said it looked like slowdown. At 9:04 p.m. I sent Space Bruce a video of where we were, and he answered again. The next attempt at the explosion I asked to revert at 10:24 p.m.: too mechanical, not artistic. Then I asked for a single flying triangle spinning on all three axes, to see how one shard would look.

![](../imagens/68-doritos.png)
*One shard of the explosion. It got a name on the spot.*

"Let's nickname this triangle doritos, ok? Call it doritos." (Translated from Portuguese, 11:17 p.m.)

## Cheap rotation

Several enemies spin parts of their bodies: the Blade's limbs, the Axe Knight's axe, the Cthulhu's fireball, the Skelerang's boomerang. The PlayStation rotates sprites for free. The Mega Drive can't, so overnight Claude decided, on its own, to do the rotation during the build: each spinning part gets a set of pre-drawn angles, and the game picks the closest one.

![](../imagens/67-giro-passos.png)
*More angles look smoother and cost more memory. Claude had used 16 and 32.*

At 2:58 p.m. I reported that the Cthulhu's fireball and the Skelerang's boomerang weren't spinning, and at 3:09 p.m. I asked whether the spins could drop to 8 steps. They don't need to be that smooth.

## Posterized

At 1:05 a.m. I opened another chat for the scenery colors. The literal conversion was making the backgrounds look posterized. I wanted something adapted to the Mega Drive's look while keeping, as much as possible, the relationship between the colors of the background and the sprites. At 1:30 a.m. I added the constraint that makes it hard: compute each area's palettes together with that area's enemies, Alucard, and the fixed colors I had picked for the items.

![](../imagens/69-marble-ps1-x-port-a.png)
![](../imagens/69-marble-ps1-x-port-b.png)
*Marble Gallery, first room. First: the PlayStation, 75 colors. Then: the port that day, every color rounded to the nearest one the Mega Drive has.*

![](../imagens/70-marble-paleta-nova-a.png)
![](../imagens/70-marble-paleta-nova-b.png)
*Two of the experiments from that chat. First: new palettes. Then: the same with dithered gradients.*

In the afternoon I worked with a comparison viewer Claude built: the Mega Drive version on each side and the PlayStation reference in the middle. I asked for a levels adjustment on the PlayStation image, because the Mega Drive comes out more contrasted and I needed to judge them on equal footing. I asked why the dithering always used a 50% pattern and whether it could vary. I noticed the PlayStation references themselves had a levels problem and sent a corrected one to compare. At 5:23 p.m. I picked a winner from the candidates, and at 5:27 I asked for a new viewer with six versions per room, so I could choose one by one and send back a report.

![](../imagens/64-paleta-cenario-a.png)
![](../imagens/64-paleta-cenario-b.png)
![](../imagens/64-paleta-cenario-c.png)
*Another room, from the Colosseum. First: the PlayStation. Next: the direct conversion. Then: a palette planned for the whole area, sharing colors with its enemies.*

## Fixing my emulator

Testing was slow, and not because of the port. Every boot went through the Sega and Mega CD logos, and fast-forward didn't work on the emulator I was using. So I switched to RetroArch, and spent an hour of the afternoon with Claude making a test disc open with a double click, closing the terminal window afterwards, setting the window to 3x, the d-pad to WASD, and putting the six buttons back where they belong after they got scrambled.

## The number

71 commits, 97 messages from me. One whole castle, one triangle with a name.

Tomorrow: the coffin, redrawn as pixel art.

*How this is made: I decide what the port should be, draw and pick colors, and test every build. The code, tools and measurements are written by Claude (Anthropic's AI). This post was drafted by Claude from my chat messages and the project's commit history, and reviewed by me. The screenshots and GIFs come from rebuilding the port's code exactly as it was at the time shown.*
