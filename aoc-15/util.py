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
