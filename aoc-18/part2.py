import os
from pathlib import Path

from util import Point3D, read


class Dim:
    def __init__(self, cubes: frozenset[Point3D]):

        self.max_x = max(x for (x, _, _) in cubes) + 1
        self.max_y = max(y for (_, y, _) in cubes) + 1
        self.max_z = max(z for (_, _, z) in cubes) + 1

        self.min_x = min(x for (x, _, _) in cubes) - 1
        self.min_y = min(y for (_, y, _) in cubes) - 1
        self.min_z = min(z for (_, _, z) in cubes) - 1

    @property
    def dims(self) -> tuple[int, int, int, int, int, int]:
        return (
            self.max_x,
            self.max_y,
            self.max_z,
            self.min_x,
            self.min_y,
            self.min_z,
        )

    def inside(self, p: Point3D) -> bool:
        x, y, z = p
        return (
            self.min_x <= x <= self.max_x
            and self.min_y <= y <= self.max_y
            and self.min_z <= z <= self.max_z
        )


def sides(dim: Dim) -> set[Point3D]:
    min_x, max_x, min_y, max_y, min_z, max_z = dim.dims
    return (
        {
            (i, j, k)
            for i in range(min_x, max_x + 1)
            for j in range(min_y, max_y + 1)
            for k in (min_z, max_z)
        }
        | {
            (i, j, k)
            for i in range(min_x, max_x + 1)
            for j in (min_y, max_y)
            for k in range(min_z, max_z + 1)
        }
        | {
            (i, j, k)
            for i in (min_x, max_x)
            for j in range(min_y, max_y + 1)
            for k in range(min_z, max_z + 1)
        }
    )


def neighbors(p: Point3D) -> set[Point3D]:
    (x, y, z) = p
    return {
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1),
    }


def outside(cubes: frozenset[Point3D]) -> set[Point3D]:

    dim = Dim(cubes)
    out = sides(dim)
    explored = out | cubes

    expand = out
    while expand:
        new_expand = {
            n for c in expand for n in neighbors(c) if dim.inside(n)
        } - explored

        explored |= new_expand
        out |= new_expand
        expand = new_expand

    return out


if __name__ == "__main__":

    os.chdir(Path(__file__).parent)

    TRAINING = False
    cubes = read("data-training.txt" if TRAINING else "data.txt")

    out = outside(cubes)
    surface = sum(1 for c in cubes for n in neighbors(c) if n in out)

    print(surface)
