from dataclasses import dataclass
from typing import Callable


@dataclass
class Monkey:
    items: list[int]
    op: Callable[[int], int]
    div: int
    mt: int
    mf: int
    count: int = 0

    def round(self):
        global monkeys

        items = [self.op(x) // 3 for x in self.items]
        self.items.clear()

        for item in items:
            self.count += 1
            if item % self.div == 0:
                monkeys[self.mt].items.append(item)
            else:
                monkeys[self.mf].items.append(item)


monkeys: list[Monkey] = [
    Monkey([83, 62, 93], lambda x: x * 17, 2, 1, 6),
    Monkey([90, 55], lambda x: x + 1, 17, 6, 3),
    Monkey([91, 78, 80, 97, 79, 88], lambda x: x + 3, 19, 7, 5),
    Monkey([64, 80, 83, 89, 59], lambda x: x + 5, 3, 7, 2),
    Monkey([98, 92, 99, 51], lambda x: x * x, 5, 0, 1),
    Monkey([68, 57, 95, 85, 98, 75, 98, 75], lambda x: x + 2, 13, 4, 0),
    Monkey([74], lambda x: x + 4, 7, 3, 2),
    Monkey([68, 64, 60, 68, 87, 80, 82], lambda x: x * 19, 11, 4, 5),
]

print("Start")
print(monkeys)
print()


for r in range(1, 21):

    for monkey in monkeys:
        monkey.round()

    print(f"Round {r}")
    for i, m in enumerate(monkeys):
        print(
            f"Monkey {i} ({m.count:5}): {', '.join(str(x) for x in m.items)}"
        )
    print()

m1, m2 = sorted(monkeys, key=lambda x: x.count)[-2:]

business_level = m1.count * m2.count

print(business_level)
