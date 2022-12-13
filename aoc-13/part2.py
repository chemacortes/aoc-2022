from functools import cmp_to_key

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
        data = [eval(z) for pair in s for z in pair] + [[[2]], [[6]]]

    cmpkey = cmp_to_key(compare)
    sorted_data = sorted(data, key=cmpkey, reverse=True)

    i = sorted_data.index([[2]]) + 1
    j = sorted_data.index([[6]]) + 1

    print(i * j)
