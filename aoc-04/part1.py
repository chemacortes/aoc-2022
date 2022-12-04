# file_input = "data-training.txt"
file_input = "data.txt"


def split(line: str) -> tuple[tuple[int, int], tuple[int, int]]:
    (x, y) = line.split(",")
    (i, j) = x.split("-")
    (k, l) = y.split("-")
    return ((int(i), int(j)), (int(k), int(l)))


def contains(r1: tuple[int, int], r2: tuple[int, int]) -> bool:
    return (r1[0] >= r2[0] and r1[1] <= r2[1]) or (
        r1[0] <= r2[0] and r1[1] >= r2[1]
    )


with open(file_input) as f:
    pairs = [split(line) for line in f]
    res = sum(1 for x, y in pairs if contains(x, y))

print(res)
