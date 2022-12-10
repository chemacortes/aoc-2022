# file_input = "data-training.txt"
file_input = "data.txt"

cycles = [20, 60, 100, 140, 180, 220]


def ticks(n: int):
    global cycle, regx, signal_strength

    for _ in range(n):
        cycle += 1
        if cycle in cycles:
            signal_strength += cycle * regx


if __name__ == "__main__":

    with open(file_input) as f:
        ops = [x[:-1] for x in f]

    cycle = 0
    regx = 1
    signal_strength = 0

    for op in ops:
        if not op:
            continue
        if op == "noop":
            ticks(1)
        else:
            ticks(2)
            (_, num) = op.split(" ")
            regx += int(num)

    print(signal_strength)
