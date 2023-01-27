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


def traverse(
    round: int, blizzards: Blizzards, initial: Pos, final: Pos
) -> int:

    # waiting before to entry
    while not blizzards.isfree(round, initial):
        round += 1
        # blizzards.show(round)

    # start
    grid = {initial}

    # moving to final
    while len(grid) > 0 and final not in grid:

        round += 1
        grid = spread(round, blizzards, grid)

        # blizzards.show(round, grid)

    has_a_path = len(grid) != 0

    return (
        (round + 1)
        if has_a_path
        else traverse(
            round, blizzards, initial, final
        )  # keep waiting to start
    )


if __name__ == "__main__":

    os.chdir(Path(__file__).parent)

    TRAINING = False

    blizzards = load_blizzards("data-training.txt" if TRAINING else "data.txt")

    initial: Pos = (1, 1)
    final: Pos = blizzards.dims

    minutes1 = traverse(1, blizzards, initial, final)
    minutes2 = traverse(minutes1, blizzards, final, initial)
    minutes3 = traverse(minutes2, blizzards, initial, final)

    print(minutes1, minutes2 - minutes1, minutes3 - minutes2)

    print(f"\nNeed a sum of {minutes3} minutes")
