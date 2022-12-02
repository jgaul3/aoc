import math
from dataclasses import dataclass, field


@dataclass
class Monkey:
    items: [int] = field(default_factory=list)
    operation: str = ""
    divisor: int = 0
    test_true: int = 0
    test_false: int = 0
    inspections: int = 0


def monkey_count(filename: str, rounds: int):
    with open(filename) as file:
        lines = [line.strip() for line in file]
    lines.append("")

    divisors = []
    monkey_list = []
    curr_monkey = {}
    for line in lines:
        if line.startswith("Monkey"):
            curr_monkey = Monkey()
        elif line.startswith("Starting"):
            items = line.split(": ")[-1].split(", ")
            curr_monkey.items = list(map(int, items))
        elif line.startswith("Operation"):
            curr_monkey.operation = line.split("= ")[-1]
        elif line.startswith("Test"):
            curr_monkey.divisor = int(line.split(" ")[-1])
            divisors.append(curr_monkey.divisor)
        elif line.startswith("If true"):
            curr_monkey.test_true = int(line.split(" ")[-1])
        elif line.startswith("If false"):
            curr_monkey.test_false = int(line.split(" ")[-1])
        else:
            monkey_list.append(curr_monkey)

    divisors = math.lcm(*divisors)
    for i in range(rounds):
        for monkey in monkey_list:
            while monkey.items:
                monkey.inspections += 1
                old = monkey.items.pop(0)
                old = eval(monkey.operation)
                if rounds == 20:
                    old = old // 3
                old = old % divisors
                index = monkey.test_true if old % monkey.divisor == 0 else monkey.test_false
                monkey_list[index].items.append(old)

    sorted_inspections = sorted([monkey.inspections for monkey in monkey_list])
    print(math.prod([sorted_inspections[-2], sorted_inspections[-1]]))


if __name__ == "__main__":
    monkey_count("input0.txt", 20)
    monkey_count("input0.txt", 10000)
    monkey_count("input1.txt", 20)
    monkey_count("input1.txt", 10000)
