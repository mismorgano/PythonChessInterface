# A GUI for chess

## Overview

Part of my journey to learn python is to make video games using pyglet.
But a GUI for chess is not precisely a video game, in any case it's a multimedia application.
So I wanted to give it a try.

## Dependencies

Besides the obvious `poetry.toml` dependencies, this project also make use of a chess engine
which use the **UCI** (Universal Chess Interface), in this case we use
[Stockfish](https://stockfishchess.org/).

## Install

For the python dependencies, just type

````commandline
poetry install
````

For the `chess engine` part just go to [Stockfish Downloads](https://stockfishchess.org/download/) or whatever other
chess engine you prefer (ojo, not forget that it should implement the **UCI**), extract it under the `chess_engine`
folder and that's it. 