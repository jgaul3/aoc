import re
import math


epsilon = 0.00000000001


def get_bounds(time: int, dist: int) -> int:
    limit_one = (time + math.sqrt(time ** 2 - 4 * dist)) / 2
    limit_two = (time - math.sqrt(time ** 2 - 4 * dist)) / 2
    higher = math.floor(max(limit_one - epsilon, limit_two - epsilon))
    lower = math.ceil(min(limit_one + epsilon, limit_two + epsilon))
    return higher - lower + 1


def solve(filename: str) -> int:
    with open(filename) as file:
        lines = file.readlines()

    time_str = lines[0].split(":")[1].strip()
    times = list(map(int, re.split(r" +", time_str)))
    dist_str = lines[1].split(":")[1].strip()
    dists = list(map(int, re.split(r" +", dist_str)))

    result = 1
    for time, dist in zip(times, dists):
        result *= get_bounds(time, dist)
    return result


def solve2(filename: str) -> int:
    with open(filename) as file:
        lines = file.readlines()

    time = int(lines[0].split(":")[1].replace(" ", ""))
    dist = int(lines[1].split(":")[1].replace(" ", ""))

    return get_bounds(time, dist)


if __name__ == "__main__":
    assert solve("sample0.txt") == 288
    print("Part 1: ", solve("input0.txt"))
    assert solve2("sample0.txt") == 71503
    print("Part 2: ", solve2("input0.txt"))
