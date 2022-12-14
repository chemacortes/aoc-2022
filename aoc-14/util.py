import sys
import time

ROCK = "#"
AIR = "."
SAND = "o"


def read(file_input: str) -> dict[tuple[int, int], str]:
    with open(file_input) as f:
        data = {}
        coords = [
            [
                (int(x), int(y))
                for (x, y) in (
                    coord.split(",") for coord in track.split(" -> ")
                )
            ]
            for track in f
        ]

        for coord in coords:
            for (c0, c1) in zip(coord, coord[1:]):
                (x0, y0) = c0
                (x1, y1) = c1

                if x0 == x1:
                    (y0, y1) = (min(y0, y1), max(y0, y1))
                    for j in range(y0, y1 + 1):
                        data[(x0, j)] = ROCK
                elif y0 == y1:
                    (x0, x1) = (min(x0, x1), max(x0, x1))
                    for i in range(x0, x1 + 1):
                        data[(i, y0)] = ROCK
                else:
                    print(c0, c1)
                    print(coords)
                    sys.exit("Tramo no esperado")

    return data


def show(data, pos=None):

    if pos is None:  # show all
        dim_x = (
            min(x for (x, y) in data.keys()) - 2,
            max(x for (x, y) in data.keys()) + 2,
        )
        dim_y = (
            min(y for (x, y) in data.keys()) - 2,
            max(y for (x, y) in data.keys()) + 2,
        )
    else:
        (x, y) = pos
        dim_x = (x - 10, x + 10)
        dim_y = (y - 10, y + 10)

    (i0, i1) = dim_x
    (j0, j1) = dim_y

    print(
        "    ",
        "".join(
            f"{'0' if i%10==0 else ' '}" if i != 500 else "+"
            for i in range(i0, i1)
        ),
    )
    for j in range(j0, j1):
        line = "".join(data.get((i, j), AIR) for i in range(i0, i1))
        print(f"{j:3} ", line)

    if pos is not None:
        time.sleep(0.2)
        print("\x1Bc")
