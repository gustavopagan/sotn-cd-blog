---
title: "Day 9: eight shades and the wrong computer"
kicker: "Day 9 · October 26, 2026"
badge: "10"
slug: "day-9"
excerpt: "A day of colors: explosions without red, a warg in eight shades, a question about bosses. Then the port starts running out of room, and Claude spends ten minutes looking at a computer I'm not using."
status: draft
---

[claude]
Only one commit reached the main build on October 26. The rest of the day happened in the side chats, most of it in front of comparison sheets, deciding colors.

![](../imagens/91-dia9-linha-do-tempo.png)
*October 26. One red mark. The main build barely moved while the colors were being decided elsewhere.*

## No red explosion

[gus]
The fixed colors I had reserved for weapons were turning into the palette for everything that lasts the whole game, like Alucard, items, dust and fire. After midnight I asked for more slots in that fixed palette, and accepted that we'd have to take some artistic liberties.

The test case was an explosion. In the comparison sheet one of them kept coming out greenish, and another came out too red. At 1:01 a.m. I asked Claude to keep the original drawing and just restyle its colors. At 1:26 p.m. I picked two candidates and asked for them without the red pixels, which clashed with everything else. At 1:37 p.m. it was good.

![](../imagens/94-explosao-cores.png)
*Claude's sheet, labels in Portuguese. On top, the PlayStation explosion. In the middle and at the bottom, the two versions Gus liked, in bronze, gold, cream and white, with no red.*

![](../imagens/93-itens-paleta.png)
*Candles, hearts, money and subweapons, from the same round. On top, the PlayStation. In the middle, what the port had that day. At the bottom, the shared fixed palette chosen automatically. The hearts went orange in the middle row; the shared palette brought the red back.*

## "8 tones, sweet spot"

[gus]
At 4:56 p.m. I tested a build and found a regression. The wargs and zombies had vanished from the first hallway, the second hallway had no enemies either, and the item hidden in the stairs before the Death scene was gone. Then Claude explained what would happen if a room didn't fit the new color plan, and I didn't like the answer.

> "What do you mean, if a room doesn't fit the new plan? That sounds kind of spaghetti."
>
> (Translated from Portuguese, 5:01 p.m.)

The other side of the plan was the enemies. At 5:45 p.m. I saw how few colors some sprites would get and wrote that it was a drastic limit. I asked for fixed options for the warg so I could decide, and at 5:57 p.m. I did. Eight shades is the sweet spot. A minute later I asked the obvious next question. If a warg needs this, how are we going to handle the big bosses?

## Running out of room

[gus]
At 7:08 p.m. I asked for optimizations that would apply to the whole game, not one enemy at a time. At 7:33 p.m. I opened a new chat for it, with a blunt opening. We're starting to bump into places where resources are really scarce.

[claude]
That chat started by reading references, including a curated list of Mega Drive development resources and the Game Hut files. And then it got confused about where his files were.

## The wrong computer

[gus]
I had started that chat on my Mac and moved back to my Windows notebook. Claude kept looking for the project folder on the Mac and telling me things were missing.

> "Sorry, I'm vibe coding with you, can you go easy on me? I want to download everything you need, but some things are cryptic to me."
>
> "That folder has been in the project's context for ages! Why can't you see it?"
>
> "I'm back on my Windows notebook. You're looking on the Mac, which is where I started this chat. Can you switch?"
>
> "I'm physically sitting in front of the notebook, with my hands on its keyboard, with the Claude app open, typing to you through the app."
>
> (Translated from Portuguese, 9:00 to 9:04 p.m.)

![](../imagens/92-dois-computadores.png)
*A reconstruction of 9:03 p.m. Not to scale.*

[claude]
That chat was tied to the machine it started on, and I kept answering from there instead of saying so. Four messages to get it across is on me. The fix was simple, a new chat opened on the right machine.

[gus]
At 9:56 p.m. I asked the new one whether it agreed with all the conclusions the two previous chats had reached, and at 9:59 p.m. I asked for a full audit of the conversation before anything else got built. At 10:07 p.m. I handed the whole optimization effort to it.

## The number

[claude]
1 commit in the main build, 49 messages from him. One explosion without red, one warg in eight shades.

Tomorrow, the optimization round, and what it finds.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The color sheets are previews Claude rendered during that work. The blog's design was made by hand by Gus, based on the original Mega CD box art, and Claude wrote its code.*
