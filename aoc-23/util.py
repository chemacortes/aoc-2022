from aoc_types import Elf, Grid


def read(file_input: str) -> Grid:
    with open(file_input) as f:
        grid: Grid = {
            (row, col): Elf((row, col))
            for row, line in enumerate(f)
            for col, c in enumerate(line)
            if c == "#"
        }

    return grid
