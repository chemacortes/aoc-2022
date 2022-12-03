with open("data.txt") as f:
    calories = sorted(
        sum(int(cal) for cal in elf.split()) for elf in f.read().split("\n\n")
    )

top_calories = calories[-1]
top_three = sum(calories[-3:])

print(top_calories, top_three)
