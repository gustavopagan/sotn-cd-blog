---
title: "Day 11: the code goes first"
kicker: "Day 11 · October 28, 2026"
badge: "12"
slug: "day-11"
excerpt: "The folder gets reorganized overnight, the compression work lands, chats get a naming rule, the mermen are still slow, and the 2D save room finally plays on its own."
status: draft
---

After the cleanup started, October 28 was a day of closing things. Four commits reached the main build, all of them before 7 a.m., and most of my messages were about what to close next.

![](../imagens/102-dia11-linha-do-tempo.png)
*October 28. Claude worked overnight; I mostly asked questions and gave orders.*

## A folder you can read

The request from the night before got done at 3:43 a.m.: the whole project folder reorganized, with numbers in front of the names so they sort in the order you use them. Disc, inputs, tools, the main build, the side tasks, previews, audio, references.

![](../imagens/101-pastas.png)
*Not a screenshot: a reconstruction. On the left, folder names that appear in the chat history from that week.*

## Why compression, again

At 1:26 a.m. I asked whether the compression chat had finished or left loose ends, and reminded it why it existed: it was created to make the warg fit without cutting animation frames. At 4:45 a.m. its work was merged into the main build: the smaller format for loading, the faster one for whatever unpacks during gameplay.

At 1:41 a.m. I also made a small rule that stuck. Each prompt I send to a chat starts with its title, and in the title the code comes before the long name. With a dozen chats open, I needed to find things by code.

## Still the mermen

At 9:49 a.m. I tested again. Better, but still slow, especially when the yellow mermen die and when they spit fire while other mermen are on screen. If one is jumping while another dies, it's worse. The mermen room has been in every post since day 2, and it will keep showing up.

## The coffin, playing

At 7:16 p.m. I asked for a GIF of the 2D save room working. Claude recorded it from the save room test disc, in the emulator that runs without a screen: Alucard walks in, presses up, chooses yes, and goes into the coffin.

![](../imagens/100-saveroom2d.gif)
*The 2D save room from the coffin task's disc, recorded in an emulator. The coffin I redrew on October 24, now in the game.*

## The number

4 commits, 14 messages from me. One folder you can read.

*How this is made: I decide what the port should be, draw and pick colors, and test every build. The code, tools and measurements are written by Claude (Anthropic's AI). This post was drafted by Claude from my chat messages and the project's commit history, and reviewed by me. The GIF was recorded by Claude from the test disc of that time.*
