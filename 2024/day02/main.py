def is_safe(row: list[int]) -> bool:
    sign = (row[0] - row[1]) > 0
    for i in range(len(row) - 1):
        diff = row[i] - row[i + 1]
        if abs(diff) > 3 or diff == 0:
            return False
        if (diff > 0) is not sign:
            return False

    return True


def is_safe_dampener(row: list[int]) -> bool:
    for skip in range(len(row)):
        new_row = row[:skip] + row[skip + 1:]
        if is_safe(new_row):
            print(skip)
            return True

    return False


def solve(filename: str, dampener: bool = False) -> int:
    grid = []
    with open(filename) as file:
        for line in file.readlines():
            grid.append(list(map(int, line.strip().split())))
    safes = 0
    for row in grid:
        if dampener:
            print(row, is_safe_dampener(row))
            safes += int(is_safe_dampener(row))
        else:
            safes += int(is_safe(row))
    return safes


if __name__ == "__main__":
    assert solve("sample0.txt") == 2
    print("Part 1: ", solve("input0.txt"))
    assert solve("sample0.txt", True) == 4
    print("Part 2: ", solve("input0.txt", True))
