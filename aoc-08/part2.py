# file_input = "data-training.txt"
file_input = "data.txt"


def score(grid, d, dim) -> int:
    (i, j) = d
    (n, m) = dim
    x = grid[(i, j)]

    res = 1

    p = 0
    for ii in range(i - 1, -1, -1):
        p += 1
        if grid[(ii, j)] >= x:
            break
    res *= p

    p = 0
    for ii in range(i + 1, n):
        p += 1
        if grid[(ii, j)] >= x:
            break
    res *= p

    p = 0
    for jj in range(j - 1, -1, -1):
        p += 1
        if grid[(i, jj)] >= x:
            break
    res *= p

    p = 0
    for jj in range(j + 1, m):
        p += 1
        if grid[(i, jj)] >= x:
            break
    res *= p

    return res


with open(file_input) as f:
    data = f.read().split()
    n = len(data[0])
    m = len(data)
    grid = {(i, j): int(data[i][j]) for i in range(n) for j in range(m)}
    print(max(score(grid, d, (n, m)) for d in grid))
