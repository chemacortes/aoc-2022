def priority(c: str) -> int:
    return (ord(c) - ord("a") + 1) if c.islower() else (ord(c) - ord("A") + 27)


def get_priority(line: str) -> int:
    n = len(line) // 2
    return next(priority(x) for x in line[:n] if x in line[n:])


# file_input = "data-training.txt"
file_input = "data.txt"

with open(file_input) as f:
    total = sum(get_priority(line) for line in f)


print(total)
