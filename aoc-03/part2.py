def priority(c: str) -> int:
    return (ord(c) - ord("a") + 1) if c.islower() else (ord(c) - ord("A") + 27)


def get_priority(line1: str, line2: str, line3: str) -> int:
    return next(priority(x) for x in line1 if x in line2 and x in line3)


# file_input = "data-training.txt"
file_input = "data.txt"

with open(file_input) as f:

    total = sum(get_priority(l1, l2, l3) for (l1, l2, l3) in zip(f, f, f))


print(total)
