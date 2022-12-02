from dataclasses import dataclass
from typing import Self


def transform(
    curr_nums: list[int], dest_start: int, source_start: int, dist: int
) -> (list[int], list[int]):
    unchanged_nums = []
    updated_nums = []
    for curr_num in curr_nums:
        amt_over_source_start = curr_num - source_start
        if 0 <= amt_over_source_start < dist:
            updated_nums.append(dest_start + amt_over_source_start)
        else:
            unchanged_nums.append(curr_num)
    return unchanged_nums, updated_nums


def solve(filename: str) -> int:
    with open(filename) as file:
        lines = [line.strip() for line in file if line.strip()]

    curr_nums = []
    updated_nums = list(map(int, lines.pop(0).split(" ")[1:]))
    for line in lines:
        if not line[0].isdigit():
            curr_nums.extend(updated_nums)
            updated_nums = []
        else:
            curr_nums, changed_nums = transform(curr_nums, *map(int, line.split(" ")))
            updated_nums.extend(changed_nums)
    return min(updated_nums + curr_nums)


@dataclass
class Range:
    # Includes start, excludes start + dist
    start: int
    dist: int

    def compare(self, other: Self) -> tuple[Self, Self, Self]:


def transform_ranges(
    curr_ranges: list[Range], dest_start: int, source_start: int, dist: int
) -> (list[Range], list[Range]):
    unchanged = []
    updated = []
    for curr_range in curr_ranges:
        if curr_range.start + curr_range.dist < source_start:
            unchanged.append(curr_range)
        elif source_start + dist < curr_range.start:
            unchanged.append(curr_range)

        # amt_over_source_start = curr_num - source_start
        # if 0 <= amt_over_source_start < dist:
        #     curr_range.start += amt_over_source_start
        #     updated.append(dest_start + amt_over_source_start)
        # else:
        #     unchanged.append(curr_num)
    return unchanged, updated


def test():
    test_ranges = [Range(5, 3)]  # 5, 6, 7
    assert transform_ranges(test_ranges, dest_start=14, source_start=9, dist=3) == ([Range(5, 3)], [])
    assert transform_ranges(test_ranges, dest_start=14, source_start=9, dist=3) == ([Range(5, 3)], [])


if __name__ == "__main__":
    assert solve("sample0.txt") == 35
    print("Part 1: ", solve("input0.txt"))
    test()
    # assert solve2("sample0.txt") == 46
    # print("Part 2: ", solve2("input0.txt"))
