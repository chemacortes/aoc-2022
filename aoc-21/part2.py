import os
from dataclasses import astuple
from pathlib import Path
from typing import cast

from util import Monkey, Number, Operator, read


class EvaluationLoopError(Exception):
    pass


def eval(monkey: Monkey, monkeys: dict[str, Monkey]) -> int:

    match monkey:
        case Number(_, number):
            pass
        case Operator(_, left, right, op):
            m1 = monkeys[left]
            m2 = monkeys[right]
            match op:
                case "+":
                    number = eval(m1, monkeys) + eval(m2, monkeys)
                case "-":
                    number = eval(m1, monkeys) - eval(m2, monkeys)
                case "*":
                    number = eval(m1, monkeys) * eval(m2, monkeys)
                case "/":
                    number = eval(m1, monkeys) // eval(m2, monkeys)
        case _:
            raise ValueError

    return number


def back_eval(
    monkey: Monkey, monkeys: dict[str, Monkey], rev_index: dict[str, str]
) -> int:

    curname = monkey.name
    prev = rev_index[curname]
    prev_monkey = cast(Operator, monkeys[prev])

    prev_name, left, right, op = astuple(prev_monkey)
    other = right if curname == left else left

    operand = eval(monkeys[other], monkeys)

    if prev == "root":
        number = operand
    else:
        total = back_eval(prev_monkey, monkeys, rev_index)

        match op:
            case "+":
                number = total - operand
            case "*":
                number = total // operand
            case "-" if curname == left:
                number = total + operand
            case "-":
                number = operand - total
            case "/" if curname == left:
                number = total * operand
            case "/":
                number = operand // total
            case _:
                raise ValueError

    return number


if __name__ == "__main__":

    os.chdir(Path(__file__).parent)

    TRAINING = False
    monkeys = read("data-training.txt" if TRAINING else "data.txt")

    rev_index: dict[str, str] = {}
    for name, monkey in monkeys.items():
        match monkey:
            case Number():
                pass
            case Operator(name, left, right, _):
                rev_index[left] = name
                rev_index[right] = name

    root = monkeys["root"]
    human = monkeys["humn"]

    res = back_eval(human, monkeys, rev_index)

    print(res)
