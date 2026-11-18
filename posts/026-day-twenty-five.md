---
title: "Day 25: Maximum economy"
kicker: "Day 25 · November 11, 2026"
badge: "26"
slug: "day-25"
excerpt: "Six tasks merge into the main branch in one go, I hand Claude a one-line design for two giants, I go looking for sound effects in other Mega Drive games and end up composing two jingles myself, and I ask for the PS1 original inside our tester."
status: draft
---

November 11 was a quiet day with two busy ends: just after midnight and the evening. In between, I was away.

![](../imagens/168-dia25-linha-do-tempo.png)
*November 11. Two clusters of work, one at each end of the day.*

## Six at once

At 12:07 a.m. I asked one chat to check every open task that was ready to merge and merge them in the right order. Between 12:11 and 12:25 six of them went into the main branch: the drawing improvements harvested from an old branch first, because the rest builds on them, then the enemy poses, the Entrance colors, the area budget with the prologue without pauses, the menu sounds, and last the code-space work, because it moves the menu and the title in memory. Two stayed out: the light effects, which still had my requests untested, and the native wolf, stuck on a freeze that belonged to the main branch.

At 11:35 a.m., reading the chat's summary, I noticed the task names from the last 24 hours didn't match all the tasks that had actually run.

## Two giants, one sentence

Blade and Gurkha were still too heavy. At 12:21 a.m. I gave the giants' task a design:

> "Let's define it right now: maximum economy is the motto. Make a list of Blade's and Gurkha's attacks. Their pattern is two steps forward and two steps back, nonstop. When Alucard gets close, they perform an attack! That's it, no more logic. For the hitbox, take inspiration from simple enemies like the skeleton."
>
> (Translated from Portuguese.)

![](../imagens/173-gigantes-ciclo.png)
*The whole behavior, as I wrote it.*

Looking back a week later, "maximum economy" wasn't really what I meant. I was trying to guess how Claude would adapt the giants, and what I wanted was a reading of them from scratch, built natively for the Mega CD's tools instead of the PlayStation's structure trimmed down. I was too lazy to explain that, so I wrote two words. Underneath, I was frustrated: Claude kept sidestepping the rewrites I'd been pushing for. We only found out why five days later.

At 8:29 p.m. I agreed to one attack per giant. By 9:01 Claude had both on a fixed cycle with each pose as the whole giant in one image. At 9:26 I tested, and it failed: each pose wasn't staying on screen for the right time. Claude fixed it so each pose holds for the next key's duration, which leaves the sword extended at the end of the strike. At 10:40 I pointed at one of the moves: "this should be Blade's attack." A minute later it was: a spin ending in a thrust, with its own sound and the weapon's hitbox active from the windup to the full extension.

![](../imagens/171-blade-gurkha-port.png)
*Blade and Gurkha in the port that evening, with Alucard between them.*

## Read it from the PS1

At 10:42 p.m., while watching the giants, I asked:

> "Are you reading the sprites from the PS1 game running? That would be good, because then you can see how the weapons rotate at each moment."
>
> (Translated from Portuguese.)

It wasn't. The poses came from the decompiled code and the game's tables. At 10:51 I offered to help: pick the best emulator, and I'd make a save state in a room with Blade. And if Claude agreed, the tester could get that as a feature: open the PS1 disc image, let me save a state and point at the screen, even record gameplay like it does for the Mega CD. I asked for a prompt to add it.

![](../imagens/174-ps1-testador.png)
*The idea: I set the scene on the PS1, the tester runs it, Claude reads what the original actually does.*

At 11:42 p.m. the PS1 tester was in the main branch, inside the live editor and runnable without a window. At 11:53 I sent a save state with a full inventory to keep as the starting point.

## Sounds from the shelf

The light effects task had my sound comparison tool from the day before: SOTN's sound on one side, another game's on the other, and a match button. At 8:44 p.m.:

> "I didn't find anything like the Life Up jingle in Bloodlines. Any suggestion?"
>
> (Translated from Portuguese.)

An hour later I had solved it myself:

> "If I weren't this good, we couldn't have this one. Jingles for the ups and for 'got'. I'll probably have to make more sounds to free up space in the future, mainly among the common sounds."
>
> (Translated from Portuguese.)

At 9:48 I added a detail from my own editing: in Furnace, the tracker I use, the sound only runs from 0 to 32, so everything after that could be cut.

At 10:20 p.m. I wanted a lot more to choose from. Besides the ROMs already in the reference folder, I had added a few more. I asked Claude to pull their sound effects into the comparison tool too, with a dropdown at the top to switch games, and an option to assign one SOTN sound to another, because some of SOTN's slots are silent and could reuse sounds that are already there.

![](../imagens/170-sound-tests.png)
*Two of the new games' sound test screens, as Claude's extraction went through them: Alisia Dragoon on top, Tiny Toon Adventures: Buster's Hidden Treasure below.*

At 10:43 one of them needed a hint from me:

> "Alisia Dragoon really is mixed, but from a certain point it stops being music and it's only sound effects. Some numbers are empty, but there are some good ones there. Can you get them anyway?"
>
> (Translated from Portuguese.)

![](../imagens/169-alisia-a.png)
![](../imagens/169-alisia-b.png)
![](../imagens/169-alisia-c.png)
*Alisia Dragoon (Game Arts, 1992), captured from my cartridge dump: title, first stage, and the sound test I was talking about.*

At 10:48 the voice lines in CD audio went on hold. Not urgent.

## The number

24 commits, 25 messages from me. Two jingles made by hand, one PS1 running inside our tester.

*How this is made: I decide what the port should be, draw and pick colors, compose sounds when needed, and test every build. The code, tools and measurements are written by Claude (Anthropic's AI). This post was drafted by Claude from my chat messages and the project's commit history, and reviewed by me. The images are diagrams, a frame from the port, and captures of other games from my own dumps.*
