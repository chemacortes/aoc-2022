Dims = tuple[int, int]  # rows x cols
Pos = tuple[int, int]
Grid = set[Pos]


class Blizzards:
    def __init__(
        self, dims: Dims, right: Grid, down: Grid, left: Grid, up: Grid
    ):
        self.dims = dims

        # one set of blizzards by direction
        # really, only need the last tuple of blizzards
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
            and all(pos not in blizz for blizz in self.blizzs[round])
        )

    def blizz(self, round: int, positions: set[Pos]) -> set[Pos]:

        if round >= len(self.blizzs):
            self.generate(round)

        rows, cols = self.dims
        right, down, left, up = self.blizzs[round]

        positions2 = {
            (r, c) for (r, c) in positions if 1 <= r <= rows and 1 <= c <= cols
        }

        return positions2 - right - down - left - up

    def show(self, round: int = 0, grid: set[Pos] = set()):

        self.generate(round)

        rows, cols = self.dims
        right, down, left, up = self.blizzs[round]

        print(f"\nRound: {round}")
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

                match len(c):
                    case 0:
                        c = "."
                    case 1:
                        pass
                    case n if n < 10:
                        c = str(n)
                    case _:
                        c = "*"

                if (row, col) in grid:
                    c = "E" if c == "." else "W"  # W = WRONG

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

    # blizzards = load_blizzards("data-training-0.txt")
    blizzards = load_blizzards("data-training.txt")

    for r in range(19):
        blizzards.show(round=r)
