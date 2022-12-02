import re
import bisect


def condense(disallowed: [[]], to_add_low: int, to_add_high: int):
    """
    disallowed is a sorted list of pairs of indices
    to_add is a pair to be added which may or may not overlap
    second element is not inclusive
    d: [... a, b, c, d...]
    """
    if not disallowed:
        return [to_add_low, to_add_high]
    left_idx = bisect.bisect_left(disallowed, to_add_low)
    right_idx = bisect.bisect_right(disallowed, to_add_high)
    if right_idx % 2 == 0:
        disallowed.insert(right_idx, to_add_high)
    if left_idx % 2 == 0:
        disallowed.insert(left_idx, to_add_low)
    for i in range(left_idx, right_idx):
        del disallowed[left_idx + int(left_idx % 2 == 0)]

    return disallowed


def find_beacon_better(filename: str, y_height: int):
    occupied = set()
    row_disallowed = []
    full_disallowed = []

    with open(filename) as file:
        while next_line := file.readline().strip():
            s_x, s_y, b_x, b_y = map(int, re.split("x=|y=|, |:", next_line)[1::2])
            dist = abs(s_x - b_x) + abs(s_y - b_y)

            y_disp = dist - abs(y_height // 2 - s_y)
            if y_disp >= 0:
                row_disallowed = condense(row_disallowed, s_x - y_disp, s_x + y_disp + 1)
            if s_y == y_height // 2:
                occupied.add(s_x)
            if b_y == y_height // 2:
                occupied.add(b_x)

            """
            Must be a point bounded on all four diagonals
            """
            for i in range(max(0, s_y - dist), min(y_height, s_y + dist)):
                y_disp = dist - abs(i - s_y)
                low_val = max(y_height * i, y_height * i + s_x - y_disp)
                high_val = min(y_height * (i + 1), y_height * i + s_x + y_disp + 1)
                full_disallowed = condense(full_disallowed, low_val, high_val)

    print(row_disallowed[1] - row_disallowed[0] - len(occupied))
    print((full_disallowed[1] % 20) * 4_000_000 + (full_disallowed[1] // 20))


if __name__ == "__main__":
    find_beacon_better("input0.txt", 20)
    find_beacon_better("input1.txt", 4000000)
