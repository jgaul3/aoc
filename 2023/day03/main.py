import itertools


def solve(filename: str) -> int:
    with open(filename) as file:
        lines = [line.strip() for line in file]
    adjacent_set = set()
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if not char.isdigit() and not char == ".":
                for x_offset, y_offset in itertools.product((-1, 0, 1), repeat=2):
                    adjacent_set.add((row + x_offset, col + y_offset))
    current_num = 0
    idx_set = set()
    total = 0
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char.isdigit():
                current_num = current_num * 10 + int(char)
                idx_set.add((row, col))
            else:
                if idx_set & adjacent_set:
                    total += current_num

                current_num = 0
                idx_set = set()

    return total


def solve2(filename: str) -> int:
    with open(filename) as file:
        lines = [line.strip() for line in file]
    gear_set = set()
    gear_dict = dict()
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "*":
                gear_set.add((row, col))
                gear_dict[(row, col)] = []

    current_num = 0
    idx_set = set()
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char.isdigit():
                current_num = current_num * 10 + int(char)
                for x_offset, y_offset in itertools.product((-1, 0, 1), repeat=2):
                    idx_set.add((row + x_offset, col + y_offset))
            else:
                if overlap := idx_set & gear_set:
                    for gear in overlap:
                        gear_dict[gear].append(current_num)

                current_num = 0
                idx_set = set()

    return sum(
        adjacency_list[0] * adjacency_list[1]
        for adjacency_list in gear_dict.values()
        if len(adjacency_list) == 2
    )


if __name__ == "__main__":
    assert solve("sample0.txt") == 4361
    print("Part 1: ", solve("input0.txt"))
    assert solve2("sample0.txt") == 467835
    print("Part 2: ", solve2("input0.txt"))
