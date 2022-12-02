import re
from math import prod


def solve(filename: str) -> int:
    with open(filename) as file:
        string = file.read()
    matches = re.findall(r"mul\((\d+),(\d+)\)", string)
    return sum(prod(map(int, nums)) for nums in matches)


def solve2(filename: str) -> int:
    with open(filename) as file:
        string = "|".join(file.readlines()) + "|"

    # preprocess
    do_index = 0
    output = ""
    while do_index >= 0:
        dont_index = string.find("don't()", do_index + 1)
        output += string[do_index:dont_index]
        do_index = string.find("do()", do_index + 1)

    matches = re.findall(r"mul\((\d+),(\d+)\)", output)
    return sum(prod(map(int, nums)) for nums in matches)


if __name__ == "__main__":
    assert solve("sample0.txt") == 161
    print("Part 1: ", solve("input0.txt"))
    assert solve2("sample1.txt") == 48
    print("Part 2: ", solve2("input0.txt"))
