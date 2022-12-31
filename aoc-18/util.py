Point3D = tuple[int, int, int]


def unpack(s: str) -> tuple[int, int, int] | None:
    match s.split(","):
        case (x, y, z):
            return (int(x), int(y), int(z))
        case _:
            return None


def read(file_input: str) -> frozenset[Point3D]:
    with open(file_input) as f:
        data = f.read()

    return frozenset(
        (x, y, z)
        for (x, y, z) in (
            pos
            for pos in (unpack(line) for line in data.split("\n"))
            if pos is not None
        )
    )
