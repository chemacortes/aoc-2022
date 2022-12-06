# file_input = "data-training.txt"
file_input = "data.txt"


def first_packet(s: str) -> int:
    return 4 + next(
        n
        for (n, t) in enumerate(zip(s, s[1:], s[2:], s[3:]))
        if len(set(t)) == 4
    )


with open(file_input) as f:
    for line in f:
        print(first_packet(line))
