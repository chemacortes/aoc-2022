# A -> Rock
# B -> Paper
# C -> Scissors

# X -> Rock
# Y -> Paper
# Z -> Scissors

values = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}


def result(i: str, j: str) -> int:

    match (i, j):

        # lost
        case ("A", "Z") | ("B", "X") | ("C", "Y"):
            return 0

        # win
        case ("A", "Y") | ("B", "Z") | ("C", "X"):
            return 6

        # draw
        case _:
            return 3


def score(i: str, j: str) -> int:
    return values[j] + result(i, j)


# with open("data-training.txt") as f:
with open("data.txt") as f:
    data = [line.split() for line in f]

full_score = sum(score(i, j) for (i, j) in data)

print(full_score)
