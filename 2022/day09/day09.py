direction_dict = {
    "R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)
}

tail_offsets = [
    [[-1, -1], [-1, -1], [-1, 0], [-1, 1], [-1, 1]],
    [[-1, -1], [0, 0], [0, 0], [0, 0], [-1, 1]],
    [[0, -1], [0, 0], [0, 0], [0, 0], [0, 1]],
    [[1, -1], [0, 0], [0, 0], [0, 0], [1, 1]],
    [[1, -1], [1, -1], [1, 0], [1, 1], [1, 1]],
]


def resolve_tail(head, tail):
    offset = tail_offsets[head[0] - tail[0] + 2][head[1] - tail[1] + 2]
    return tail[0] + offset[0], tail[1] + offset[1]


def get_visible(filename: str, length: int):
    actions = []
    with open(filename) as file:
        for line in file:
            direction, amt = line.split(" ")
            actions.extend([direction for _ in range(int(amt))])

    segments = [(0, 0) for _ in range(length)]
    spots = set()

    for direction in actions:
        head_offset_x, head_offset_y = direction_dict[direction]
        segments[0] = (segments[0][0] + head_offset_x, segments[0][1] + head_offset_y)
        for i in range(len(segments) - 1):
            segments[i + 1] = resolve_tail(segments[i], segments[i + 1])
        spots.add(segments[-1])

    return len(spots)


if __name__ == "__main__":
    print(get_visible("input0.txt", 2), get_visible("input0.txt", 10))
    print(get_visible("input1.txt", 2), get_visible("input1.txt", 10))
