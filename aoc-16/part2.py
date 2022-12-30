import os
from dataclasses import astuple, dataclass, replace
from enum import IntEnum
from operator import attrgetter
from pathlib import Path
from typing import Iterable, Mapping

from util import NodeID, read

# types
Score = int
Time = int


class Op(IntEnum):
    PERSON = 1
    ELEPHANT = 2
    MONKEY = 3

    def __repr__(self):
        return self.name.capitalize()


@dataclass
class Operator:
    op: Op
    time: Time
    pos: NodeID

    def __repr__(self):
        return f"{self.op!r}(time={self.time}, pos={self.pos})"

    def distance(self, node: NodeID):
        return nodes[self.pos].neighbors[node]

    def same_pos(self, other: "Operator") -> bool:
        return (self.pos, self.time) == (other.pos, other.time)


Visited = Mapping[NodeID, Operator]
Operators = tuple[Operator, ...]


# Score calculation
def calc_score(visited: Visited) -> Score:
    global nodes
    return sum(nodes[n].flow * op.time for (n, op) in visited.items())


# Show moves
def show(visited: Visited):
    global start, maxtime

    print(f"Score: {calc_score(visited)}")
    print("-" * 30)
    path = sorted(visited.values(), key=attrgetter("time"), reverse=True)
    for operator in path:
        op, time, pos = astuple(operator)
        if operator.pos == start:
            continue
        print(
            f" minute {maxtime-time:2} "
            f"{op!r:8} opens valve {pos} "
            f"Release: {nodes[pos].flow*time:4}"
        )


def select(operators: Operators) -> Iterable[tuple[Operator, Operators]]:
    for v in operators:
        yield (v, tuple(x for x in operators if x.op != v.op))


# Implementing a memoizer to use with traverse function
class Memoize:
    def __init__(self):
        self._memoize = {}

    def register(self, visited: Visited, score: Score) -> bool:
        key = frozenset(visited)
        if key in self._memoize and score < self._memoize[key]:
            return False
        self._memoize[key] = score
        return True


def traverse(operators: Operators, visited: Visited) -> Visited:

    global nodes, endpoints
    global max_score, memoize

    score = calc_score(visited)

    # print partial solutions
    if score > max_score:
        max_score = score
        show(visited)
        print()

    # memoization
    if not memoize.register(visited, score):
        return visited

    # Shortcutting (simetrical paths)
    if operators != tuple(sorted(operators, key=attrgetter("time"))):
        return {}

    missing = endpoints - frozenset(visited)

    visited = max(
        (
            traverse(
                (move_operator, *waiting_operators),
                visited | {neighbor: move_operator},
            )
            for (neighbor, move_operator, waiting_operators) in (
                (
                    node,
                    replace(
                        operator,
                        time=operator.time - operator.distance(node) - 1,
                        pos=node,
                    ),
                    waiting_operators,
                )
                for node in missing
                for (operator, waiting_operators) in select(operators)
            )
            if move_operator.time > 0
        ),
        key=calc_score,
        default=visited,
    )

    return visited


def solution(ops: tuple[Op, ...]):
    global start, maxtime, max_score

    maxtime -= (len(ops) - 1) * 4
    max_score = 0

    operators: Operators = tuple(Operator(op, maxtime, start) for op in ops)
    visited: Visited = {start: operators[0]}
    visited = traverse(operators, visited)

    print("-" * 30)
    print("SOLUTION".center(30))
    print("-" * 30)
    show(visited)


if __name__ == "__main__":

    start = "AA"
    maxtime: Time = 30
    max_score = 0
    memoize = Memoize()

    os.chdir(Path(__file__).parent)

    TRAINING = False
    nodes = read("data-training.txt" if TRAINING else "data.txt")
    endpoints = frozenset(k for k, n in nodes.items() if n.flow > 0)

    ops = (Op.ELEPHANT, Op.PERSON)
    solution(ops)

    # Equivalente to Part 1
    #  ops = (Op.PERSON,)  # part1
    #  solution(ops)

    # Solution with three operators
    #  ops = (Op.ELEPHANT, Op.MONKEY, Op.PERSON)
    #  solution(ops)
