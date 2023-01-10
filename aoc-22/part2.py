from __future__ import annotations

import math
import time

from aoc22_types import DOWN, LEFT, RIGHT, UP, Face, Map, Pos
from cube import cube_front, schema1, schema2
from util import read


class Pointer:
    def __init__(self, map: Map, pos: Pos, face: Face):
        # face: int  # 0 for right, 1 for down, 2 for left and 3 for up
        self.map = map
        self.pos = pos
        self.face = face
        self.side = math.isqrt(len(map) // 6)

    def __repr__(self):
        return f"Pointer(pos={self.pos},face={self.face.name})"

    def value(self):
        row, col = self.pos

        return 1000 * row + 4 * (col) + self.face

    def go(self) -> bool:

        row, col = self.pos
        if self.face == RIGHT:
            col += 1
        elif self.face == DOWN:
            row += 1
        elif self.face == LEFT:
            col -= 1
        elif self.face == UP:
            row -= 1

        pos = (row, col)

        front = self.map.get(pos, " ")
        face = self.face

        if front == " ":  # wrap
            schema = schema1 if TRAINING else schema2
            pos, face = cube_front(self.pos, self.face, schema, self.side)
            front = self.map.get(pos, " ")

        if front == ".":
            self.pos = pos
            self.face = face
        elif front != "#":
            raise ValueError

        return front == "."

    def turn(self, c):
        if c == "R":
            self.face = Face((self.face + 1) % 4)
        else:
            self.face = Face((self.face - 1) % 4)

    def show(self, msg: str | None = None, *, stop=False):
        global SHOW

        if not SHOW:
            return

        row, col = self.pos

        print("\x1Bc")
        print(self)
        for i in range(row - 10, row + 10):
            print(
                "".join(
                    ">v<^"[self.face]
                    if (i, j) == self.pos
                    else self.map.get((i, j), " ")
                    for j in range(col - 20, col + 20)
                )
            )

        print()
        if msg is not None:
            print(msg.center(40))

        if stop:
            input("Press a key...")
        else:
            time.sleep(0.1)


if __name__ == "__main__":

    import os
    from pathlib import Path

    os.chdir(Path(__file__).parent)

    TRAINING = False
    SHOW = True
    map, moves = read("data-training.txt" if TRAINING else "data.txt")

    start = (1, min(y for ((x, y), c) in map.items() if x == 1 and c == "."))
    pointer = Pointer(map, start, RIGHT)
    pointer.show()

    for move in moves:
        match move:
            case int(n):
                while n > 0:
                    if not pointer.go():
                        break
                    else:
                        pointer.show(f"Move {n} of {move}")
                    n -= 1
            case str(t):
                pointer.turn(t)
                pointer.show()

    print(pointer)
    print(pointer.value())
