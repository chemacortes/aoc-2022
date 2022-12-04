# file_input = "data-training.txt"
file_input = "data.txt"


def split(line: str) -> tuple[range, range]:
    (x, y) = line.split(",")
    (i, j) = x.split("-")
    (k, l) = y.split("-")
    return (range(int(i), int(j) + 1), range(int(k), int(l) + 1))


def overlap(r1: range, r2: range) -> bool:
    return any(i in r2 for i in r1) or any(j in r1 for j in r2)


with open(file_input) as f:
    pairs = [split(line) for line in f]
    res = sum(1 for x, y in pairs if overlap(x, y))

# for p, q in pairs:
#     print(p, q, overlap(p, q))
print(res)
