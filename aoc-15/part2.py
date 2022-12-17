from itertools import combinations
from typing import Iterable

from util import distance, read


def ball(pos: tuple[int, int], radius: int) -> Iterable[tuple[int, int]]:
    """Return a ball around a position in Manhatan geometry.
    They include the coordinate's limit `m`."""

    global max_coordinate

    (x, y) = pos

    # Vertices
    for (i, j) in (
        (x - radius, y),
        (x + radius, y),
        (x, y - radius),
        (x, y + radius),
    ):
        if 0 <= i <= max_coordinate and 0 <= j <= max_coordinate:
            yield (i, j)

    # sides of the ball
    for j in range(max(1, y - radius), min(max_coordinate, y + radius)):
        i = x - radius + abs(y - j)
        if 0 <= i <= max_coordinate:
            yield (i, j)
        i = x + radius - abs(y - j)
        if 0 <= i <= max_coordinate:
            yield (i, j)


if __name__ == "__main__":

    TRAINING = False
    sb = read("data-training.txt" if TRAINING else "data.txt")
    max_coordinate = 20 if TRAINING else 4000000

    # transform dict[Sensor, Beacon] --> dict[Sensor, Radius]
    sensors = {
        sensor: distance(sensor, beacon) for (sensor, beacon) in sb.items()
    }

    # Hay exáctamente una única posición donde puede estar el beacon defectuoso,
    # por lo tanto tiene que estar adjunto al límite de detección de alguno de
    # los sensores. Si estuviera a más distancia, querría decir que hay más
    # posiciones posibles ya que habría más posiciones desde el límite de un
    # sensor hasta llegar a beacon defectuoso.
    #
    # Por lo tanto, miramos las posiciones en la frontera de detección de los
    # sensores en busca de alguna posición a la que no alcancen el resto de
    # sensores.
    #
    # La frontera de detección será el bolo (ball) de radio limite+1
    #
    # Por otro lado, para que sólo haya una única posición, ésta debe ser
    # frontera de al menos 4 sensores (siempre que no sea algún punto en los
    # límites del tablero)

    for (s, r) in sensors.items():
        for pos in ball(s, r + 1):

            if any(
                distance(ss, pos) <= dd
                for (ss, dd) in sensors.items()
                if ss != s
            ):
                # position detected
                continue

            # position not detected
            (x, y) = pos
            print(f"Out range position: {x=}, {y=}")
            print(f"Frecuency: {4000000*x+y}")
            break
        else:
            continue

        break
