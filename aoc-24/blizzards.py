Dims = tuple[int, int]  # rows x cols
Pos = tuple[int, int]
Grid = set[Pos]


class Blizzards:
    def __init__(
        self, dims: Dims, right: Grid, down: Grid, left: Grid, up: Grid
    ):
        self.dims = dims
        # one set of blizzards by direction
        self.blizzs = [(right, down, left, up)]

    def generate(self, round: int):

        if round < len(self.blizzs):
            return

        # generate previous rounds
        for r in range(len(self.blizzs), round):
            self.generate(r)

        # generate the last round
        rows, cols = self.dims
        right, down, left, up = self.blizzs[round - 1]

        self.blizzs.append(
            (
                {(r, (c + 1) if c < cols else 1) for (r, c) in right},
                {((r + 1) if r < rows else 1, c) for (r, c) in down},
                {(r, (c - 1) if 1 < c else cols) for (r, c) in left},
                {((r - 1) if 1 < r else rows, c) for (r, c) in up},
            )
        )

    def isfree(self, round: int, pos: Pos) -> bool:

        if round >= len(self.blizzs):
            self.generate(round)

        r, c = pos
        rows, cols = self.dims
        return (
            1 <= r <= rows
            and 1 <= c <= cols
            and any(pos in blizz for blizz in self.blizzs[round])
        )

    def show(self, round: int = 0):

        self.generate(round)

        rows, cols = self.dims
        right, down, left, up = self.blizzs[round]

        print("#." + "#" * cols)
        for row in range(1, rows + 1):
            print("#", end="")
            for col in range(1, cols + 1):
                c = ""
                if (row, col) in right:
                    c += ">"
                if (row, col) in down:
                    c += "v"
                if (row, col) in left:
                    c += "<"
                if (row, col) in up:
                    c += "^"

                if len(c) == 0:
                    c = "."
                elif len(c) > 1:
                    c = str(len(c))

                print(c, end="")
            print("#")
        print("#" * cols + ".#")


def load_blizzards(file_input: str) -> Blizzards:

    right: set[Pos] = set()
    down: set[Pos] = set()
    left: set[Pos] = set()
    up: set[Pos] = set()

    rows = 0
    with open(file_input) as f:
        first = f.readline()
        cols = len(first) - 3

        for row, line in enumerate(f, start=1):
            if line[1] == "#":  # last row
                rows = row - 1
                break
            for col, c in enumerate(line):
                match c:
                    case ">":
                        right.add((row, col))
                    case "v":
                        down.add((row, col))
                    case "<":
                        left.add((row, col))
                    case "^":
                        up.add((row, col))
                    case _:
                        pass

    return Blizzards((rows, cols), right, down, left, up)


if __name__ == "__main__":

    # blizzards = load_blizzards("data-training-1.txt")
    blizzards = load_blizzards("data.txt")

    for r in range(10):
        print(f"\nRound {r}")
        blizzards.show(round=r)
