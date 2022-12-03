# A -> Rock
# B -> Paper
# C -> Scissors

# X -> Lose
# Y -> Draw
# Z -> Win

values = {"A": 1, "B": 2, "C": 3, "X": 0, "Y": 3, "Z": 6}

strategy = {
    "X": {"A": "C", "B": "A", "C": "B"},
    "Y": {"A": "A", "B": "B", "C": "C"},
    "Z": {"A": "B", "B": "C", "C": "A"},
}


def score(i: str, j: str) -> int:
    return values[strategy[j][i]] + values[j]


# with open("aoc-02-training.txt") as f:
with open("aoc-02.txt") as f:
    data = [line.split() for line in f]

full_score = sum(score(i, j) for (i, j) in data)

print(full_score)
