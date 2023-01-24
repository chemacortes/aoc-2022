import os
from pathlib import Path

from aoc_types import Elf, Grid, Pos
from util import read


def around(pos: Pos) -> list[Pos]:
    x, y = pos
    return [
        (i, j)
        for i in range(x - 1, x + 2)
        for j in range(y - 1, y + 2)
        if (i, j) != (x, y)
    ]


def alone(grid: Grid, pos: Pos) -> bool:
    i, j = pos
    return all(grid.get(p, None) is None for p in around(pos))


def north(pos: Pos) -> list[Pos]:
    x, y = pos
    return [(x - 1, j) for j in range(y - 1, y + 2)]


def south(pos: Pos) -> list[Pos]:
    x, y = pos
    return [(x + 1, j) for j in range(y - 1, y + 2)]


def west(pos: Pos) -> list[Pos]:
    x, y = pos
    return [(i, y - 1) for i in range(x - 1, x + 2)]


def east(pos: Pos) -> list[Pos]:
    x, y = pos
    return [(i, y + 1) for i in range(x - 1, x + 2)]


def directions(pos: Pos) -> list[list[Pos]]:
    return [north(pos), south(pos), west(pos), east(pos)]


def propose(grid: Grid, elf: Elf) -> Pos | None:
    d = elf.dir
    dirs = directions(elf.pos)
    for n in [*range(d, 4), *range(d)]:
        if all(grid.get(p, None) is None for p in dirs[n]):
            return dirs[n][1]
    else:
        return None


def print_grid(grid: Grid):

    if not TRAINING:
        return

    min_row = min(r for r, _ in grid.keys())
    max_row = max(r for r, _ in grid.keys())
    min_col = min(c for _, c in grid.keys())
    max_col = max(c for _, c in grid.keys())

    for row in range(min_row, max_row + 1):
        print(
            "".join(
                "#" if (row, col) in grid else "."
                for col in range(min_col, max_col + 1)
            )
        )
    print()


def empty_tiles(grid: Grid) -> int:
    min_row = min(r for r, _ in grid.keys())
    max_row = max(r for r, _ in grid.keys())
    min_col = min(c for _, c in grid.keys())
    max_col = max(c for _, c in grid.keys())

    return (max_row - min_row + 1) * (max_col - min_col + 1) - len(grid)


if __name__ == "__main__":

    os.chdir(Path(__file__).parent)

    TRAINING = False

    elf: Elf | None
    # grid = read("data-training.txt" if TRAINING else "data.txt")
    grid: Grid = read("data-training.txt" if TRAINING else "data.txt")

    print_grid(grid)

    round = 1
    while True:

        # First half
        proposes_iter = (
            (propose(grid, elf), elf)
            for (pos, elf) in grid.items()
            if not alone(grid, pos)
        )
        proposes: list[tuple[Pos, Elf]] = [
            (pro, elf) for pro, elf in proposes_iter if pro is not None
        ]

        if not proposes:
            break

        round += 1

        moves: dict[Pos, Elf | None] = {}
        for pos, elf in proposes:
            moves[pos] = elf if pos not in moves else None

        # Second half
        for pos, elf in moves.items():
            if elf is None:
                continue
            del grid[elf.pos]
            grid[pos] = elf
        del moves

        grid = {pos: Elf(pos, (elf.dir + 1) % 4) for pos, elf in grid.items()}

        print_grid(grid)

    print(f"Need {round} rounds")
