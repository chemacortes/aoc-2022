# file_input = "data-training.txt"
file_input = "data.txt"

def step(cur):
    global map, dim

    p = map[cur][0]
    (i, j) = cur
    ns = []

    if i > 0:
        ns.append((i - 1, j))
    if i < dim[0]:
        ns.append((i + 1, j))
    if j > 0:
        ns.append((i, j - 1))
    if j < dim[1]:
        ns.append((i, j + 1))

    ns = [n for n in ns if map[n][1] == 0 and map[n][0] - p <= 1]

    return ns


if __name__ == "__main__":

    with open(file_input) as f:
        start = None
        end = None
        map = {}
        for (j, line) in enumerate(f):
            for (i, c) in enumerate(line[:-1]):
                if c not in ("E", "S"):
                    map[(i, j)] = [ord(c) - ord("a"), 0]
                elif c == "E":
                    end = (i, j)
                    map[(i, j)] = [ord("z") - ord("a"), 0]
                else:
                    start = (i, j)
                    map[(i, j)] = [0, 0]

        dim = max(map.keys())

    print((dim[0] + 1) * (dim[1] + 1))

    curs = {start}
    cont = 1
    while True:
        ns = set(sum((step(n) for n in curs), start=[]))
        for n in ns:
            map[n][1] = cont
        if end in ns:
            break
        curs = ns
        cont += 1

    print(cont)
