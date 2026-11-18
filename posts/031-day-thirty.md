---
title: "Day 30: Assembly apocalypse"
kicker: "Day 30 · November 16, 2026"
badge: "31"
slug: "day-30"
excerpt: "The menu chat almost loses its purpose a second time and I take the blame for the first, the Ophan becomes the port's first original familiar, I design the familiar screens and status effects, and I ask Claude to reconsider writing everything in assembly."
status: draft
---

November 16 had 211 commits, the most of any day so far. Five or six chats were working in parallel, and I was moving between them.

![](../imagens/201-dia30-linha-do-tempo.png)
*November 16. The early-morning block is work I left running when I went to sleep at 1:34 a.m.*

## It's happening again

Just after midnight the pause menu chat had my designs from the day before. At 12:20 a.m. I double-checked: the material makes clear the idea is to remake the menu from scratch, right? At 1:24 I asked for a prompt to continue in a new chat, and at 1:25 asked whether the new chat would know it's a new native menu. At 1:27 I stopped:

> "Wait, it's happening again. I already went down this path when I left the native menu for here, and you're telling me to open a new chat with the same problem of the prompt not guaranteeing a new native engine."
>
> (Translated from Portuguese.)

And at 1:30 I said where the drift had come from:

> "Yesterday, at the start of the native menu task, the work was exactly this, and it had even started on it! I was the one who deviated in the middle to do the redesign."
>
> (Translated from Portuguese.)

At 1:34 I went to sleep with a clear instruction: when I woke up, I expected to test the complete native menu, rewritten to suit the hardware, with instant commands and screen refresh and 100% smooth scrolling. Claude worked until about 5 a.m.

## The Ophan

The eye with the ring I'd drawn two days before had a name now: Ophan. At 9:30 a.m. I asked whether it was cheaper than the bat familiar, and why. At 11:47 I asked Claude to check the other cards around the castle so the Ophan's card would sit at the right height above the floor. At 12:45 I kept its scope in check: one proposed behavior was something the Faerie already does in the original, so it didn't belong to the Ophan.

At 4:50 p.m. it merged into the main branch: the first original familiar of the port, with its card in the Royal Chapel's confessional.

![](../imagens/207-ophan-jogo.png)
*The Ophan next to Alucard in the port, from that day's measurements.*

## Assembly, all of it

At 11:55 a.m. I opened a chat with a provocative name, ASSEMBLY APOCALYPSE:

> "Now that we're further along in the project and have a better idea of what things cost, reevaluate rewriting EVERYTHING in assembly and how much that would save."
>
> (Translated from Portuguese.)

The point was memory, not speed: every module window lives on a few hundred spare bytes, and hand-written 68000 assembly is smaller than compiled C. Claude's reservation was code that rarely runs, where the gain looked small. At 12:36 I answered it:

> "Got it. Cold code is your reservation. I think we just create switches for everything you detect as cold code and give them to me to test. There's no rush! That way we spend more time together, mwahahaha 😈"
>
> (Translated from Portuguese.)

At 12:41 I asked for one more thing: make it show in all of the project's documentation, first so that future chats don't fall into the tendency of dodging the rewrite, and second so there's no conflicting information that leads Claude to dodge it. It became a project rule: our code is written in assembly by default, every rewrite sits behind a switch that goes back to the C, and the measure is bytes saved.

![](../imagens/202-assembly.png)
*The rule as it ended up.*

At 11:50 p.m., ready to start the rewrite, I admitted a worry: "Before opening it, I'm afraid it'll resist the idea and not want to do it." At 11:53 I asked which model to use for the task.

## The familiar screens

In the afternoon the menu chat reached the Familiars screen. At 1:54 p.m. I asked for the D-pad and button glyphs in LibreSprite to edit them myself. At 3:23: "glyphs edited". At 3:24 I spotted leftover black pixels under the small B, and at 3:31 I'd fixed A and B myself.

![](../imagens/204-glifos.png)
*The button glyphs after my edits.*

At 3:51 I asked whether familiars have a list of attacks unlocked by level. At 4:01 I set the layout: locked abilities show "Lv 40 ------------" until they unlock, to hint there's more to come; inside a familiar's sheet you scroll through its attacks and the bottom of the screen describes each one, all in English. At 4:17: the main background in shadow instead of blue. At 4:22 I noticed the ON button's green matched the border green: if the player customizes the border color, wouldn't the ON change too?

![](../imagens/203-familiares-tela.png)
*The Familiars screen as it stood that evening, before the portraits.*

Then the rules. At 5:29 I took the toggles off the Sword familiar: it only does one attack at a time, its spell is by input, and Manifest is an equippable item. At 5:31 we needed to decide what happens to the percentages when an attack is switched off. At 5:36:

> "Let the spells' frequency go up a little, just put a slightly higher ceiling if one stays on alone. That strategy needs to pay off a bit more than normal when there's an enemy weak to lightning."
>
> (Translated from Portuguese.)

At 6:27 I sent images of the familiars: I wanted portraits of their faces instead of the sprite. At 6:34 I asked for a page to do the crops myself, and at 6:38 they were done. At 7:53: flip the portraits facing left, they have to look right. At 5:47 the fly got its line, "It licks what it likes...", and at 8:53 the Ophan its own: "Do not be afraid."

## Effects on Alucard

Another chat was making the indicators for status effects and buffs. At 4:42 p.m. I described one pixel by pixel: white pixels in threes rising from the middle of the bottom of Alucard's outline until they meet at the top, three clockwise and three counterclockwise. At 4:47 the catch: could we reproduce those colors in the fixed palette? No. At 4:51: "Neither A nor B. We'll have to make do with the fixed colors!" At 4:56 I asked for the palette with each index's number so I could describe exactly what I wanted. At 5:28: for curse and poison, double the frequency, and the pixels travel top to bottom; for curse, blue base with green pixels.

![](../imagens/205-estados.gif)
*The bad-status indicators that evening, at the editor's preview size.*

At 9:24 I reasoned through the cost: what makes it need recalculating all the time is the glow of a different color, dynamic, never in a known place in each pose. Otherwise it would be just another sprite on screen. At 9:30 I suggested particles that rise like steam from the top of Alucard, and asked whether they'd fall behind when he walks. They should, by gravity.

![](../imagens/206-vapor.png)
*The steam particles. On the right, walking, they trail behind.*

## From my phone

At 10:34 p.m. the desktop vanished from Moonlight. I was away from the PC. At 10:44 I was at the PC and unlocked it. At 11:15 I added that whatever runs remotely also needs to be able to click the error window that pops up saying the resolution doesn't exist.

At 11:39 I left one chat to watch two merges and start the assembly rewrite once they finished, working through the night until 8 a.m.

## The number

211 commits, 149 messages from me, counting some long review comments. One original familiar in the game, one rule written into every document, and one confession about who derailed the menu.

*How this is made: I decide what the port should be, draw and pick colors, and test every build. The code, tools and measurements are written by Claude (Anthropic's AI). This post was drafted by Claude from my chat messages and the project's commit history, and reviewed by me. The images are previews from that day's work, my edited glyphs, and a diagram.*
