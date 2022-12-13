# file_input = "data-training.txt"
file_input = "data.txt"


def compare(left, right) -> int:

    match (left, right):
        case ([], []):
            return 0

        case ([], _):
            return 1

        case (_, []):
            return -1

        case ([x, *xs], [y, *ys]):

            match (x, y):

                case (int(), int()):
                    if x == y:
                        return compare(xs, ys)
                    else:
                        return 1 if x < y else -1

                case (int(), list()):
                    res = compare([x], y)
                    return res if res != 0 else compare(xs, ys)

                case (list(), int()):
                    res = compare(x, [y])
                    return res if res != 0 else compare(xs, ys)

                case _:
                    res = compare(x, y)
                    return res if res != 0 else compare(xs, ys)

        case _:
            return -99


if __name__ == "__main__":
    with open(file_input) as f:
        s = [z.split() for z in f.read().split("\n\n")]
        data = [(eval(x), eval(y)) for (x, y) in s]

    print(
        sum(
            i
            for (i, (left, right)) in enumerate(data, start=1)
            if compare(left, right) == 1
        )
    )
