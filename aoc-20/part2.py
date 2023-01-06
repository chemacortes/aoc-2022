import os
from pathlib import Path

from util import read


def debug(res):
    if TRAINING:
        print(", ".join(f"{n:2}" for _, n in res))


if __name__ == "__main__":

    os.chdir(Path(__file__).parent)

    TRAINING = False
    data = read("data-training.txt" if TRAINING else "data.txt")

    DECRYPTION_KEY = 811589153
    REPEATS = 10

    data = [n * DECRYPTION_KEY for n in data]
    size = len(data)

    initial = list(enumerate(data))
    res = initial[:]

    for round in range(REPEATS):

        for e in initial:
            _, n = e
            if n == 0:
                zero = e
                continue

            pos = res.index(e)

            # reset list
            res = res[pos + 1 :] + res[:pos]  # noqa
            res.insert(n % (size - 1), e)

        # reset to zero
        pos = res.index(zero)
        res = res[pos:] + res[:pos]
        debug(res)

    positions = [i % size for i in (1000, 2000, 3000)]
    print(positions)
    numbers = [res[i][1] for i in positions]
    print(numbers, sum(numbers))
