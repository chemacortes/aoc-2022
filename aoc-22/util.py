import os
import re
from pathlib import Path
from pprint import pprint


def read(file_input: str):
    with open(file_input) as f:
        data = [line.strip("\n") for line in f]

    mapstr = data[:-2]
    movesstr = data[-1]

    map = {
        (row, col): char
        for row, line in enumerate(mapstr, start=1)
        for col, char in enumerate(line, start=1)
        if char != " "
    }

    moves = re.findall(r"(\d+|[RL])", movesstr)

    return (map, moves)


if __name__ == "__main__":
    os.chdir(Path(__file__).parent)

    map, moves = read("data-training.txt")

    pprint(map)
    print(moves)
