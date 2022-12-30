from collections.abc import Iterable
from enum import Enum

ROCK = "#"
AIR = "."

# types
Pos = tuple[int, int]


class Chamber:

    WIDTH = 7

    def __init__(self):
        self.positions = set()

    @property
    def top(self):
        return max((y for (_, y) in self.positions), default=-1) + 1

    def add(self, pos: set[Pos]):
        self.positions |= pos

    def freepos(self, pos: set[Pos]) -> bool:
        return all(
            0 <= x < self.WIDTH and 0 <= y for (x, y) in pos
        ) and not bool(pos & self.positions)

    def show(self, with_pos: set[Pos] = set()):
        top = max(self.top, max((y for (_, y) in with_pos), default=0))
        levels = (
            "|"
            + "".join(
                (
                    ROCK
                    if p in self.positions
                    else "@"
                    if p in with_pos
                    else AIR
                )
                for p in ((i, j) for i in range(0, self.WIDTH))
            )
            + "|"
            for j in range(top, -1, -1)
        )

        for level in levels:
            print(level)
        print("+-------+")

    # Used in Part2

    def base(self) -> tuple[int, ...]:
        return tuple(
            self.top
            - max((y for (x, y) in self.positions if x == i), default=0)
            for i in range(0, self.WIDTH)
        )


class Move(Enum):
    left = "<"
    right = ">"


class Rock:
    def __init__(self, shape: list[str]):
        self.dim = (len(shape[0]), len(shape))
        self.stopped = False
        self.base = 0
        self.shape = shape

        self.positions = {
            (i, j)
            for (j, l) in enumerate(shape[::-1])
            for (i, c) in enumerate(l)
            if c == ROCK
        }

    def __repr__(self):
        return "\n".join(self.shape)

    def pos(self, x: int, y: int):
        self.positions = {(i + x, j + y) for (i, j) in self.positions}

    def move(self, chamber: Chamber, move: Move):

        m = 1 if move == Move.right else -1

        new_positions = {(i + m, j) for (i, j) in self.positions}
        if chamber.freepos(new_positions):
            self.positions = new_positions

        new_positions = {(i, j - 1) for (i, j) in self.positions}
        if chamber.freepos(new_positions):
            self.positions = new_positions
        else:
            self.stopped = True
            chamber.add(self.positions)


hbar = [
    "####",
]
croiss = [
    ".#.",
    "###",
    ".#.",
]
invl = [
    "..#",
    "..#",
    "###",
]
vbar = [
    "#",
    "#",
    "#",
    "#",
]
square = [
    "##",
    "##",
]


def rocks() -> Iterable[Rock]:
    while True:
        for r in (hbar, croiss, invl, vbar, square):
            yield Rock(r)


def moves(s: str) -> Iterable[Move]:
    while True:
        yield from (Move(c) for c in s)


def read(file_input: str):
    with open(file_input) as f:
        data = f.read().strip("\n")

    return moves(data)


# Special for Part2


def moves2(s: str) -> Iterable[tuple[int, Move]]:
    while True:
        yield from ((i, Move(c)) for (i, c) in enumerate(s))


def read2(file_input: str):
    with open(file_input) as f:
        data = f.read().strip("\n")

    return moves2(data)
