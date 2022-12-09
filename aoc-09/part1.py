# file_input = "data-training.txt"
file_input = "data.txt"


head = (0, 0)
tail = (0, 0)

visited = {(0, 0)}


def contiguous() -> bool:
    (i, j) = head
    (k, l) = tail

    return i - 1 <= k <= i + 1 and j - 1 <= l <= j + 1


def move(x: int, y: int):
    global head, tail

    head = (head[0] + x, head[1] + y)
    (i, j) = head
    (k, l) = tail

    if abs(i - k) >= 2 or abs(j - l) >= 2:

        if i > k:
            k += 1
        elif i < k:
            k -= 1

        if j > l:
            l += 1
        elif j < l:
            l -= 1

    tail = (k, l)
    visited.add(tail)


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
