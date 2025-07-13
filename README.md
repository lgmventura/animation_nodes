Animation Nodes
===============

![Build And Deploy](https://github.com/JacquesLucke/animation_nodes/actions/workflows/build.yml/badge.svg)

Animation Nodes is a node based visual scripting system designed for motion graphics in [Blender](https://blender.org).

Download the latest version from the Animation Nodes website. https://animation-nodes.com/#download

Get started with Animation Nodes by reading the documentation. https://docs.animation-nodes.com/

[![Showreel](https://img.youtube.com/vi/nCghhlMOwRg/0.jpg)](https://www.youtube.com/watch?v=nCghhlMOwRg)

Improved MIDI nodes
===================

This fork introduces improved MIDI nodes, allowing to work with MIDI tempos and notes on and off as a multiple of quarter nodes.

The original MIDI nodes in Animation Nodes doesn't include tempo information and only include note on and off in seconds, which will deform them instead of changing the tempo. Nothing was reomved in this fork, only additionally included.

Example of a node tree to create a MIDI animation accelerating the pan instead of stretching the notes for each tempo change:
![Complete node structure](https://user-images.githubusercontent.com/16710238/197834327-08314cb4-f4e5-4568-b943-dd2b9b28f47d.png)
![Subprogram only](https://user-images.githubusercontent.com/16710238/197834710-06549164-257f-4b11-b370-0bcba604d770.png)

## New nodes
### Tempo event info node
Permits access to the tempo changes in the MIDI file. If you want something to move or go faster in your animation when there is an accelerando or a sudden tempo change, this is the right node to use. You will access the tempos directly from the MIDI file reader nodes as a list of tempo changes that start in a given time as a multiple of quavers (quarter notes).

### Time signatures info node
This can access the time signatures from a MIDI track (via track info node), retrieving when it starts, the numerator and the denominator. If you want to animate a metronome, a conductor or a dancer, this is the right node for it ;).
