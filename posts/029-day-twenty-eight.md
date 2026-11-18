---
title: "Day 28: A fly, an eye, and what nobody sees"
kicker: "Day 28 · November 14, 2026"
badge: "29"
slug: "day-28"
excerpt: "The tester learns to fit my phone, I design two new familiars for the Mega CD version and end up drawing one of them myself, and I set a rule for everything the port removes because the player never sees it."
status: draft
---

November 14 had three threads running all day: the tester on my phone, two familiars of my own, and the effects the PS1 draws with primitives, which the Mega CD can barely afford.

![](../imagens/191-dia28-linha-do-tempo.png)
*November 14. Ninety-seven messages from me, most of them in the afternoon and evening.*

## The tester on my phone

The plan from the night before became real just after midnight. At 12:13 a.m. I raised a detail about my own marks on the screen: when I point at something, I write the mark's number and a comment and keep playing, but the mark stays on screen. I wasn't sure that when Claude looked at it, the screen would match the moment I pointed. It should disappear when I unpause, to make clear that the mark belongs to that one frame.

Then the small things. At 12:21 I opened the test list on the phone and couldn't get back to the game. At 12:36 the game was too small; I wanted it to fill the screen's whole height. At 12:45 I wanted the tester as an entry in Sunshine, the streaming server Moonlight connects to, and asked Claude to set it up through the browser. At 12:53: when I connect from the phone, the resolution should switch to the phone's proportions, at 720p.

At 1:11 I asked for a vertical, phone-sized version of the sound comparison tool too.

## Sounds and channels

At 1:32 a.m., choosing sounds from several games, I asked whether mixing them would weigh more because of the instruments each one brings. At 1:34: how do I know how many channels an effect uses? At 1:56 I pointed Claude to more of my dumps: Shinobi III, Streets of Rage 2 and 3, and QuackShot.

## A fly

At 2:13 a.m. I came back to what that chat was opened for: original familiars for the Mega CD version. The first one is a fly, obtained after killing Beelzebub, the corpse covered in flies. Its card would be in the room where the Bat card sits in the normal castle, but in the inverted one.

> "Its behavior will be peculiar: it lands on disgusting enemies, undead and bloody ones, and stays there causing damage while it's perched. Other than that, if Alucard stops, it lands and stays cleaning its legs. It is, after all, a fly."
>
> (Translated from Portuguese.)

At 2:20 I asked whether where it lands could be random: ceiling, walls, floor, Alucard's head.

Then the sprite. Claude generated some designs; I liked them but asked for them smaller, wings only as outline and veins, and at 2:42 said it looked too comical. At 2:46:

> "It got better, but I still think you generating it directly doesn't work. We need a strategy for generating pixel art sprites, something that can understand the impressionistic and symbolic technique and create this kind of asset."
>
> (Translated from Portuguese.)

I looked at a paid pixel art service and dropped it at 2:55: ten cents per image is too expensive. At 3:14 the wings at rest were right. At 3:46 p.m. I'd edited the fly's sprite myself.

## An eye with a ring

At 4:20 p.m. I wanted another familiar: the Angel. Claude's first version was quite different from the sketch I'd pasted. At 4:31 I described it again: built entirely from symmetry, with eyes that travel around a ring always in the same direction, and two rings spinning constantly. Then a round of corrections: light and shadow from Alucard's palette, because it looked flat; no black outline; with the outline gone, the ring can be thicker; the inner ring should look like a ribbon at that angle, not a full circle.

At 5:29 I sent Claude a LibreSprite file: "Open anel.ase, it's ready, it has 16 frames." At 5:42, after a misunderstanding:

> "Oh my, sorry, I didn't express myself well. The anel.ase is already the final sprite. I changed the idea: it's just a big eye with a ring spinning around it."
>
> (Translated from Portuguese.)

At 6:03 I explained how I made it: a golden 3D ring spinning, saved as frames, then the eye painted inside.

![](../imagens/189-angel.gif)
*The Angel, from my file, at 8x.*

![](../imagens/190-angel-quadros.png)
*The 16 frames.*

At 6:00 p.m. I told how it's obtained: after doing every possible routine in the Royal Chapel's confessional, confessing to the good priest and the bad one, listening to the good woman and the bad one. Leave and come back, and the Angel card is there.

Then its blessings, one rule at a time, between 6:45 and 7:59 p.m. At 7:20 I had been about to cut the intelligence buff, then remembered some weapons' special attacks spend MP; we'd need to check whether their damage is magic too. At 7:31 Claude described a play a player could make with it. I liked it, but then the player should lose the blessing, or it just becomes an easy way to get the buff by spending hearts.

![](../imagens/194-bencaos.png)
*The rules I set for the Angel that evening.*

At 8:35 I asked for a glow like the reddish one that carries the items away in Death's scene, recolored. At 8:52 the glow was a few pixels low and one to the right of where it should be for its star to be concentric with the familiar. At 8:53 I asked for fire colors, at 8:55 less gold and more orange-red.

## What nobody sees

The port's rule is that a calculation nobody sees and nothing reads gets removed. At 12:30 p.m. I questioned it:

> "When you say you'll delete what's invisible in the port, don't we risk deleting something important?"
>
> (Translated from Portuguese.)

Two minutes later I set the condition:

> "Everything removed for that reason has to be investigated to find out what it is, and stays as a pending item for, if needed, how to implement it adapted to the Mega CD."
>
> (Translated from Portuguese.)

![](../imagens/192-regra-invisivel.png)
*Removed isn't the same as forgotten.*

That task went through what the PS1 draws with primitives, the flexible polygons the Mega Drive doesn't have. At 2:59 p.m. I said what we'd been doing all along: primitives on the Mega CD are expensive, only what uses them sparingly keeps them, everything else gets adapted another way. In the evening I decided case by case.

![](../imagens/193-adaptacoes.png)
*My calls on the cases that came up.*

At 7:50 p.m. I pushed for the weapons to go on the disc and be reviewed early:

> "The weapons are very varied, there could be a surprise along the way. We'll have to get that out of the way as soon as possible. Weapons, shields, familiars, subweapons, spells, usable items are multiple combinations that can walk the whole castle."
>
> (Translated from Portuguese.)

![](../imagens/195-magias.png)
*Hellfire, Tetra Spirit and Soul Steal cast in the port during that review. Most of what makes them spectacular on the PS1 isn't drawn yet.*

At 9:14 p.m. the Gas Cloud test passed.

## The number

53 commits, 97 messages from me. One familiar designed, one familiar drawn by me, and a rule for what the port takes away.

*How this is made: I decide what the port should be, draw and pick colors, and test every build. The code, tools and measurements are written by Claude (Anthropic's AI). This post was drafted by Claude from my chat messages and the project's commit history, and reviewed by me. The Angel is my own sprite; the other images are captures from the port and diagrams.*
