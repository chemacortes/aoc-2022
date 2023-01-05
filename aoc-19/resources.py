from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import cast

from puzzle import Clay, Cost, Geode, Obsidian, Ore

# types
Value = tuple[Geode, Obsidian, Clay, Ore]
Robots = tuple[int, int, int, int]
Time = int

material_types = (
    "ore",
    "clay",
    "obsidian",
    "geode",
)


@dataclass
class Resources:

    time: Time

    ore: Ore = 0
    clay: Clay = 0
    obsidian: Obsidian = 0
    geode: Geode = 0

    robots_ore: int = 1
    robots_clay: int = 0
    robots_obsidian: int = 0
    robots_geode: int = 0

    max_time: Time = field(default=-1, compare=False, kw_only=True)
    trace: tuple[str, ...] = field(default=(), compare=False, kw_only=True)

    def __repr__(self):
        return (
            f"Resources(time={self.time}, store={self.store}, "
            f"robots={self.robots}, value={self.value})"
        )

    def show(self):
        for r in self.trace:
            print(r)
        print(self)

    def active_trace(self):
        self.max_time = self.time

    @property
    def value(self) -> Value:
        return (
            self.geode + self.robots_geode * self.time,
            self.obsidian + self.robots_obsidian * self.time,
            self.clay + self.robots_clay * self.time,
            self.ore + self.robots_ore * self.time,
        )

    @property
    def store(self) -> Value:
        return (self.ore, self.clay, self.obsidian, self.geode)

    @property
    def robots(self) -> Robots:
        return (
            self.robots_ore,
            self.robots_clay,
            self.robots_obsidian,
            self.robots_geode,
        )

    def replace(self, time: Time, store: Value, robots: Robots) -> Resources:
        return Resources(
            time,
            *store,
            *robots,
            max_time=self.max_time,
            trace=self.trace,
        )

    def time_cost(self, cost: Cost) -> Time | None:

        # need to extract these materials
        need = tuple(
            0 if (b == 0 or a >= b) else b - a
            for a, b in zip((self.ore, self.clay, self.obsidian), cost)
        )

        # we have robots to extract these materials?
        if any(r == 0 for r, n in zip(self.robots, need) if n > 0):
            return None

        spend_time = max(
            (math.ceil(n / r) for r, n in zip(self.robots, need) if n > 0),
            default=0,
        )

        return spend_time

    def produce(self, time: Time = 1) -> Resources:

        spend_time = min(self.time, time)
        production = cast(
            Value,
            tuple(i + j * spend_time for i, j in zip(self.store, self.robots)),
        )

        res = self.replace(self.time - spend_time, production, self.robots)
        res.add_trace()
        return res

    def make_robot(self, robot_type: str, cost) -> Resources | None:

        if self.time <= 0:
            return None

        inc_robots = (
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (0, 0, 1, 0),
            (0, 0, 0, 1),
        )[material_types.index(robot_type)]

        if any(i < k for i, k in zip(self.store, cost + (0,))):
            print("FAIL", self, robot_type, cost)
            return None

        production = cast(
            Value,
            tuple(i - k for i, k in zip(self.store, cost + (0,))),
        )
        robots = cast(
            Robots, tuple(i + j for i, j in zip(self.robots, inc_robots))
        )

        # assertion
        if any(x < 0 for x in production):
            print("FALLA")
            return None

        res = self.replace(self.time, production, robots)
        res.add_trace(f" <<< new {robot_type} robot")
        return res

    def add_trace(self, msg: str = ""):
        if self.max_time > 0:
            self.trace = self.trace + (
                f"{self.max_time-self.time:2} {self!r} ".ljust(90) + msg,
            )
