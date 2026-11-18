---
title: "Day 3: a warg in the sky and water made of paint"
kicker: "Day 3 · October 20, 2026"
badge: "4"
slug: "day-3"
excerpt: "The merman gets rewritten and it barely matters, a dead warg floats in the corner of the screen, water arrives as a palette trick, and at midnight I ask Claude if it's fixing the right things."
status: draft
---

The zombie cap fixed the hallway. One room later, the mermen hit the same wall. At 10 a.m. I asked the question that would follow us for weeks: how do other Mega Drive games deal with a screen full of enemies? Is Sonic the reference, or should we look at the technically crazier games?

![](../imagens/38-dia3-linha-do-tempo.png)
*The whole day in one picture. Red is Claude committing, blue is me writing. The gap in the evening is the only quiet stretch.*

![](../imagens/215-sonic-a.png)
![](../imagens/215-sonic-b.png)
*Sonic the Hedgehog (1991), captured from my own dump. The obvious reference.*

## The experiment

Claude's answer pointed at the difference between the two machines. These enemies were designed for a PlayStation, and the port was running their original code, translated for the 68000 but written with a different processor in mind. So I asked Claude to rewrite the merman by hand, specifically for the 68000, and explained why I wanted the experiment even if it didn't pay off:

"I want to try it, because I'm human, and the contingency of actually playing the version I imagine will have more strength to change the probability of me asking you for this again in the future." (Translated from Portuguese.)

That is a behavior analyst explaining reinforcement to an AI at 10:28 in the morning. Claude wrote the new merman, checked it frame by frame against the original (same jumps, same fireballs, same everything), and measured it.

![](../imagens/32-merman-medido.png)
*Each merman got 5% cheaper. The frame as a whole barely moved.*

At 11:20 I wrote back: "The difference really was negligible. Anyway, since you already rewrote it and it came out perfect, keep it." The experiment answered a better question than the one I asked. The expensive part wasn't any single enemy. It was what all of them share: every frame, the game walked through all 256 entity slots, three times, to find the dozen that were actually alive. On a PlayStation with a cache, that costs nothing. On a 68000, every empty slot costs real time. Claude replaced the walk with a list of the live ones.

![](../imagens/33-lista-de-vivos.png)
*Before and after. Same entities, visited in the same order, minus the empty ones.*

## A warg in the sky

By noon I had a list. The first screens with wargs didn't feel fluid, even with the emulator at 60. The mermen room was still slow. And when a warg died, it exploded into so many fire sprites that the game nearly stopped.

![](../imagens/39-warg-morte-0952.gif)
*A warg dying in the morning build, rebuilt from the 9:52 a.m. code. Watch the corner of the screen.*

Claude didn't touch the fire itself. It rewrote how the drawing processor deals with a burst of sprites: each new frame is decompressed while the screen is being drawn and sent to video memory in the next vertical blank, with a budget per frame, and whatever doesn't fit waits for the next one. I tested it at 1:20 p.m.: the fire cloud really was better, but now a whole warg appeared up in the corner of the screen while the other one burned.

![](../imagens/40-warg-fantasma-a.png)
![](../imagens/40-warg-fantasma-b.png)
*Two frames apart. In the second, the dying warg has a twin floating at the top of the screen.*

The explanation is one of my favorite things we found. To fade a dying warg out, the PlayStation draws it in a hidden spot outside the visible screen and then pastes that picture onto the real warg with a transparent polygon. The Mega Drive has no hidden spot and no transparent polygons, so the port drew the warg exactly where the PlayStation hid it: in plain view. Claude moved the drawing to the right place and, with no transparency to work with, made the dying warg blink instead of fading. That was Claude's call, not mine. In the same test I had noticed the zombies flashing fully above the ground for one frame before their rising animation started. They're supposed to be buried. That one got fixed in the same change.

At 2:22 p.m. I approved the warg, and found one more problem:

> "Warg: the transparency looked great! One problem: if I walk with Alucard while the warg is dying, its transparent sprite walks along."
>
> (Translated from Portuguese.)

The blink read as transparency to me. And the dying warg had been pinned to the screen instead of to the room, so it followed the camera.

Four weeks later, reviewing this post, I could have sworn the blink had been my idea. I even remembered thinking about it. The record says otherwise: I first asked for blinking a day later, for the mist, and the day after that for items on the floor. What I was probably remembering is something else. On the PlayStation, a dying warg fades out, then turns into a solid white silhouette and fades out again. The port carried that white flash for a while, and on November 2 the request I actually made was to take it out. Human memory isn't very reliable.

![](../imagens/41-warg-morte-2340.gif)
*The same death in the build from 11:40 p.m. that night. One warg, less fire.*

![](../imagens/82-warg-antes-depois-a.png)
![](../imagens/82-warg-antes-depois-b.png)
*Before and after, same frame of the same run. First, 9:52 a.m.: a cloud of fire and the twin warg floating top left. Then, 11:40 p.m.: fewer flames, no twin. The numbers on top are the debug readout.*

## A month on hold

At 2:22 p.m. I sent a longer report: the dead warg's blink moved along with Alucard, the red merman left a trail of its body behind its falling skeleton, and one of the two splash effects showed up black. Then I asked how much all of this weighed, and suggested a different approach. Use one water splash instead of two. Draw the swimming mermen in the background layer, the way big bosses are done on the Mega Drive. Give all the mermen the same entrance and death routines, just in different colors.

Claude fixed the bugs and kept the original structure. That day, porting the PlayStation's enemies as they were still felt like the safe choice. About a month later, the project's rulebook says the opposite: big enemies are built as backgrounds, effects come from a small shared pool, and the PlayStation's code is a reference rather than a starting point. I had written most of it down on October 20 in one message.

## Water out of paint

The mermen room has a waterline, and on the PlayStation everything below it is drawn semi-transparent. The Mega Drive has no transparency. What it has is a way to change colors in the middle of the screen. When the TV's beam reaches the line above the water, an interrupt fires, the port swaps in a tinted copy of every palette, and everything below that line is drawn in water colors.

![](../imagens/35-agua-hint.png)
*The trick, step by step. The few blank lines during the swap became the foam.*

![](../imagens/30-agua-2010.gif)
*The water working in the 4:54 p.m. build, rebuilt from that commit. Same raw palettes as before, now with a waterline.*

It worked, and then it broke in creative ways. At 6:05 p.m. I reported that Alucard turned water-colored and stayed that way in the next room, turned into a bat that refused to change back, and then crashed the game. Four minutes later I added that Alucard was supposed to be hidden behind the pile of rocks in that room, not in front of it. The tint and the rocks were fixed within the hour.

At 11:11 p.m. a new one: sometimes the whole screen flashed with a pale layer. The cause was a late frame. When the game logic didn't finish in time, the palette from the previous swap stayed in place for the entire screen.

![](../imagens/31-agua-pisca-a.png)
![](../imagens/31-agua-pisca-b.png)
*First: the water as intended. Then: the frame where the whole screen kept the water colors, HUD included.*

## FM, because I said so

In the afternoon I brought up music. Inglebard made Sega Genesis versions of the Symphony of the Night songs, and they sound great. I wanted an option in the game: the original soundtrack from the CD, or the same songs played on the Mega Drive's own sound chip. It's an aesthetic decision, not a technical one. At 6:30 p.m. I dropped a Mega Drive arrangement of the Castle Entrance theme into a folder, and twenty minutes later it was playing.

![](../imagens/37-fm-caminho.png)
*How a recorded chip performance became music inside the port. The drums go to the Mega CD's sample chip.*

At 10:32 p.m. I wrote that something had gone radically wrong and the whole game was slow. Ten minutes later Claude found it: on my emulator, the song was being read back from the sound chip's memory as blanks, and the main processor dutifully played the result: hundreds of junk writes per frame, two thirds of its time gone. The FM mode is shelved today, for reasons that deserve their own post.

## Missing lines

The same 11:11 p.m. message reported something else. With many mermen, splashes and fire on screen, other sprites lost lines. Same thing when a warg died next to zombies. That's the Mega Drive's 16-sprites-per-line limit again, and this time the cuts were landing on random objects.

![](../imagens/36-orcamento-por-linha.png)
*Before: the chip decides who loses lines. After: the port decides, and the loser blinks instead of getting sliced.*

The fix, Claude's choice, landed at 11:40 p.m. It counts the sprites on every line before the chip does: Alucard first, then enemy bodies, then effects. Whatever doesn't fit sits out that frame, whole, and the turn rotates, so the leftover object blinks. That's exactly what Mega Drive games do, and it's still how the port works.

## 11:56 p.m.

I tested that build and wasn't happy. "Are you sure you're working on the right problems? The previous build was smoother than this one. Now, besides not fixing the sprites, it's slower again. Right away, when I kill the first warg, it gets super slow." And: "It would be good if you could test with an identical copy of my emulator." (Translated from Portuguese.)

It was a fair question. Claude had been measuring on one emulator, and I was playing on another.

## The number

21 commits. One merman rewritten by hand, 5% faster, kept anyway.

Tomorrow: what Gunstar Heroes does with its explosions, and the day we started copying from the masters on purpose.

*How this is made: I decide what the port should be, draw and pick colors, and test every build. The code, tools and measurements are written by Claude (Anthropic's AI). This post was drafted by Claude from my chat messages and the project's commit history, and reviewed by me. The screenshots and GIFs come from rebuilding the port's code exactly as it was at the time shown.*
