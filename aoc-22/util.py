import re
from typing import cast

from aoc22_types import Map, Move


def read(file_input: str) -> tuple[Map, list[Move]]:
    with open(file_input) as f:
        data = [line.strip("\n") for line in f]

    mapstr = data[:-2]
    movesstr = data[-1]

    map = cast(
        Map,
        {
            (row, col): char if char in ".#" else " "
            for row, line in enumerate(mapstr, start=1)
            for col, char in enumerate(line, start=1)
            if char != " "
        },
    )

    moves: list[Move] = [
        int(m) if m.isdigit() else m
        for m in re.findall(r"(\d+|[RL])", movesstr)
    ]

    return (map, moves)


if __name__ == "__main__":
    import os
    from pathlib import Path
    from pprint import pprint

    os.chdir(Path(__file__).parent)

    map, moves = read("data-training.txt")

    pprint(map)
    print(moves)

    # util for part2
    import math

    print(f"Side: {math.isqrt(len(map) // 6)}")
