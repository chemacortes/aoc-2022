import os
from itertools import zip_longest
from pathlib import Path

from util import read

values = {"0": 0, "1": 1, "2": 2, "-": -1, "=": -2}


def snafu(nums: list[str]) -> int:
    return 0


def snafu_sum(digits: tuple[str], acc: int = 0) -> tuple[str, int]:

    res = acc + sum(values[c] for c in digits)
    n, r = divmod(res, 5)

    if r >= 3:
        n += 1

    return ("012=-"[r], n)


if __name__ == "__main__":

    os.chdir(Path(__file__).parent)

    TRAINING = False
    data = read("data-training.txt" if TRAINING else "data.txt")

    print(data)

    acc = 0
    res = ""

    for digits in zip_longest(*(num[::-1] for num in data), fillvalue="0"):
        c, acc = snafu_sum(digits, acc)
        res = c + res
        print(res)

    print(res)
