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
    Monkey([79, 98], lambda x: x * 19, 23, 2, 3),
    Monkey([54, 65, 75, 74], lambda x: x + 6, 19, 2, 0),
    Monkey([79, 60, 97], lambda x: x * x, 13, 1, 3),
    Monkey([74], lambda x: x + 3, 17, 0, 1),
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
