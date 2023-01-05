import re
from dataclasses import dataclass

# types

Ore = int
Clay = int
Obsidian = int
Geode = int

Cost = tuple[Ore, Clay, Obsidian]

# globals
max_time = 24


@dataclass(frozen=True)
class Blueprint:
    cost_robot_ore: Cost
    cost_robot_clay: Cost
    cost_robot_obsidian: Cost
    cost_robot_geode: Cost

    @property
    def max_spend_ore(self) -> Ore:
        return self._max_spend(0)

    @property
    def max_spend_clay(self) -> Clay:
        return self._max_spend(1)

    @property
    def max_spend_obsidian(self) -> Obsidian:
        return self._max_spend(2)

    def _max_spend(self, i):
        return max(
            x[i]
            for x in (
                self.cost_robot_ore,
                self.cost_robot_clay,
                self.cost_robot_obsidian,
                self.cost_robot_geode,
            )
        )


def read(file_input: str) -> dict[int, Blueprint]:

    blueprints: dict[int, Blueprint] = {}
    with open(file_input) as f:
        for line in f:
            (i, ro, rc, ro1, ro2, rg1, rg2) = [
                int(x) for x in re.findall(r"\d+", line)
            ]  # type: ignore

            blueprints[i] = Blueprint(
                (ro, 0, 0), (rc, 0, 0), (ro1, ro2, 0), (rg1, 0, rg2)
            )

    return blueprints
