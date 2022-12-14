from util import AIR, ROCK, SAND, read, show  # noqa

if __name__ == "__main__":  # noqa

    TRAINING = True

    data = read("data-training.txt" if TRAINING else "data.txt")

    bottom = max(y for (_, y) in data.keys())

    print(f"Bottom: {bottom}")
    show(data)

    while True:

        pos = (500, 0)
        while pos[1] < bottom:
            (x, y) = pos
            for n in ((x, y + 1), (x - 1, y + 1), (x + 1, y + 1)):
                if data.get(n, AIR) == AIR:
                    pos = n
                    break
            else:
                data[pos] = SAND
                # show(data, pos)
                break
        else:
            break

    res = sum(1 for v in data.values() if v == SAND)

    print(res)
    show(data)
