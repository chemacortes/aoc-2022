import re
from dataclasses import dataclass

# types
NodeID = str
Distance = int


@dataclass
class Node:
    id: str
    flow: int
    neighbors: dict[NodeID, Distance]

    def __repr__(self):
        neighbors = ", ".join(
            f"{id}:{distance}"
            for (id, distance) in sorted(self.neighbors.items())
        )
        return f"Node({self.id}, flow={self.flow}, neighbors=({neighbors}))\n"


# read input file
def read(file_input: str) -> dict[NodeID, Node]:

    pat = re.compile(
        r"Valve ([A-Z]{2}) has flow rate=(\d+); .*valves? ([A-Z, ]+)"
    )

    with open(file_input) as f:

        nodes = {
            id: Node(id, int(flow), {s: 1 for s in neighbors.split(", ")})
            for line in f
            for (id, flow, neighbors) in pat.findall(line)
        }

    endpoints = set(nodes.keys())

    # growing map
    for node in nodes.values():
        distance = 1
        while missing := endpoints - set(node.neighbors) - {node.id}:
            new_neighbors = {
                n
                for (k, v) in node.neighbors.items()
                if v == distance
                for (n, dd) in nodes[k].neighbors.items()
                if dd == 1 and n in missing
            }

            distance += 1
            node.neighbors.update((k, distance) for k in new_neighbors)

    nulls = {n.id for n in nodes.values() if n.flow == 0}

    for node in nodes.values():
        node.neighbors = {
            n: v for (n, v) in node.neighbors.items() if n not in nulls
        }

    return nodes
