import os
from operator import itemgetter
from pathlib import Path

from util import NodeID, read

# types
Score = int
Minute = int
Visited = dict[NodeID, Minute]


def show(visited: Visited, maxtime: Minute):
    global nodes

    print("Visited nodes:")
    path = sorted(visited.items(), key=itemgetter(1), reverse=True)
    for (n, t) in path:
        if n == start:
            continue
        print(
            f"  minute {maxtime-t:2} "
            f"open valve {n} "
            f"Score: {nodes[n].flow*t : 4}"
        )

    score = sum(nodes[n].flow * t for (n, t) in path)
    print("Score:", score)


# Implementing a memoizer to use with traverse function
Args = tuple[NodeID, Minute, frozenset]
Result = tuple[Score, Visited]
memoize: dict[Args, Result] = {}


def traverse(
    current_node: NodeID,
    time: Minute,
    visited: Visited = {},
) -> Result:
    global nodes

    if time <= 0:
        return (0, visited)

    key: Args = (current_node, time, frozenset(visited.keys()))
    if key in memoize:
        return memoize[key]

    node = nodes[current_node]
    score = node.flow * time
    visit = {current_node: time}
    new_visited = visited | visit

    (childs_score, childs) = max(
        (
            traverse(neighbor, time - distance - 1, new_visited)
            for (neighbor, distance) in node.neighbors.items()
            if neighbor not in new_visited
        ),
        key=itemgetter(0),
        #       default=(0, new_visited),
    )

    memoize[key] = (score + childs_score, childs)
    return (score + childs_score, childs)


if __name__ == "__main__":

    os.chdir(Path(__file__).parent)

    TRAINING = False
    nodes = read("data-training.txt" if TRAINING else "data.txt")

    start: NodeID = "AA"
    maxtime: Minute = 30

    (score, visited) = traverse(start, time=maxtime)

    print(f"Score: {score}")
    show(visited, maxtime)
