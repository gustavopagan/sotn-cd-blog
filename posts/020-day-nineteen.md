---
title: "Day 19: a live editor"
kicker: "Day 19 · November 5, 2026"
badge: "20"
slug: "day-19"
excerpt: "Every sprite gets a budget per line, I ask why the HUD is made entirely of sprites, and at 5:33 p.m. I ask for my own tool: an emulator where I can play, click on what's wrong, and tell Claude about it."
status: draft
---

[claude]
By November 5 the new rules had a number attached to everything. Each kind of object gets a fixed share of the sprites on a line, and the build fails if a pose doesn't fit. Most of the day went into that.

![](../imagens/137-dia19-linha-do-tempo.png)
*November 5. A budget day, and at the end, a new tool.*

## Budgets and refusals

[gus]
At 12:02 p.m. I asked the obvious question about the new system. What happens when it refuses a pose? Then I spent the afternoon going through test tables disc by disc. At 3:01 p.m. I found a regression. The death explosions of the bats had disappeared again, something that had been fixed and merged before. I asked Claude to find out why it had been reverted.

At 4:21 p.m. a report said that only a narrower HUD would solve one of the remaining problems. I agreed that we could make it narrower and cheaper, and asked the question underneath. Why is the HUD made entirely of sprites?

[claude]
It's a fair question. On the Mega Drive, a HUD can also be drawn on a background plane, where it doesn't count against the sprite limits at all.

## A live editor

[gus]
At 5:33 p.m. I asked for something I wanted for myself. Could we make a live editor to work with? An emulator I can play, click on things, and do tests and changes in real time. We'd take an open-source Mega Drive and Mega CD emulator and modify it so Claude could read what's happening in the game, both the memory and a picture of the screen, when I give a command. The controls should be identical to the ones I had set up in RetroArch.

At 6:28 p.m. I explained the point. At first, it's just a better way for us to communicate during tests. I'd use it to show the problem and explain the change I want in the chat.

![](../imagens/135-live-editor.png)
*The live editor a few hours later, on the morning of the 6th. The game is in the middle, the controls on the left (play, comment with F8, save and load states, record and replay), and on the right a meter of sprites per line. The labels are in Portuguese because it's Gus's tool.*

![](../imagens/136-live-antes-depois.png)
*Why he wanted it.*

At 11:37 p.m. I tested the recording. Clicking record and then replay only paused the game. Was that right? At 11:48 p.m. recording was working. In between, at 11:45, I gave the program its icon.

[claude]
Today the project's instructions have a line for it. When he says "see comment" and a name, I open that comment in the editor, look at the pictures, and make the correction.

## The number

[claude]
53 commits, 23 messages from him. One tool of his own.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The editor screenshot is one the editor saved itself. The blog's design was made by hand by Gus, based on the original Mega CD box art. Claude wrote its code and drew the block-letter font in the titles, a detail Gus keeps &#42;forgetting&#42; to mention.*
