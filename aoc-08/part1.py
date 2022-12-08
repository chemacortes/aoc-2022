# file_input = "data-training.txt"
file_input = "data.txt"


def visible(grid, d, dim):
    (i, j) = d
    (n, m) = dim

    if i == 0 or j == 0 or i == n - 1 or j == m - 1:
        return True

    x = grid[(i, j)]
    return (
        all(grid[(i, jj)] < x for jj in range(j))
        or all(grid[(i, jj)] < x for jj in range(j + 1, m))
        or all(grid[(ii, j)] < x for ii in range(i))
        or all(grid[(ii, j)] < x for ii in range(i + 1, n))
    )


with open(file_input) as f:
    data = f.read().split()
    n = len(data[0])
    m = len(data)
    grid = {(i, j): int(data[i][j]) for i in range(n) for j in range(m)}
    print(sum(1 for k in grid.keys() if visible(grid, k, (n, m))))
