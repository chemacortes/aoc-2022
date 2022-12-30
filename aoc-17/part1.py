import os
from pathlib import Path

from util import Chamber, read, rocks


def show_step(msg: str, chamber, rock):
    print("\x1Bc")  # clear terminal
    print(msg)
    chamber.show(with_pos=rock.positions)
    input("Press any key...")


if __name__ == "__main__":

    os.chdir(Path(__file__).parent)

    TRAINING = False
    SHOW_STEPS = False
    SHOW_MOVE = False

    moves = read("data-training.txt" if TRAINING else "data.txt")

    chamber = Chamber()
    until = 2022

    for (n, rock) in enumerate(rocks()):
        if n == until:
            break

        rock.pos(2, chamber.top + 3)

        if SHOW_STEPS:
            show_step("New rock falls", chamber, rock)

        while not rock.stopped:
            move = next(moves)
            rock.move(chamber, move)

            if SHOW_STEPS:
                show_step(f"Move: {move.name} and falls 1", chamber, rock)

        if SHOW_MOVE:
            print("\x1Bc")  # clear terminal
            chamber.show()
            input("Press any key...")

    print(chamber.top)
