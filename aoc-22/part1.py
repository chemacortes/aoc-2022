from __future__ import annotations

import os
from pathlib import Path

from util import read

Pos = tuple[int, int]
Move = tuple[int, str]

FACES = ["RIGHT", "DOWN", "LEFT", "UP"]


class Pointer:
    def __init__(self, map, pos, face):
        # face: int  # 0 for right, 1 for down, 2 for left and 3 for up
        self.map = map
        self.pos = pos
        self.face = face

    def __repr__(self):
        return f"Pointer(pos={self.pos},face={FACES[self.face]}:{self.face})"

    def value(self):
        row, col = self.pos

        return 1000 * row + 4 * (col) + self.face

    def go(self) -> bool:

        row, col = self.pos
        match self.face:
            case 0:
                pos = (row, col + 1)
            case 1:
                pos = (row + 1, col)
            case 2:
                pos = (row, col - 1)
            case 3:
                pos = (row - 1, col)
            case _:
                raise ValueError

        front = self.map.get(pos, " ")

        if front == " ":  # wrap
            pos = self.wrap()
            front = self.map.get(pos, " ")

        if front == ".":
            self.pos = pos
        elif front != "#":
            raise ValueError

        return front == "."

    def turn(self, c):
        if c == "R":
            self.face = (self.face + 1) % 4
        else:
            self.face = (self.face - 1) % 4

    def wrap(self) -> Pos:
        row, col = self.pos
        match self.face:
            case 0:
                pos = (row, min(c for r, c in self.map.keys() if r == row))
            case 1:
                pos = (min(r for r, c in self.map.keys() if c == col), col)
            case 2:
                pos = (row, max(c for r, c in self.map.keys() if r == row))
            case 3:
                pos = (max(r for r, c in self.map.keys() if c == col), col)
            case _:
                raise ValueError

        return pos

    def show(self):
        row, col = self.pos

        print("\x1Bc")
        for i in range(row - 10, row + 10):
            print(
                "".join(
                    ">v<^"[self.face]
                    if (i, j) == self.pos
                    else self.map.get((i, j), " ")
                    for j in range(col - 10, col + 10)
                )
            )


if __name__ == "__main__":

    os.chdir(Path(__file__).parent)

    TRAINING = False
    map, moves = read("data-training.txt" if TRAINING else "data.txt")

    pointer = Pointer(map, (1, 1), 0)
    for move in moves:
        if move.isdigit():
            n = int(move)
            while n > 0:
                if not pointer.go():
                    # input("BLOCKED....")
                    break
                else:
                    # pointer.show()
                    # print(f"{n} de {move}")
                    # input("Press...")
                    pass
                n -= 1
        else:
            pointer.turn(move)
            # pointer.show()
            # input("Press...")

    print(pointer)
    print(pointer.value())
