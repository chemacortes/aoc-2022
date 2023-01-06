import os
from pathlib import Path
from pprint import pprint
from typing import cast

from util import Number, Operator, read

if __name__ == "__main__":

    os.chdir(Path(__file__).parent)

    TRAINING = False
    data = read("data-training.txt" if TRAINING else "data.txt")

    pprint(data)

    numbers = {
        name: monkey
        for name, monkey in data.items()
        if isinstance(monkey, Number)
    }

    while True:

        operators: dict[str, Operator] = {
            k: cast(Operator, m) for k, m in data.items() if k not in numbers
        }
        if "root" not in operators:
            break

        for (name, monkey) in operators.items():

            m = cast(Operator, monkey)
            m1, m2 = m.left, m.right
            if m1 in numbers and m2 in numbers:
                number1 = numbers[m1].number
                number2 = numbers[m2].number
                match m.op:
                    case "+":
                        n = number1 + number2
                    case "-":
                        n = number1 - number2
                    case "*":
                        n = number1 * number2
                    case "/":
                        n = number1 // number2

                numbers[name] = Number(name, n)
                print(numbers[name])

    root = numbers["root"]
    print(root.number)
