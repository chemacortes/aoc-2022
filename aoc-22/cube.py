from aoc22_types import DOWN, LEFT, RIGHT, UP, Face, Pos, Schema

schema1: Schema = {
    (1, 3): {RIGHT: ((3, 4), LEFT), LEFT: ((2, 2), DOWN), UP: ((2, 1), DOWN)},
    (2, 1): {DOWN: ((3, 3), UP), LEFT: ((3, 4), UP), UP: ((1, 3), DOWN)},
    (2, 2): {DOWN: ((3, 3), RIGHT), UP: ((1, 3), RIGHT)},
    (2, 3): {RIGHT: ((3, 4), DOWN)},
    (3, 3): {DOWN: ((2, 1), UP), LEFT: ((2, 2), UP)},
    (3, 4): {RIGHT: ((1, 3), LEFT), DOWN: ((2, 1), RIGHT), UP: ((2, 3), LEFT)},
}

schema2: Schema = {
    (1, 2): {LEFT: ((3, 1), RIGHT), UP: ((4, 1), RIGHT)},
    (1, 3): {RIGHT: ((3, 2), LEFT), DOWN: ((2, 2), LEFT), UP: ((4, 1), UP)},
    (2, 2): {RIGHT: ((1, 3), UP), LEFT: ((3, 1), DOWN)},
    (3, 1): {LEFT: ((1, 2), RIGHT), UP: ((2, 2), RIGHT)},
    (3, 2): {RIGHT: ((1, 3), LEFT), DOWN: ((4, 1), LEFT)},
    (4, 1): {RIGHT: ((3, 2), UP), DOWN: ((1, 3), DOWN), LEFT: ((1, 2), DOWN)},
}


def cube_front(
    pos: Pos, face: Face, schema: Schema, side: int
) -> tuple[Pos, Face]:
    x, y = (pos[0] - 1, pos[1] - 1)
    sector = (1 + x // side, 1 + y // side)

    # translation to sector (1,1)
    (x0, y0) = (x % side, y % side)
    dest_sector, dest_face = schema[sector][face]

    # rotation
    rot = (dest_face - face) % 4
    (x1, y1) = [
        (x0, y0),
        (y0, side - x0 - 1),
        (side - x0 - 1, side - y0 - 1),
        (side - y0 - 1, x0),
    ][rot]

    # front
    if dest_face == RIGHT:
        y1 = (y1 + 1) % side
    elif dest_face == DOWN:
        x1 = (x1 + 1) % side
    elif dest_face == LEFT:
        y1 = (y1 - 1) % side
    elif dest_face == UP:
        x1 = (x1 - 1) % side

    # translate to dest_sector
    n, m = dest_sector
    pos1 = (x1 + 1 + (n - 1) * side, y1 + 1 + (m - 1) * side)

    return pos1, dest_face
