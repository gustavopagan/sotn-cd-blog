---
title: "Day 13: moving house"
kicker: "Day 13 · October 30, 2026"
badge: "14"
slug: "day-13"
excerpt: "The project moves from my laptop to my desktop, Claude misunderstands which computer needs more memory, and the port gets a build queue that runs on my own machine."
status: draft
---

October 30 had almost no game in it. It was moving day.

![](../imagens/108-dia13-linha-do-tempo.png)
*October 30. The morning is me setting up the desktop; the night is the two of us teaching the project to use it.*

## The move

The night before, I had dragged the whole project folder to an external drive. At 12:29 a.m. the copy was on the desktop and I had swapped the folders in the project's context. Eight minutes later I sent every open chat the same message: I switched computers, this message comes from the desktop called "pagan", not the laptop "pagan-laptop" anymore.

![](../imagens/110-mudanca.png)
*The route. Nothing more sophisticated than a drive in a drawer.*

One chat that started fresh on the desktop got a little lost, so at 12:59 a.m. I asked for a temporary rule in the project explaining the move. Three chats had been working when I decided to switch machines; I had told all three to pause, and at 2:07 a.m. I brought their reports to the chat handling the move.

## Whose computer?

That evening I installed WSL, the Linux that runs inside Windows, and Debian on top of it. At 9:31 p.m. I asked how to give more memory and threads to the virtual machine. Claude walked me through giving them to WSL, and at 9:59 p.m. I had to stop it: "Calm down, you misunderstood me, I want to give more resources to YOUR VM." (Translated from Portuguese.)

Claude's own workspace on my computer runs inside the Claude app, and it can't be resized from a chat. What Claude could do was use WSL as a second machine. At 10:22 p.m. I asked whether that meant I should leave more tabs ready for parallel tasks. At 10:30 p.m. I agreed to all of it, and added the part that mattered: now we need to teach the project to use this new tool.

## A queue

What came out of that night is still how the port gets built. Claude's workspace drops a small file describing the build it wants into a folder; a script running in WSL on my desktop picks it up, builds, and writes the log back. Every disc in this blog's GIFs went through that queue.

![](../imagens/109-fila.png)
*The queue, simplified. Full builds stopped competing with Claude's own work for memory.*

At 10:44 p.m. it was done, and I asked whether I could resume the three tasks that had been on the laptop: music, menu and fixes. Claude wrote the prompts to reopen them on the desktop.

## The number

19 commits, 50 messages from me, one computer swapped for another.

*How this is made: I decide what the port should be, draw and pick colors, and test every build. The code, tools and measurements are written by Claude (Anthropic's AI). This post was drafted by Claude from my chat messages and the project's commit history, and reviewed by me.*
