import os
from pathlib import Path

from util import Chamber, read2, rocks


class Cache:
    def __init__(self):
        self.cache = {}

    def __call__(
        self, n_rock: int, n_move: int, chamber: Chamber
    ) -> tuple[int, int] | None:
        def roof(x: int) -> int:
            heights = (j for (i, j) in chamber.positions if i == x)
            return chamber.top - max(heights, default=0)

        chamber_roof = tuple(roof(i) for i in range(0, chamber.WIDTH))
        key = (n_rock % NUMROCKS, n_move, chamber_roof)

        if key in self.cache:
            return self.cache[key]

        self.cache[key] = (n_rock, chamber.top)
        return None


if __name__ == "__main__":

    os.chdir(Path(__file__).parent)

    TRAINING = False

    moves = read2("data-training.txt" if TRAINING else "data.txt")

    chamber = Chamber()
    until = 1000000000000
    NUMROCKS = 5

    cache = Cache()
    cycle_found = False
    sum_top = 0

    for (n_rock, rock) in enumerate(rocks()):
        if n_rock >= until:
            break

        rock.pos(2, chamber.top + 3)

        while True:
            (n_move, move) = next(moves)
            rock.move(chamber, move)

            if rock.stopped:
                break

        if not cycle_found:

            match cache(n_rock, n_move, chamber):

                case (n_rock_last, top_last):
                    cycle_found = True

                    size = n_rock - n_rock_last
                    repeats, rest = divmod(until - n_rock_last, size)

                    until = n_rock + rest
                    sum_top = (chamber.top - top_last) * (repeats - 1)

                case None:
                    pass

    print(chamber.top + sum_top)
