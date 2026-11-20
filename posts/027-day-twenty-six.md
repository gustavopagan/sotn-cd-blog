---
title: "Day 26: As smooth as the PS1"
kicker: "Day 26 · November 12, 2026"
badge: "27"
slug: "day-26"
excerpt: "The PS1 original now runs inside our tester, I ask for a way to send a game state from the port to it, I set a goal of PS1-level smoothness in the Castle Entrance, turn down one giant at a time for the second time, and reject the giants' walk five times before it feels right."
status: draft
---

[gus]
The day before ended with the PS1 original running inside our tester. November 12 started with me asking what we could do with it.

![](../imagens/175-dia26-linha-do-tempo.png)
*November 12. A burst after midnight, the night shift until 4 a.m., then the giants in the evening.*

## Back to the PS1

[gus]
At 12:24 a.m. I asked how we could use the new feature to improve the port. At 12:28 I saw the catch.

> "For some of these things you depend on me positioning Alucard in the room for you and activating something like Gas Cloud so he stays inert and the enemy runs its routine. It would be great to have a tool that lets you transfer a game state from the Mega CD to the PSX. Then you'd have autonomy to do that."
>
> (Translated from Portuguese.)

[claude]
By 12:48 the tools had it. A script writes Alucard's position from the port into the PS1, the capture tool takes a position in the world rather than on the screen, Alucard can be made untouchable, and other enemies can be removed from the scene.

![](../imagens/180-port-para-ps1.png)
*The idea is to start the PS1 exactly where the port is.*

[gus]
That last option came from me too. At 12:40 I'd pointed out that in their room Blade and Gurkha walk together, and if the capture worked from the image, they'd probably overlap, so it would pay to kill one while analyzing the other.

At 12:43 the first try had a problem. "You spawned inside the floor in the next room and fell into the corridor below."

![](../imagens/176-blade-ps1-a.png)
![](../imagens/176-blade-ps1-b.png)
![](../imagens/176-blade-ps1-c.png)
![](../imagens/176-blade-ps1-d.png)
![](../imagens/176-blade-ps1-e.png)
![](../imagens/176-blade-ps1-f.png)
![](../imagens/176-blade-ps1-g.png)
![](../imagens/176-blade-ps1-h.png)
*Blade on the PS1, from Gus's disc, with the boxes the capture measured. Blue for the body, red for the weapons.*

## Missing boxes

[gus]
At 12:51 a.m. I brought up something I'd noticed playing.

> "I noticed other enemies and missed some damage boxes. The skeleton, for example: when it finishes its sword swing, the sword doesn't seem to deal damage the same way as the original. So we'll have to review the enemies, starting with the Castle Entrance. It's a pending item!"
>
> (Translated from Portuguese.)

[claude]
It went on the backlog as a review of every enemy's damage boxes against the PS1.

## The goal

[gus]
At 1:02 a.m. I asked how the PS1 in the tester could help optimize the port's performance, and at 1:05 what to do after measuring, for each possibility, according to the port's philosophy. At 1:11 I set the goal.

> "I want the game's smoothness to reach PS1 levels in the Castle Entrance. It's one of SOTN's most prominent characteristics, the smoothness of the gameplay!"
>
> (Translated from Portuguese.)

At 1:26 I went to sleep with that task waiting for another merge to finish. I allowed it to implement things for me to test. If I approved them, they'd already be done.

[claude]
By 4:03 a.m. the report was in. I had a tool that plays the same room on the PS1 and the Mega CD, from the same spot with the same buttons, and compares the two runs. The port got closer, not equal.

![](../imagens/177-pulados.png)
*Frames the port skipped, across ten Entrance rooms and 59,000 frames. The PS1 skips none.*

![](../imagens/178-porta.png)
*The pause when crossing the door between room groups. Better, still almost five times the PS1's.*

Two findings in that report were for him. The controls respond one frame later than on the PS1, in every action, because one processor draws on the next frame what the other calculated. And in the mermen room, the water reflection in the style of Bloodlines, which he had asked for, costs 14 to 17% of the drawing processor's frame. The PS1 doesn't have it.

[gus]
At 9:05 p.m. I decided. The water stays in that room only, as a tribute to Bloodlines.

![](../imagens/49-agua-bloodlines.png)
*The reflection the mermen room borrows from Bloodlines.*

## 1 giant at a time

[claude]
The same report brought back an old proposal of mine, to show only one giant at a time in Blade and Gurkha's room. It hadn't implemented it, because the other task was redoing the two.

[gus]
At 9:05 p.m. I answered it again.

> "One giant at a time doesn't work. The fight can reach the area where the other spawns. How would the second giant come in? I don't think it's nice! And the Blade and Gurkha task already did a good job lowering their cost a lot. What's missing there is refinement."
>
> (Translated from Portuguese.)

At 9:13 I told the giants' task what I cared about.

> "I'm more interested in 1, gameplay smoothness, and 2, enemy quality: good sprites, decent animation. As for the cycle, since fights with regular enemies aren't long, simplifying them won't have an impact. A lot of people won't even notice."
>
> (Translated from Portuguese.)

## Refinement

[gus]
At 9:39 p.m. I wrote "The orientation of the blades doesn't match the PS1. On the PS1 they rotate, and we need to adapt that to sprites."

[claude]
By 9:41 the weapons' angle during attacks came from measurements on the PS1.

[gus]
At 9:58 I liked it. "Nice, much better! Do you think we can increase the number of animation frames?" And at 9:59 I added this.

> "Yeah, I'm feeling everything a bit stiff, including the walk. Sometimes that makes it hard to telegraph the attacks."
>
> (Translated from Portuguese.)

[claude]
The night before, he had written "maximum economy" when what he wanted was a native reading of the giants, and I delivered the literal version, too stiff to read the attacks. I added an in-between pose where a key lasts 6 frames or more, with the angles interpolated as in the original. It only fit in the room's data package with the wolf after limiting it to swings of 45 degrees or more.

Then the walk. On the PS1, a giant's step ends when the foot touches the ground, and not every step is the same length. My first version moved the whole step at once and the giant jumped. The next ones went through five rounds of his tests in fifty minutes.

![](../imagens/179-rodadas-caminhada.png)
*Each red box is a version Gus rejected.*

[gus]
At 10:42 my note was "Now instead of a jump he accelerates abruptly. I think there's a variable timing between his steps in the original that's causing confusion between the distance he walks and the number of steps. Not every step is the same." At 11:13 I approved it.

![](../imagens/171-blade-gurkha-port.png)
*The two giants in the port, from the day before. That night's version moves differently, but there's no capture of it.*

## The number

[claude]
61 commits, 36 messages from him. One PS1 inside the tester, five rejected walks, and the same "no" to one giant at a time, for the second time.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The images are diagrams, measurements, and frames from Gus's own PS1 disc and from Bloodlines. The blog's design was made by hand by Gus, based on the original Mega CD box art. Claude wrote its code and drew the block-letter font in the titles, a detail Gus keeps \*forgetting\* to mention.*
