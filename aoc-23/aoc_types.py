from dataclasses import dataclass

Pos = tuple[int, int]
Dir = int  # Literal[0, 1, 2, 3]  # "N", "S", "W", "E"


@dataclass(frozen=True)
class Elf:
    pos: Pos
    dir: Dir = 0


Grid = dict[Pos, Elf]
