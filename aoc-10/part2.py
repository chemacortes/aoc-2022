# file_input = "data-training.txt"
file_input = "data.txt"


def ticks(n: int):
    global cycle, regx, crt

    for _ in range(n):
        if regx - 1 <= cycle % 40 <= regx + 1:
            crt += "#"
        else:
            crt += "."
        cycle += 1

    # print(cycle, regx, crt)


def show(crt: str):
    for l in range(6):
        s = l * 40
        print(crt[s : s + 40])


if __name__ == "__main__":

    with open(file_input) as f:
        ops = [x[:-1] for x in f]

    cycle = 0
    regx = 1
    crt = ""

    for op in ops:
        if op == "noop":
            ticks(1)
        else:
            ticks(2)
            (_, num) = op.split(" ")
            regx += int(num)

        print(cycle, regx, crt)

    show(crt)
