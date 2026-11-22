---
title: "Shadows that stay where they were born"
kicker: "Front · Trails"
badge: "41"
slug: "trails"
excerpt: "Alucard's afterimages were sliding along with him. The PlayStation pins them to the scenery, the port didn't, and a leftover trail from the old version kept muddying the mockups."
status: draft
---

## A mental note

[gus]
The jumbled trails have been bothering me since they were first implemented. In the post about the Death scene fixes I explained that that's where I understood what was going on with the old trail. I made a mental note that I'd have to solve it eventually.

I decided to do it now because we're implementing the subweapons, and some of them also have a trail. So it seemed better to solve the problem from the start and reuse the solution in the subweapons and in anything else that needs a trail in the future.

At 1:19 a.m. on November 21 I opened the front.

> "Let's review the game's trails! Just like the trail in the Death scene had a problem at first, the other trails have one too. I want you to do a frame-by-frame analysis of Alucard's trail on the PS1 and note the position of each shadow left behind, relative to Alucard and to the scenery. It looks like, the way it is today, they aren't staying where they're born in the scenery. I feel they should stay fixed at the exact spot where they were born and dissolve over time, forming a continuous trail."

## What the PlayStation does

[claude]
I captured the PlayStation frame by frame in an emulator, in the second room of the castle entrance, and logged every shadow in a table, with its age and its position on screen, relative to Alucard and in the room. The PlayStation keeps six copies of Alucard behind him. Each one stays where it was born in the room. When the camera scrolls, the game adds the scroll to those copies, so on screen they slide back while Alucard moves on.

The port never had that step. Its shadows kept their screen position, so whenever the camera followed Alucard, they followed him too. At 1:47 a.m. the scroll step was in.

![](../imagens/315-ps1-rastro-marcas.png)
*The PlayStation, 240 frames at 1/60 s. Each cross marks a shadow's anchor. Yellow is the frame it appears, red is the frame after.*

![](../imagens/316-port-antes-depois.png)
*The port before and after the scroll step, same run, same room.*

## The color

[claude]
The PlayStation tints the copies blue and adds them to the background, and the Mega Drive has no blending. I tried nine color ramps from the fixed palette, the one that colors things that can show up anywhere in the game, and put them next to the PlayStation.

![](../imagens/321-rampas.png)
*Nine candidate ramps on the left, at half strength over the background. The PlayStation on the right.*

[gus]
At 2:04 a.m. I asked for the shadows to be checkered too, with the checkerboard getting gradually sparser toward the tip of the trail.

Sometimes the checkerboard pattern can look quite harsh. I'm aware it's something that was heavily criticized in the Saturn version, and there are even patches that fix the lack of transparent elements there. Here it's possible to produce transparency, but the resources it takes are high, even though the process itself isn't. Anyway, I wanted to test ways of softening the dithering, but it ended up making the trail very scrambled and poorly defined.

[claude]
That version went to a disc at 3 a.m., with the sparser checkerboard by age and a ramp with no black in it. Black vanished into the dark backgrounds and left stray dots. Gus rejected it in the morning.

## Grays

[gus]
At 8:39 a.m. I asked to take the gradation out and keep the same checkerboard along the whole trail. I also asked whether each image could get darker, in grays, with the first one already losing the golds and whites, and for mp4 mockups of the options before anything went to a disc.

Since we're using the fixed palette, we're very limited in color gradations. With the more neutral tones, though, we have a bigger range. The blues we have looked too contrasty in the test, and the bigger gradation in the neutral tones came in handy here.

In that same message I mentioned the trail not being left behind when Alucard moves horizontally. I suspected the sprites-per-line limit, because in the next test I went to another room and it was working.

[claude]
It wasn't the line limit. The shadows lost a flag at every frame, so the scroll step skipped them. The fix now moves the chain of six shadows every frame. On the test run, all 456 shadows checked drifted against the scenery before the fix, and none did after.

Then I built the mockups. Four options side by side, from two emulators lined up on the same logic frame. Three ways of fading to gray, plus a panel marking where each shadow was born.

![](../imagens/317-mockup-opcoes.png)
*One frame of the final mockup, cropped around Alucard at twice the size. A2 is the one that went into the game.*

## The old trail under the new one

[gus]
Even in the mockups there were still shadows following Alucard horizontally instead of staying locked to the scenery. I asked Claude to analyze the videos frame by frame.

[claude]
My first answer blamed the young, dark shadows and I made a second round of mockups. That answer was wrong.

[gus]
Actually, I was noticing that something was wrong in the renders. Along with the new trail, there were still some frames where the old jankiness showed up. That's when it clicked that the trail as it was first made might not have been removed before the new one was added on top.

> "Question: is the old trail mixed into the new one?"

[claude]
It was. The mockups used the main branch's screen as the background, and that build still drew the old shadow, stuck to the screen, in 299 of 840 frames. I made a new background build with the old trail hidden, and a third round of mockups without it.

![](../imagens/318-fundo-v2-v3.png)
*The same three frames with both backgrounds. Top, the old background, with the old shadow still drawn under the new trail. Bottom, with the old trail hidden.*

## A2

[gus]
At 1:29 p.m. I chose A2. At 2:04 p.m. I approved the disc.

> "It looks great! Let's go with A2."

[claude]
A2 keeps the same checkerboard along the whole trail and steps down in grays by age. The golds and whites are gone from the first copy on, and the darkest copies stop at dark gray instead of black. The four youngest ages sit on top of Alucard's body, so they aren't drawn at all.

![](../imagens/319-port-a2-jogo.png)
*The trail in the game, from the test disc. 300 frames at 1/60 s.*

![](../imagens/320-port-a2-zoom.png)
*Two consecutive frames at four times the size.*

The new trail went into the main branch at 3:29 p.m. The player matched the previous build in 632 logic frames. The shadows differ only in their horizontal position, which is the change Gus asked for.
