import re
import numpy as np


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
                        (next_index[0] + side_length - 1) // side_length,
                        (next_index[1] + side_length - 1) // side_length,
                    )
                    overflows = (
                        (next_index[0] + side_length - 1) % side_length,
                        (next_index[1] + side_length - 1) % side_length,
                    )

                    if facing == 0:
                        if helper_coords == (1, 4):
                            next_index = coords[0], np.argwhere(grid[coords[0]])[0][0]
                            new_facing = 2
                        elif helper_coords == (2, 4):
                            pass
                        elif helper_coords == (3, 5):
                            pass

                    elif facing == 1:
                        next_index = np.argwhere(grid[:, coords[1]])[0][0], coords[1]
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
