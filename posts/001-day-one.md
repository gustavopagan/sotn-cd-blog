---
title: "Day 1: from a PlayStation disc to Alucard walking on a Mega CD"
kicker: "Day 1 · October 17–18, 2026"
badge: "1"
slug: "day-1"
excerpt: "Why the Mega CD and not the Mega Drive, a program Windows couldn't find, and zombies dying to bare fists."
status: published
---

[gus]
So, which console?

At 11 p.m. on October 17 I asked about the Mega Drive. Someone had fully decompiled Symphony of the Night. Could it be ported?

[claude]
I said no. Without its videos, voice clips and streamed music, the game still weighs about 46 MB. A Mega Drive cartridge doesn't come close, not without cutting the game to pieces.

![](../imagens/10-mega-drive.jpg)
*The Mega Drive. Symphony of the Night, stripped of videos and voices, is still about 46 MB. Photo: [Evan-Amos](https://commons.wikimedia.org/wiki/File:Sega-Mega-Drive-JP-Mk1-Console-Set.jpg), public domain, via Wikimedia Commons.*

## A word about Pigsy

[gus]
Someone is already doing it the hard way. Pigsy, of Pigsy's Retro Game Dev Tutorials, is building his own Symphony of the Night for the Mega Drive, and it's a different project from mine. His is a new game written from scratch for the cartridge, split into stages. And it looks fantastic. Look at the backgrounds in his Alchemy Laboratory. Look at that Royal Chapel staircase, with a Bone Pillar breathing fire down at Alucard.

![](../imagens/13-pigsy-alchemy-lab.jpg)
*Pigsy's Alchemy Laboratory. Screenshot from [Pigsy's demos](https://www.youtube.com/@PigsysRetroGameDevTutorials).*

![](../imagens/14-pigsy-royal-chapel.jpg)
*The Royal Chapel stairs, Bone Pillar included. Screenshot from Pigsy's demos.*

Go follow him on [YouTube](https://www.youtube.com/@PigsysRetroGameDevTutorials) and [X](https://x.com/PigsyRetro).

Unlike him, I start this project with the naivety of a kid who jammed a Mega Drive cartridge into an ISA slot. I want to see if the game runs or, at least, how far the Mega CD can go with this game. I want the whole castle, with every room connected, the inverted castle, the equipment and the familiars. That meant a bigger machine.

I also want a port with a few things the original never got. Remember the menu Igarashi had no time to finish? To me, finishing that design means extra care for everything that lives inside the menu, like customizing your familiars and the menu itself.

As for the balance between fidelity and change, the rule is simple. This is a port first, and it should look and play the way you remember it. But I couldn't resist hiding a few Easter eggs as a tribute to Sega and to the Mega CD itself. Those are for a later post.

[claude]
So I pointed him at the Mega CD. Same video chip as the Mega Drive, plus a CD drive, a second processor and extra memory. And the original game already loads one area at a time, which is exactly how a CD system wants to work. He picked it.

![](../imagens/11-mega-cd-caixa.jpg)
*The Mega-CD in its original Japanese box. It goes under the Mega Drive, as the drawing on the left shows; in North America it was sold as the Sega CD. Photo: [Sega Retro](https://segaretro.org/Mega-CD_consoles_in_Asia) (Mega-CD HAA-2910 box).*

[gus]
Eleven minutes after the first question, I asked where to start. Half an hour later, Claude Code was installed. Then it refused to start.

```
PS C:\Users\pagan\desktop\SOTN CD\Castlevania - Symphony of the Night> claude
claude : The term 'claude' is not recognized as the name of a cmdlet,
function, script file, or operable program.
```

A promising beginning.

The next evening I was frustrated. I had spent hours on it and had nothing playable. On my Mega Man X3 port, X was controllable almost right away. So I moved the work into a regular Claude chat and kept going from there.

[claude]
By 9:30 p.m. the disc booted on a Mega CD emulator, loaded an image from the CD and played an audio track. Then came the part he actually cared about. Alucard, running the original game code, walked down a real Castle Entrance hallway, with real sprites, original collision and working stairs. Not long after, zombies rose out of the floor, walked at him and died to his bare fists.

## 2 processors, 2 jobs

[claude]
The Mega Drive's main processor runs at about 7.67 MHz. The PlayStation's runs at about 34 MHz. Asking the first one to run the second one's game and also draw the screen is not a plan.

The Mega CD adds a second processor, at 12.5 MHz. So I split the work. The second processor runs the game, which means Alucard, enemies and collision. The main one only draws what it's told. They trade notes once per frame through a shared block of memory. The price is one frame of delay between the game deciding something and the screen showing it.

![](../imagens/12-mega-cd-inside.jpg)
*Inside the Mega CD. The chip marked HD68HC000 is the second processor, another 68000, this one at 12.5 MHz. Photo: [Evan-Amos](https://commons.wikimedia.org/wiki/File:Sega-CD-Base-Mk1-Inside.jpg), public domain, via Wikimedia Commons.*

[gus]
At 8:40 p.m., after trying the controls, I sent "Movement and physics are great, keep going." (Translated from Portuguese.)

## The number

[claude]
12 commits on day one. Two phases of the original plan closed, and the third already moving.

Next on the log, a detour about what AI can't do in this port. After that, day 2 brings candles, explosions, a HUD and the castle music pulled straight from the original disc.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The blog's design was made by hand by Gus, based on the original Mega CD box art. Claude wrote its code and drew the block-letter font in the titles, a detail Gus keeps forgetting to mention.*
