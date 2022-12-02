import re
import numpy as np


def next_index_from_overflow(next_index, side_length, facing_start, facing_end, hc_start, hc_end):
    overflows = (
        (next_index[0] - 1) % side_length,
        (next_index[1] - 1) % side_length,
    )

    match facing_start, facing_end:
        case 0, 0:
            x_offset = overflows[0] + 1
            y_offset = 0
        case 0, 1:
            pass

    # if facing_start == 0:
    #     pass
    # elif facing_start == 1:
    #     pass
    # elif facing_start == 2:
    #     pass
    # else:
    #     pass
    #
    # if facing_end == 0:
    #     pass
    # elif facing_end == 1:
    #     pass
    # elif facing_end == 2:
    #     pass
    # else:
    #     pass
    return side_length * hc_end[0] + x_offset, side_length * hc_end[1] + y_offset


def get_nums(filename: str, cube: bool):
    with open(filename) as file:
        raw_grid = []
        while line := file.readline().rstrip():
            raw_grid.append(list(line))

        actions = re.split(r"(\D)", file.readline().strip())

    max_width = max([len(line) for line in raw_grid])
    grid = np.zeros((len(raw_grid), max_width), dtype=int)
    for i, row in enumerate(raw_grid):
        for j, elem in enumerate(row):
            match elem:
                case ".":
                    grid[i, j] = 1
                case "#":
                    grid[i, j] = 2
    grid = np.pad(grid, 1)
    coords = np.argwhere(grid == 1)[0]
    facing = 0

    for action in actions:
        if not action.isdigit():
            facing += 1 if action == "R" else -1
            facing %= 4
        else:
            for i in range(int(action)):
                if facing == 0:  # Right
                    next_index = coords[0], coords[1] + 1
                elif facing == 1:  # Down
                    next_index = coords[0] + 1, coords[1]
                elif facing == 2:  # Left
                    next_index = coords[0], coords[1] - 1
                else:  # Up
                    next_index = coords[0] - 1, coords[1]

                new_facing = facing
                if grid[next_index] == 0 and not cube:
                    if facing == 0:
                        next_index = coords[0], np.argwhere(grid[coords[0]])[0][0]
                    elif facing == 1:
                        next_index = np.argwhere(grid[:, coords[1]])[0][0], coords[1]
                    elif facing == 2:
                        next_index = coords[0], np.argwhere(grid[coords[0]])[-1][0]
                    else:
                        next_index = np.argwhere(grid[:, coords[1]])[-1][0], coords[1]

                elif grid[next_index] == 0 and cube and len(grid) == 14:
                    side_length = 4
                    helper_coords = (
                        (next_index[0] - 1) // side_length,
                        (next_index[1] - 1) // side_length,
                    )
                    overflows = (
                        (next_index[0] - 1) % side_length,
                        (next_index[1] - 1) % side_length,
                    )

                    if facing == 0:
                        if helper_coords == (0, 3):
                            # 180 -> 2, 3 right
                            next_index = (
                                side_length * 3 - overflows[0],
                                side_length * 4
                            )
                            new_facing = 2
                        elif helper_coords == (1, 3):
                            # 90 -> 2, 3 top
                            next_index = (
                                side_length * 2 + 1,
                                side_length * 4 - overflows[0],
                            )
                            new_facing = 1
                        elif helper_coords == (2, 4):
                            # 180 -> 0, 2 right
                            next_index = (
                                side_length - overflows[0],
                                side_length * 3,
                            )
                            new_facing = 2

                    elif facing == 1:
                        if helper_coords == (2, 0):
                            # 180 -> 2, 2 up
                            next_index = (
                                side_length * 3,
                                side_length * 3 - overflows[1]
                            )
                            new_facing = 3
                        elif helper_coords == (2, 1):
                            # 270 -> 2, 2 right
                            next_index = (
                                side_length * 3 - overflows[1],
                                side_length * 2 + 1,
                            )
                            new_facing = 0
                        elif helper_coords == (3, 2):
                            # 0 -> 0, 2 down
                            next_index = (
                                side_length * 0 + 1,
                                side_length * 2 + overflows[1] + 1,
                            )
                            new_facing = 1
                        elif helper_coords == (3, 3):
                            # 270 -> 1, 0 left
                            pass

                    elif facing == 2:
                        next_index = coords[0], np.argwhere(grid[coords[0]])[-1][0]
                    else:
                        next_index = np.argwhere(grid[:, coords[1]])[-1][0], coords[1]

                if grid[next_index] == 1:
                    coords = next_index
                    facing = new_facing
                else:
                    break

    print(1000 * coords[0] + 4 * coords[1] + facing)


if __name__ == "__main__":
    get_nums("input0.txt", False)
    get_nums("input0.txt", True)
    get_nums("input1.txt", False)
    get_nums("input1.txt", True)
