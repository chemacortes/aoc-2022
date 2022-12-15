import re

pat = re.compile(
    "Sensor at x=([-]?\d+), y=([-]?\d+): closest beacon is at x=([-]?\d+), y=([-]?\d+)"
)


def read(file_input: str):

    with open(file_input) as f:
        sensors = {
            (int(x), int(y)): (int(w), int(z))
            for (x, y, w, z) in pat.findall(f.read())
        }

    return sensors


def distance(p: tuple[int, int], q: tuple[int, int]) -> int:
    """Distance function in Manhatan Geometry
    https://en.wikipedia.org/wiki/Taxicab_geometry"""

    (x, y) = p
    (w, z) = q

    return abs(x - w) + abs(y - z)
