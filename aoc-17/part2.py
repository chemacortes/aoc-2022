import os
from pathlib import Path

from util import Chamber, read2, rocks

if __name__ == "__main__":

    os.chdir(Path(__file__).parent)

    TRAINING = False

    moves = read2("data-training.txt" if TRAINING else "data.txt")

    chamber = Chamber()
    until = 1000000000000
    NUMROCKS = 5

    seen: dict[tuple, tuple] = {}
    found_repeat = False
    sum_top = 0

    for (n, rock) in enumerate(rocks()):
        if n >= until:
            break

        rock.pos(2, chamber.top + 3)

        while not rock.stopped:
            (mi, move) = next(moves)
            rock.move(chamber, move)

        if not found_repeat:
            key = (n % NUMROCKS, mi, chamber.base())
            if key in seen:
                found_repeat = True
                last_n, last_top = seen[key]
                size = n - last_n

                repeats, rest = divmod(until - last_n, size)
                repeats -= 1

                until = n + rest
                sum_top = (chamber.top - last_top) * repeats
            else:
                seen[key] = (n, chamber.top)

    print(chamber.top + sum_top)
