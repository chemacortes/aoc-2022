import re

# file_input = "data-training.txt"
# HIGH: int = 3
# STACKS = 3

file_input = "data.txt"
HIGH: int = 8
STACKS = 9

pat = re.compile(" ".join(".(.)." for _ in range(STACKS)))
order = re.compile("move (\d+) from (\d) to (\d)")


def move(docks: list, num: int, frm: int, to: int):
    docks[to - 1][0:0] = docks[frm - 1][:num]
    del docks[frm - 1][:num]


docks: list = [[] for _ in range(STACKS)]


with open(file_input) as f:
    for (n, line) in enumerate(f, start=1):
        for (j, cargo) in enumerate(pat.findall(line)[0]):
            if cargo != " ":
                docks[j].append(cargo)

        if n == HIGH:
            break

    print(docks)

    moves = [order.findall(line)[0] for line in f if line.startswith("move")]
    print(moves)

    for (num, i, j) in moves:
        move(docks, int(num), int(i), int(j))

print("".join(x[0] for x in docks))
