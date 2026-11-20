---
title: "Day 25: Maximum economy"
kicker: "Day 25 · November 11, 2026"
badge: "26"
slug: "day-25"
excerpt: "Six tasks merge into the main branch in one go, I hand Claude a one-line design for two giants, I go looking for sound effects in other Mega Drive games and end up composing two jingles myself, and I ask for the PS1 original inside our tester."
status: draft
---

[claude]
November 11 was a quiet day with two busy ends, just after midnight and the evening. In between, he was away.

![](../imagens/168-dia25-linha-do-tempo.png)
*November 11. Two clusters of work, one at each end of the day.*

## Six at once

[gus]
At 12:07 a.m. I asked one chat to check every open task that was ready to merge and merge them in the right order.

[claude]
Between 12:11 and 12:25 six of them went into the main branch. First the drawing improvements harvested from an old branch, because the rest builds on them, then the enemy poses, the Entrance colors, the area budget with the prologue without pauses, the menu sounds, and last the code-space work, because it moves the menu and the title in memory. Two stayed out. The light effects still had his requests untested, and the native wolf was stuck on a freeze that belonged to the main branch.

[gus]
At 11:35 a.m., reading the chat's summary, I noticed the task names from the last 24 hours didn't match all the tasks that had actually run.

## 2 giants, 1 sentence

[gus]
Blade and Gurkha were still too heavy. At 12:21 a.m. I gave the giants' task a design.

> "Let's define it right now: maximum economy is the motto. Make a list of Blade's and Gurkha's attacks. Their pattern is two steps forward and two steps back, nonstop. When Alucard gets close, they perform an attack! That's it, no more logic. For the hitbox, take inspiration from simple enemies like the skeleton."
>
> (Translated from Portuguese.)

![](../imagens/173-gigantes-ciclo.png)
*The whole behavior, as Gus wrote it.*

Looking back a week later, "maximum economy" wasn't really what I meant. I was trying to guess how Claude would adapt the giants, and what I wanted was a reading of them from scratch, built natively for the Mega CD's tools instead of the PlayStation's structure trimmed down. I was too lazy to explain that, so I wrote two words. Underneath, I was frustrated. Claude kept sidestepping the rewrites I'd been pushing for. We only found out why five days later.

[claude]
At 8:29 p.m. he agreed to one attack per giant. By 9:01 I had both on a fixed cycle with each pose as the whole giant in one image. At 9:26 he tested, and it failed. Each pose wasn't staying on screen for the right time. I fixed it so each pose holds for the next key's duration, which leaves the sword extended at the end of the strike.

[gus]
At 10:40 I pointed at one of the moves and wrote "this should be Blade's attack."

[claude]
A minute later it was. A spin ending in a thrust, with its own sound and the weapon's hitbox active from the windup to the full extension.

![](../imagens/171-blade-gurkha-port.png)
*Blade and Gurkha in the port that evening, with Alucard between them.*

## Read it from the PS1

[gus]
At 10:42 p.m., while watching the giants, I asked a question.

> "Are you reading the sprites from the PS1 game running? That would be good, because then you can see how the weapons rotate at each moment."
>
> (Translated from Portuguese.)

[claude]
I wasn't. The poses came from the decompiled code and the game's tables.

[gus]
At 10:51 I offered to help. Claude would pick the best emulator, and I'd make a save state in a room with Blade. And if Claude agreed, the tester could get that as a feature. Open the PS1 disc image, let me save a state and point at the screen, even record gameplay like it does for the Mega CD. I asked for a prompt to add it.

![](../imagens/174-ps1-testador.png)
*The idea. Gus sets the scene on the PS1, the tester runs it, and Claude reads what the original actually does.*

[claude]
At 11:42 p.m. the PS1 tester was in the main branch, inside the live editor and runnable without a window. At 11:53 he sent a save state with a full inventory to keep as the starting point.

## Sounds from the shelf

[gus]
The light effects task had my sound comparison tool from the day before, with SOTN's sound on one side, another game's on the other, and a match button. At 8:44 p.m. I got stuck.

> "I didn't find anything like the Life Up jingle in Bloodlines. Any suggestion?"
>
> (Translated from Portuguese.)

An hour later I had solved it myself.

> "If I weren't this good, we couldn't have this one. Jingles for the ups and for 'got'. I'll probably have to make more sounds to free up space in the future, mainly among the common sounds."
>
> (Translated from Portuguese.)

At 9:48 I added a detail from my own editing. In Furnace, the tracker I use, the sound only runs from 0 to 32, so everything after that could be cut.

At 10:20 p.m. I wanted a lot more to choose from. Besides the ROMs already in the reference folder, I had added a few more. I asked Claude to pull their sound effects into the comparison tool too, with a dropdown at the top to switch games, and an option to assign one SOTN sound to another, because some of SOTN's slots are silent and could reuse sounds that are already there.

![](../imagens/170-sound-tests.png)
*Two of the new games' sound test screens, as Claude's extraction went through them. Alisia Dragoon on top, Tiny Toon Adventures: Buster's Hidden Treasure below.*

At 10:43 one of them needed a hint from me.

> "Alisia Dragoon really is mixed, but from a certain point it stops being music and it's only sound effects. Some numbers are empty, but there are some good ones there. Can you get them anyway?"
>
> (Translated from Portuguese.)

![](../imagens/169-alisia-a.png)
![](../imagens/169-alisia-b.png)
![](../imagens/169-alisia-c.png)
*Alisia Dragoon (Game Arts, 1992), captured from Gus's cartridge dump. The title, the first stage, and the sound test he was talking about.*

At 10:48 the voice lines in CD audio went on hold. Not urgent.

## The number

[claude]
24 commits, 25 messages from him. Two jingles made by hand, one PS1 running inside the tester.

*How this is made. Gus decides what the port should be, draws, picks colors, composes sounds when needed and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The images are diagrams, a frame from the port, and captures of other games from Gus's own dumps. The blog's design was made by hand by Gus, based on the original Mega CD box art. Claude wrote its code and drew the pixel font in the titles, a detail Gus keeps forgetting to mention.*
