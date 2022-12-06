from typing import Iterable

# file_input = "data-training.txt"
file_input = "data.txt"


def split(s: str) -> Iterable[str]:
    i = 0
    while i < len(s) - 14:
        yield s[i : i + 14]
        i += 1


def first_packet(s: str) -> int:
    return 14 + next(n for (n, t) in enumerate(split(s)) if len(set(t)) == 14)


with open(file_input) as f:
    for line in f:
        print(first_packet(line))
