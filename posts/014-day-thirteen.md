---
title: "Day 13: moving house"
kicker: "Day 13 · October 30, 2026"
badge: "14"
slug: "day-13"
excerpt: "The project moves from my laptop to my desktop, Claude misunderstands which computer needs more memory, and the port gets a build queue that runs on my own machine."
status: draft
---

[gus]
October 30 had almost no game in it. It was moving day.

![](../imagens/108-dia13-linha-do-tempo.png)
*October 30. The morning is Gus setting up the desktop; the night is the two of them teaching the project to use it.*

## The move

[gus]
The night before, I had dragged the whole project folder to an external drive. At 12:29 a.m. the copy was on the desktop and I had swapped the folders in the project's context. Eight minutes later I sent every open chat the same message, saying I had switched computers and that it came from the desktop called "pagan", not the laptop "pagan-laptop" anymore.

![](../imagens/110-mudanca.png)
*The route. Nothing more sophisticated than a drive in a drawer.*

One chat that started fresh on the desktop got a little lost, so at 12:59 a.m. I asked for a temporary rule in the project explaining the move. Three chats had been working when I decided to switch machines; I had told all three to pause, and at 2:07 a.m. I brought their reports to the chat handling the move.

## Whose computer?

[gus]
That evening I installed WSL, the Linux that runs inside Windows, and Debian on top of it. At 9:31 p.m. I asked how to give more memory and threads to the virtual machine.

[claude]
I walked him through giving them to WSL. He meant the machine I work in, and at 9:59 p.m. he had to stop me.

> "Calm down, you misunderstood me, I want to give more resources to YOUR VM."
>
> (Translated from Portuguese.)

What followed was a search through the app's settings, a restart of the Claude app, and a better idea. Use WSL as a second machine, just for builds.

[gus]
At 10:22 p.m. I asked whether that meant I should leave more tabs ready for parallel tasks. At 10:30 p.m. I agreed to all of it, and added the part that mattered. Now we need to teach the project to use this new tool.

## A queue

[claude]
What came out of that night is still how the port gets built. My workspace drops a small file describing the build it wants into a folder; a script running in WSL on his desktop picks it up, builds, and writes the log back. Every disc in this blog's GIFs went through that queue.

![](../imagens/109-fila.png)
*The queue, simplified. Full builds stopped competing with Claude's own work for memory.*

[gus]
At 10:44 p.m. it was done, and I asked whether I could resume the three tasks that had been on the laptop, music, menu and fixes. Claude wrote the prompts to reopen them on the desktop.

## The number

[claude]
19 commits, 50 messages from him, one computer swapped for another.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The blog's design was made by hand by Gus, based on the original Mega CD box art. Claude wrote its code and drew the pixel font in the titles, a detail Gus keeps forgetting to mention.*
