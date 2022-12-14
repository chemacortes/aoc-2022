file_input = "data-training.txt"
# file_input = "data.txt"

ROCK = "#"
AIR = "."
SAND = "o"


if __name__ == "__main__":
    with open(file_input) as f:
        data = {}
        for track in f:
            coords = [
                (int(x), int(y))
                for (x, y) in (
                    coord.split(",") for coord in track.split(" -> ")
                )
            ]

        for (c0, c1) in zip(coords, coords[1:]):
            (x0, y0) = c0
            (x1, y1) = c1

            if x0 == x1:
                (y0, y1) = (min(y0, y1), max(y0, y1))
                for j in range(y0, y1 + 1):
                    data[(x0, j)] = ROCK
            if y0 == y1:
                (x0, x1) = (min(x0, x1), max(x0, x1))
                for i in range(x0, x1 + 1):
                    data[(i, y0)] = ROCK

    bottom = max(y for (_, y) in data.keys())

    print(bottom, data)

    while True:

        pos = (500, 0)
        while pos[1] < bottom:
            (x, y) = pos
            for n in ((x, y + 1), (x - 1, y + 1), (x + 1, y + 1)):
                if data.get(n, AIR) == AIR:
                    pos = n
                    print(pos)
                    break
            else:
                data[pos] = SAND
                print(data)
                break
        else:
            break

    res = sum(1 for v in data.values() if v == SAND)

    print(res)
    print(data)
