from dataclasses import dataclass
from typing import Literal, cast

Ops = Literal["+", "-", "/", "*"]


@dataclass
class Monkey:
    name: str


@dataclass
class Number(Monkey):
    number: int


@dataclass
class Operator(Monkey):
    left: str
    right: str
    op: Ops


def read(file_input: str):
    data: dict[str, Monkey] = {}
    with open(file_input) as f:
        for line in f:
            match line.split():
                case (m, n):
                    name = m.strip(":")
                    data[name] = Number(name, int(n))
                case (m, m1, op, m2):
                    name = m.strip(":")
                    data[name] = Operator(name, m1, m2, cast(Ops, op))
    return data
