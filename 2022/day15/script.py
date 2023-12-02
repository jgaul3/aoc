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

    with open(filename) as file:
        while next_line := file.readline().strip():
            s_x, s_y, b_x, b_y = map(int, re.split("x=|y=|, |:", next_line)[1::2])
            dist = abs(s_x - b_x) + abs(s_y - b_y)

            y_disp = dist - abs(y_height - s_y)
            if y_disp >= 0:
                row_disallowed = condense(row_disallowed, s_x - y_disp, s_x + y_disp + 1)
            if s_y == y_height:
                occupied.add(s_x)
            if b_y == y_height:
                occupied.add(b_x)

    print(row_disallowed[1] - row_disallowed[0] - len(occupied))


def rule_factory(s_x, s_y, dist):
    def rule(x, y):
        return (abs(s_x - x) + abs(s_y - y)) < dist
    return rule


def find_intersections(filename: str, bound: int):
    pos_intercepts = set()
    neg_intercepts = set()
    rules = []
    with open(filename) as file:
        while next_line := file.readline().strip():
            s_x, s_y, b_x, b_y = map(int, re.findall(r"-?\d+", next_line))
            dist = abs(s_x - b_x) + abs(s_y - b_y) + 1

            pos_intercepts.update({s_y - s_x + dist, s_y - s_x - dist})
            neg_intercepts.update({s_y + s_x - dist, s_y + s_x + dist})
            rules.append(rule_factory(s_x, s_y, dist))

    for i in pos_intercepts:
        for j in neg_intercepts:
            intersection = (j - i) // 2, (j + i) // 2
            if 0 <= intersection[0] <= bound and 0 <= intersection[1] <= bound:
                if not any([rule(*intersection) for rule in rules]):
                    print(4000000 * intersection[0] + intersection[1])


if __name__ == "__main__":
    find_beacon_better("input0.txt", 10)
    find_intersections("input0.txt", 20)
    find_beacon_better("input1.txt", 2000000)
    find_intersections("input1.txt", 4000000)
