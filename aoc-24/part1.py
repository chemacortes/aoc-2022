import os
from pathlib import Path

from blizzards import Blizzards, Grid, Pos, load_blizzards


def spread(round: int, blizzards: Blizzards, grid: Grid) -> Grid:

    new_grid = {
        (r + i, c + j)
        for (r, c) in grid
        for (i, j) in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1))
    }

    return blizzards.blizz(round, new_grid)


if __name__ == "__main__":

    os.chdir(Path(__file__).parent)

    TRAINING = False

    blizzards = load_blizzards("data-training.txt" if TRAINING else "data.txt")

    initial: Pos = (1, 1)
    final: Pos = blizzards.dims

    round = 1
    blizzards.generate(round)

    while not blizzards.isfree(round, initial):
        round += 1

    grid = {initial}

    while final not in grid:

        round += 1
        grid = spread(round, blizzards, grid)

        # blizzards.show(round, grid)

    print(f"\nNeed {round+1} minutes")
