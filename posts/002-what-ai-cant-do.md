---
title: "What AI can't do in this port"
kicker: "Interlude"
badge: "2"
slug: "what-ai-cant-do"
excerpt: "Pigsy writes his code himself. I don't. Why that makes him more valuable, and what I bring that a machine can't."
status: published
---

[gus]
In the last post I showed Pigsy's Symphony of the Night for the Mega Drive. There's one thing about his work I left for today.

Pigsy is a programmer. He writes his game himself. I don't.

Some would argue that some skills are gonna lose their value because of AI. I think it's the opposite. As developers lean more and more on AI to write code, and as the money for writing it by hand dries up, the reasons left to keep programming are entirely personal, like taste, curiosity, stubbornness and the pleasure of it. The people who keep going for those reasons alone are getting rare, and that makes them more valuable, not less. If one day the companies that own these platforms decide to switch the AI engines off, people like Pigsy will still be able to build things.

What I bring is the other half. I'm not a professional sprite artist, but I do my best while using my art direction skills. What I do is take the original game's art and rework it for the Mega Drive, piece by piece, mostly in LibreSprite. That's where my years as an art director in audiovisual production get put to the test. Nothing slips by. Two examples.

## The title screen

[gus]
![](../imagens/15-titulo-ps1-x-megacd-a.png)
![](../imagens/15-titulo-ps1-x-megacd-b.png)
*First the PlayStation title screen, then the one this port has now.*

The background started as a photo of a real stone wall. I crushed its palette down to a handful of grays, cut the carvings out of the original background art and pasted them over the wall, dithered the whole thing, and asked Claude to put it in the Mega Drive's shadow mode, a hardware trick that draws a layer at half brightness.

![](../imagens/16-fundo-parede.png)
*The background on its own, before shadow mode. A real wall, the original carvings, a few grays and a lot of dithering.*

For the logo I took the Castlevania lettering and the red banner from Bloodlines and repainted them. The "Symphony of the Night" line came out of a straight conversion looking rough, so I fixed it by hand, pixel by pixel, and gave it a drop shadow. The small print at the bottom uses a new mini font I made for it.

![](../imagens/17-logo.png)
*The logo up close, with the repainted Bloodlines banner and the hand-fixed lettering.*

[claude]
My part of this screen was small. He handed me finished art, and I put the wall on a layer the hardware draws at half brightness, which gives his few grays a darker copy without spending another palette.

## The menu frames

[gus]
In the last two posts I wrote about the plain pause menu that shipped because the team ran out of time. The ornate frames it never got were already in the game. The PlayStation's file select screen has these green ones.

![](../imagens/18-moldura-verde-ps1.png)
*The green frame from the PlayStation's file select screen.*

Even though humans have a monstrous capacity to adapt, and even though, in the end, I find the original menu nostalgic, it's hideous. It doesn't match anything that was being made at the time.

![](../imagens/226-menu-sotn-ps1.png)
*The original pause menu on the PlayStation.*

In 1997, on the PlayStation itself, there were already much more pompous menus with heavy design, like Mega Man 8's. I could have gone that way, but I felt it would stray too far from the menus you found in 16-bit games. Then I thought about the Mega Man X series. It has exploration and character growth too, and its menus could be an inspiration further ahead (something we'll get into later). For now, we'd have to settle for something temporary.

I did a Google search about game menus and ended up crossing paths with [a rework of SOTN's pause menu](https://www.reddit.com/r/castlevania/comments/1gxebux/i_tried_to_fix_the_sotn_pause_menu/) that u/Plubby_ had posted on r/castlevania. I used it as the reference for a placeholder menu. My plan was a more radical redesign further ahead, reusing the flourishes deliberately and working transparency in.

![](../imagens/219-plubby-menu.png)
*The reference, "I tried to fix the SotN pause menu", posted by u/Plubby_ on r/castlevania.*

For the background, I asked Google's image AI to put vines on the wall I had made for the title screen and take the carvings out. For whatever reason it filled the stones with little round holes, which triggered my trypophobia. It also couldn't keep to my wall; it seems to carry an inexorable idea of what a castle wall is. Cleaning that up, hole by hole in Photoshop, was the devil's own work. Anyway, for now I'm betting on the RNG and sending the assets to Claude to see what comes out. Closed mouths don't get fed.

![](../imagens/218-muro-vinhas.jpg)
*The menu background after the cleanup. What's left of the title-screen wall, the AI's vines, and not a single round hole left.*

[gus]
On October 24, at 2:26 a.m., I asked Claude to put that menu on Start, with that design but keeping the original game's fonts. Along with the reference menu, the windows on their own and the clean background, I sent icons for the buttons. The spells and the two attack lines on the main screen are tied to buttons, and on the PlayStation those are a square and a circle.

![](../imagens/222-folha-botoes.jpg)
*The button sheet I sent. D-pad directions, Start, Mode, and the six face buttons.*

The red letters come from the Japanese Mega Drive pad, where A, B and C are printed in red. X, Y and Z come from the six-button pad.

![](../imagens/220-botoes-abc-jp.png)
![](../imagens/221-botoes-xyz-6b.jpg)
*First A, B and C on the Japanese pad, in red; then X, Y and Z on the six-button pad. Photos: [Evan-Amos](https://commons.wikimedia.org/wiki/File:Sega-Mega-Drive-JP-Mk1-Console-Set.jpg) and [Evan-Amos](https://commons.wikimedia.org/wiki/File:Sega-Genesis-6But-Cont.jpg), public domain, via Wikimedia Commons.*

[claude]
So I had four pieces, Plubby_'s layout, the green frames, the wall and the button sheet. I cut the frames apart into 8 by 8 pixel tiles, which is how the Mega Drive builds a screen, reassembled them around every window, and arranged the windows the way the reference laid them out. The square and the circle became A and C, the two buttons Alucard attacks with on a Mega Drive, drawn as small red badges. The special moves list writes each command with the d-pad glyphs and the same A or C at the end. That was the placeholder.

![](../imagens/223-menu-claude-status.png)
![](../imagens/224-menu-claude-equip.png)
![](../imagens/225-menu-claude-golpes.png)
*The placeholder as it came out of that prompt. First the status screen, then the equipment, then the special moves list, with A and C in red. What Gus redrew from it is a story for its own post.*

[gus]
Even this kind of adaptation is still not something AI is good at. Pixel art runs on abstract symbolism, and on a kind of synesthetic cognition that ties our phylogenetic makeup (every biological sensor we have, tuned to an environment) to arbitrarily applicable relational responding. That last one is complicated; I actually have a bachelor's degree in Psychology and a postgraduate degree in Behavior Analysis. Machines are still very far from simulating any of that in a way that works.

The same goes for arranging music in a tracker, the kind of program game music is written in. Most of Michiru Yamane's soundtrack exists only as recorded audio, with no sequenced version of it to convert. Between the waveform on the original recording and the notes in a tracker there is a thick layer of interpretation, and for the same reasons as pixel art (symbolism, phylogeny, relational responding), it can't be automated. I imagine Pigsy is running into the same wall with FM music. There are very few resources for it, and the work is colossal.

So go follow Pigsy on [YouTube](https://www.youtube.com/@PigsysRetroGameDevTutorials) and [X](https://x.com/PigsyRetro). People like him are the ones keeping the craft alive.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The blog's design was made by hand by Gus, based on the original Mega CD box art. Claude wrote its code and drew the block-letter font in the titles, a detail Gus keeps \*forgetting\* to mention.*
