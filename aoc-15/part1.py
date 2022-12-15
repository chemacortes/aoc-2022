from util import distance, read

if __name__ == "__main__":

    TRAINING = False
    sensors = read("data-training.txt" if TRAINING else "data.txt")

    print(sensors)

    nline = 10 if TRAINING else 2000000

    beacons = {}
    for k, v in sensors.items():
        (x, y) = k
        (w, z) = v

        d = distance(k, v)
        e = d - abs(nline - y)
        if e >= 0:
            for i in range(x - e, x + e + 1):
                beacons[i, nline] = "#"

    for k, v in sensors.items():
        beacons[k] = "S"
        beacons[v] = "B"

    for j in range(-2, 20):
        print("".join(beacons.get((i, j), ".") for i in range(-5, 30)))

    print()

    print(sum(1 for k in beacons if k[1] == nline and beacons[k] == "#"))
