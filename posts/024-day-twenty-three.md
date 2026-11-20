---
title: "Day 23: Nine chats and a traffic light"
kicker: "Day 23 · November 9, 2026"
badge: "24"
slug: "day-23"
excerpt: "The VM fills up again, I go hunting for its disk file myself, and before leaving for the afternoon I set up nine chats that wait for each other through a traffic light. They keep working while I'm out."
status: draft
---

[gus]
November 9 started with tests of what the night shift had left, the wolf, the mermen room shadow, the mist and the door. By 12:05 p.m. I had approved or waved through all four. Then the day turned into logistics.

![](../imagens/152-dia23-linha-do-tempo.png)
*November 9. The shaded block is the afternoon Gus was out. The commits kept coming.*

## The VM is full again

[gus]
At 12:27 p.m., before anything else, I said we had to clean the VM. The virtual machine on my PC where Claude's chats compile and run the emulator was out of space again. At 1:03 p.m. I hesitated to ask the finished chats to merge their work, because merging takes space and there wasn't any.

There was a cleanup script. The problem was knowing which chat had used it. At 2:49 p.m. I pasted the same command into ten chats, one after the other, asking each to report the free space before and after. At 2:53 p.m. I reported back.

> "I ran it in several merged chats, but it doesn't look like I found the problem."
>
> (Translated from Portuguese.)

![](../imagens/160-colar.png)
*Three times that day Gus pasted the same message into nine or ten chats. This was the first.*

[claude]
At 4:05 p.m. one chat finally came back with real numbers. Its own corner of the VM had gone from 2.0 GB to 7 MB, and the VM's free space from 1.0 GB to 3.0 GB. The script had skipped most of it on the first pass, because it doesn't touch what it doesn't recognize, so I deleted my own leftovers by hand, 19 copies of test discs and old measurement files.

![](../imagens/154-vm-espaco.png)
*One chat's cleanup, as that chat reported it.*

[gus]
I wasn't satisfied.

> "There has to be a more efficient way to do this. That's the only chat I managed to find! The folders don't have the same names as the chats or the tasks, because when I create a chat the task doesn't necessarily exist yet, and that's where the names diverge. And there are a lot of chats open."
>
> (Translated from Portuguese.)

I asked for two things, permission to delete any chat's folders and more space for the VM. At 4:10 p.m. I couldn't find the menu or the folder Claude pointed me to, so I opened PowerShell and searched my user folders for the VM's disk file myself. It turned up at 4:12, `sessiondata.vhdx`, inside the Claude app's data folder. At 4:14 the VM reported 9.3 GB free out of 9.8.

[claude]
My reply to that came with an admission. I had first run the free-space check in my cloud container, where that path doesn't exist, instead of on his PC.

## Leaving them to work

[gus]
At 3:45 p.m. I had to leave for a few hours and asked whether chats could start only when it made sense. If one depends on another finishing something, it waits.

[claude]
I wrote a rulebook for unattended work and a small traffic light script. Each task turns on a light when it ends, merged, ready for testing, or stopped, with the reason. Anyone waiting checks the light, leaves a note on a shared board, and comes back on its own 20 minutes later. Nobody asks him anything. A decision that can't be undone gets prepared, written down as pending, and left for him.

[gus]
At 4:16 p.m. I pasted nine prompts into nine chats.

![](../imagens/153-nove-chats.png)
*Who waited for whom. One chat frees code space; the others need that space before making their test discs.*

At 4:41 p.m. I left. I came back at 8:14 p.m.

[claude]
In between, the chats made 58 commits, and the code-space task merged by itself at 6:44 p.m. There was one trick in it. A decompression table of 256 jumps became one of 32, which freed 896 bytes in each of the two tightest memory areas. Same output, four cycles more per token.

## Prayer

[gus]
One of the nine tasks was the menu sounds. I had written in its prompt that the menu music was my call, and to leave it silent.

[claude]
The chat looked at the decompiled sound code and came back with a finding. "Prayer", the menu track, isn't a sequenced song that would need rearranging. It's a regular streamed track on the original disc. My proposal was to play that file as-is, through the same path as the area music, with the PS1's loop point. At 4:41 p.m., on his way out, he agreed.

The same chat noticed the play time had never advanced in the port. Nothing counted the seconds, so the status screen always showed 0:00:00, and so did saves. It counts now, and stops in the menu and the map, as on the PS1.

It also looked at the title screen's lightning. On the PS1 it isn't transparency. The game swaps between four ready-made versions of the same image area.

![](../imagens/158-relampago-ps1-a.png)
![](../imagens/158-relampago-ps1-b.png)
![](../imagens/158-relampago-ps1-c.png)
![](../imagens/158-relampago-ps1-d.png)
*The four versions of the title area on the PS1, from Gus's disc. On the Mega Drive this can be a palette swap, if all four share the same drawing.*

One idea from that chat didn't stay. Death steals Alucard's gear in the prologue, and on the PS1 the stolen icon grows out of the center. I made the growing icon as ready-made frames. It fit, but it took the spot in that room's data package where the wolf and mist are read from the CD, so Alucard couldn't transform in Death's room. I undid it and left the item open.

## Done that already?

[gus]
At 8:18 p.m. two chats got a question from me in the same minute.

I wrote to the color task, about the shadows it was adding to three Entrance rooms, "If I'm not mistaken, shadow was already implemented in the mermen room today!"

[claude]
It had been. The prompt asked for the mermen room's method to be reused in rooms 1, 8 and 10, and those are the rooms the commits touched.

![](../imagens/157-sala8-sombra-a.png)
![](../imagens/157-sala8-sombra-b.png)
![](../imagens/157-sala8-sombra-c.png)
![](../imagens/157-sala8-sombra-d.png)
*Room 8. Options from the comparison tool for the wall-only shadow.*

[gus]
I asked the menu task "Wait, what are you doing? Why are you messing with the menu with the old design?" At 8:30 I explained. I meant the "press start" screen, which we'd already redone and I thought was already in the main branch, and the Konami logo before it. At 8:31 I told it to go ahead.

Since I wasn't there to pick colors in the comparison tool, I had asked the color task to build options for each item, put its recommendation on the disc, and say where the others were. At 8:14 p.m. I told it my decisions and report were in the comparison folders.

![](../imagens/155-portao-a.png)
![](../imagens/155-portao-b.png)
*The castle gate. First the old conversion, then the new one in neutral grays. In each, the top is the source and the bottom is the Mega Drive version.*

![](../imagens/156-slogra.png)
*Slogra. Top, before; bottom, the recommendation, with a yellower beak and a greener body.*

[claude]
One of its changes was switched off by default. The new colors for every area's loading rooms made the full-castle build stop in those rooms.

## The door

[gus]
At 2:59 p.m., testing the merged wolf and mist, I reported that the game froze right when the door closes.

[claude]
I fixed it by 3:13. At 3:38 the remaining issue was a pause of about 0.7 seconds the first time Alucard turns into a wolf or mist after the door, while the wolf's data is re-read from the CD.

[gus]
> "It bothers me. Leave that pending."
>
> (Translated from Portuguese.)

In the budget task's prompt I wrote that I wanted it without the pause, reading from the CD in the background from the moment the door closes. It's the idea from the night before, borrowing the music's buffer, now with an item number.

[claude]
By 11:54 p.m. that chat had the door holding on its last frame until the new data arrived.

![](../imagens/159-lobo-porta.png)
*The wolf in the door room, from the merge tests that day.*

## Housekeeping

[gus]
At 9:52 p.m. one chat answered me in English. I told it to speak Portuguese. At 8:36 p.m. I had to ask a chat whether it was the one that wanted me to test a CD audio build. It wasn't; the one that was got told to drop the test.

At 10:34 p.m. I asked whether the test discs were being built with all areas or only the tested ones.

[claude]
His own prompts had asked for the whole castle, for the measurements.

[gus]
At 10:40 I pasted the answer into nine chats. From now on, the whole castle only when it's needed; otherwise just the Castle Entrance and the Alchemy Laboratory. At 10:39 p.m. I approved the budget plan for the Castle Entrance.

## The number

[claude]
159 commits, 94 messages from him, a few of them the same message nine times. Nine chats, one traffic light, one VM disk he had to find himself.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The images are previews and comparisons Claude made during that work, plus frames from Gus's own PS1 disc. The blog's design was made by hand by Gus, based on the original Mega CD box art, and Claude wrote its code.*
