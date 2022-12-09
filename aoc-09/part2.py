# file_input = "data-training.txt"
# file_input = "data-training2.txt"
file_input = "data.txt"

num_knots = 10
rope = [(0, 0) for _ in range(num_knots)]
visited = {(0, 0)}


def move(x: int, y: int):

    rope[0] = (rope[0][0] + x, rope[0][1] + y)

    for knot in range(len(rope) - 1):
        (i, j) = rope[knot]
        (k, l) = rope[knot + 1]

        if abs(i - k) >= 2 or abs(j - l) >= 2:

            if i > k:
                k += 1
            elif i < k:
                k -= 1

            if j > l:
                l += 1
            elif j < l:
                l -= 1

        rope[knot + 1] = (k, l)

    visited.add(rope[-1])


with open(file_input) as f:
    for line in f:
        (m, n0) = line.split()
        n = int(n0)
        for i in range(n):
            match m:
                case "R":
                    move(1, 0)
                case "L":
                    move(-1, 0)
                case "U":
                    move(0, 1)
                case "D":
                    move(0, -1)

    print(len(visited))
