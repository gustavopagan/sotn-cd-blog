---
title: "Day 2: the night shift and the music math"
kicker: "Day 2 · October 19, 2026"
badge: "3"
slug: "day-2"
excerpt: "Zombies without end, transformations on a six-button pad, 114 minutes of music for 75 minutes of disc, and the day I turned out to be right."
status: draft
---

[gus]
Day 2 started at 12:23 a.m., when I went to bed and asked Claude to keep working on some tasks during bedtime. By morning there was a new build waiting, and I sent back the review. I couldn't find the candle, nothing blinked, the zombies died without any animation, and the backdash was unacceptably slow. While I was at it, I moved the backdash from Start to Y on the six-button pad. Start is going to be the menu.

[claude]
I kept committing until 2:05 a.m. and then stopped. Nobody played that build until he woke up, so his morning list was the first test it ever got.

![](../imagens/25-dia2-linha-do-tempo.png)
*October 19 in one picture. Gus went to bed at 12:23 a.m.; I kept committing until 2:05, and nobody touched anything until he woke up.*

[gus]
An hour later the build was much smoother and the death animations worked. It also crashed twice and sometimes forgot to draw the scenery, but that's what mornings are for.

![](../imagens/23-corredor-1910.png)
*The hallway as it really looked that day, rebuilt from the October 19 code. Colors straight from the PlayStation with no palette work at all, zombies piling up, and the debug readout across the top.*

## Zombies without end

[gus]
The Castle Entrance hallway spawns zombies forever, and after a while sprites started disappearing.

[claude]
The PlayStation keeps up to eight of them alive at once. The Mega Drive can only draw 16 sprites on any line of the screen, and the hallway is one long line of zombies.

![](../imagens/21-sprites-por-linha.png)
*On the yellow line, Alucard plus eight zombies need more sprites than the Mega Drive will draw on one line. The ones at the end simply vanish. An illustration, not a screenshot.*

[gus]
At 1:44 p.m. I told Claude to lower the cap to three. Nobody has complained.

![](../imagens/43-zumbis-teto.png)
*Eight on the PlayStation, three here.*

While testing that, I also noticed Alucard was being knocked back too hard by zombie contact. I told Claude that in the original, the size of the recoil depends on how much damage he takes.

## 3 forms, 6 buttons

[claude]
The PlayStation controller has shoulder buttons for the transformations. The Mega Drive pad doesn't, so the three forms needed a new home.

[gus]
I laid them out myself. X for the bat, Z for the wolf, up plus X for the mist. That evening only the bat had graphics; the wolf and the mist worked, invisibly. The double jump felt perfect on the first try.

![](../imagens/20-six-button.jpg)
*The six-button pad. X is the bat, Z is the wolf, up plus X is the mist (which I plan to change to X plus Z), Y is the backdash. Photo: [Evan-Amos](https://commons.wikimedia.org/wiki/File:Sega-Genesis-6But-Cont.jpg), public domain, via Wikimedia Commons.*

![](../imagens/26-controle-6-botoes.png)
*The layout from that night, drawn as a diagram.*

[gus]
It wasn't the first time I played Symphony of the Night with a Mega Drive pad. In 2000 I played it for the first time, on an emulator, on an Athlon computer the family had at home. Around then I found a DIY schematic for an adapter that let you plug a Mega Drive controller into the PC's parallel port, something like [this Instructables tutorial](https://www.instructables.com/Build-Sega-Genesis-Controller-Ports-for-your-PC/). I had no digital camera back then, and smartphones didn't exist, so there are no photos of mine. It was my first experience with a soldering iron, and it wasn't pretty, but it worked almost too well. The Mega Drive had been retired at home for a long time, and its joypad became my main controller. There was a driver for it, [PPJoy](https://github.com/elitak/PPJoy), written by Deon van der Westhuysen.

![](../imagens/228-adaptador-crrimson.jpg)
*An adapter like the one I soldered. Two Mega Drive ports and a parallel port connector on a board. Photo: crrimson, from the [Instructables tutorial](https://www.instructables.com/Build-Sega-Genesis-Controller-Ports-for-your-PC/).*

![](../imagens/227-adaptador-paralela.jpg)
*The kind of wiring diagram that adapter follows, with two Mega Drive pads on one parallel port.*

That's where the button layout came from. The Genesis pad was inspired by the arcade cabinets of its time, and this grip was very common. It's the one I used. With no shoulder buttons on the pad, their absence was never an issue.

![](../imagens/229-pegada-foto.png)
*How I hold the pad, recorded on November 20, 2026, for this post.*

## The music math

[claude]
The PlayStation streams its music from the disc in a format the Mega CD can't play, so every song gets converted into a regular CD audio track during the build. On the original disc, each song is two pieces, an intro that plays once and a loop that repeats. I did the math. All the songs, intro plus loop, come to about 114 minutes. A CD has room for about 75, after the game data.

![](../imagens/27-musica-xa-cdda.png)
*What the build does to every song. The intro is the part that's easy to cut.*

![](../imagens/22-musica-em-minutos.png)
*The music math. The dashed line is what fits on the disc.*

My recommendation was a middle ground. Keep the intros on the important songs, cut the long and forgettable ones, swap a few songs that barely play.

[gus]
I went further and cut every intro. Half an hour later I asked for some of them back, because Marble Gallery, Dracula's Castle and Dance of Pales have short intros that are worth keeping.

[claude]
By the end of the night the list had seven songs. We ended up roughly where I had started, by a different road.

## The day I was right

[gus]
Twice, actually. Three times, if you count the one that took a while to pay off.

Claude listed the enemies it was porting next, and I pointed out that none of them show up the first time you walk into the castle. At first there are only the wolves and the encounter with Death.

[claude]
He was right. The port had been using the Castle Entrance from the return visit, a deliberate shortcut of mine for the first test, and I hadn't flagged it. From that night on, the game starts in the real first visit.

![](../imagens/28-no3-np3.png)
*The same rooms exist twice in the game files. The port had picked the wrong one.*

[gus]
Then the area graphics didn't fit in memory with the music playing nonstop. The original has transition rooms with no music between areas, probably to give it time to load, and Sonic CD hides its loading behind the time travel animation. So silence while loading was fine by me. I suggested grouping the rooms, so the music would only stop at a few chosen doors.

[claude]
My plan had been a cache of rooms. His groups were simpler, and they are what the port still uses.

![](../imagens/29-grupos-de-salas.png)
*Room groups, simplified. The real Castle Entrance has more rooms and several groups.*

[gus]
The third one came at 10:55 p.m., with the mermen room crawling. I wrote that there must be known tricks for this, that the Mega Drive scene before AI was full of brilliant solutions, and that every problem we hit probably had a game that had already solved it. I even offered to dump any game Claude needed as a reference.

[claude]
That message became the method of this whole project. Before I optimize anything, I look for the Mega Drive or Mega CD game that already solved the same problem. More on that soon.

![](../imagens/24-mermen-1910.gif)
*The mermen room in the build from that evening, rebuilt from the 10:44 p.m. code. The readout at the top includes the processor load, and here it sits between 100% and 120%. Past 100%, the game no longer fits in a frame. On Gus's emulator it crawled. The fireballs and splashes are all there; the speed wasn't.*

[gus]
And somewhere in the evening, after Claude handed me a terminal command, I replied "Oh, I don't plan on doing that. I'm vibe coding, and I'm zero programmer." (Translated from Portuguese.)

[claude]
I promised no more terminal commands.

## The number

[claude]
35 commits. Three zombies on screen instead of eight.

Tomorrow, a merman rewritten for the 68000, and water made out of a palette trick.

*How this is made. Gus decides what the port should be, draws, picks colors and tests every build. Claude (Anthropic's AI) writes the code, the tools and the measurements. The CLAUDE parts are Claude's own account. The GUS parts are drafted by Claude from Gus's chat messages and corrected by him. The blog's design was made by hand by Gus, based on the original Mega CD box art, and Claude wrote its code.*
