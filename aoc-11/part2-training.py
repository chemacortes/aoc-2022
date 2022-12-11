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

        for item in self.items:
            item %= modulador
            res = self.op(item)
            if res % self.div == 0:
                monkeys[self.mt].items.append(res)
            else:
                monkeys[self.mf].items.append(res)

        self.count += len(self.items)
        self.items.clear()


modulador = 23 * 19 * 13 * 17

monkeys: list[Monkey] = [
    Monkey([79, 98], lambda x: x * 19, 23, 2, 3),
    Monkey([54, 65, 75, 74], lambda x: x + 6, 19, 2, 0),
    Monkey([79, 60, 97], lambda x: x * x, 13, 1, 3),
    Monkey([74], lambda x: x + 3, 17, 0, 1),
]

print("Start")
print(monkeys)
print()


for r in range(1, 10001):

    for monkey in monkeys:
        monkey.round()

    if r == 20 or r % 1000 == 0:
        print(f"Round {r}")
        for i, m in enumerate(monkeys):
            print(f"Monkey {i} ({m.count:5})")
        print()


m1, m2 = sorted(monkeys, key=lambda x: x.count)[-2:]

business_level = m1.count * m2.count

print(business_level)
