from enum import IntEnum
from typing import Literal


class Face(IntEnum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3

    def __repr__(self) -> str:
        return self.name


RIGHT = Face.RIGHT
DOWN = Face.DOWN
LEFT = Face.LEFT
UP = Face.UP

Pos = tuple[int, int]
Sector = tuple[int, int]
Move = int | Literal["L", "R"]
Map = dict[Pos, Literal[".", "#", " "]]
Schema = dict[Sector, dict[Face, tuple[Sector, Face]]]
