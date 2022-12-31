import os
from pathlib import Path

from util import read

if __name__ == "__main__":

    os.chdir(Path(__file__).parent)

    TRAINING = False
    cubes = read("data-training.txt" if TRAINING else "data.txt")

    surface = len(cubes) * 6

    for (x, y, z) in cubes:
        common = {
            (x - 1, y, z),
            (x + 1, y, z),
            (x, y - 1, z),
            (x, y + 1, z),
            (x, y, z - 1),
            (x, y, z + 1),
        } & cubes
        surface -= len(common)

    print(surface)
