import re
from collections import defaultdict


def solve(filename: str) -> int:
    first_nums = []
    second_nums = []
    with open(filename) as file:
        for line in file.readlines():
            matches = re.findall(r"(\d+)\D+(\d+)", line.strip())
            first_nums.append(int(matches[0][0]))
            second_nums.append(int(matches[0][1]))
    first_nums.sort()
    second_nums.sort()
    return sum(abs(first_nums[i] - second_nums[i]) for i in range(len(first_nums)))


def other_solve(filename: str) -> int:
    first_nums = []
    second_nums = defaultdict(lambda: 0)
    with open(filename) as file:
        for line in file.readlines():
            matches = re.findall(r"(\d+)\D+(\d+)", line.strip())
            first_nums.append(int(matches[0][0]))
            second_nums[int(matches[0][1])] += 1

    return sum(num * second_nums[num] for num in first_nums)


if __name__ == "__main__":
    assert solve("sample0.txt") == 11
    print("Part 1: ", solve("input0.txt"))
    assert other_solve("sample0.txt") == 31
    print("Part 2: ", other_solve("input0.txt"))
