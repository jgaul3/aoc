import numpy as np


def fill_sand(filename: str, has_floor: bool = False):
    grid_set = set()
    grid = np.zeros((1000, 1000), dtype=bool)
    maxxest_x = maxxest_y = 0
    with open(filename) as file:
        while next_line := file.readline().strip():
            verts = [tuple(map(int, vert.split(","))) for vert in next_line.split(" -> ")]
            for i in range(len(verts) - 1):
                min_x, max_x = sorted([verts[i][0], verts[i + 1][0]])
                min_y, max_y = sorted([verts[i][1], verts[i + 1][1]])
                for j in range(min_x, max_x + 1):
                    for k in range(min_y, max_y + 1):
                        grid_set.add((j, k))
                grid[min_x:max_x + 1, min_y:max_y + 1] = True
                maxxest_x = max(maxxest_x, max_x + 1)
                maxxest_y = max(maxxest_y, max_y + 1)

    grid = grid[500 - maxxest_y - 1:500 + maxxest_y + 2, :maxxest_y + 2]
    if has_floor:
        grid[:, -1] = True

    add_count = 0
    sand_y = 0
    while not grid[maxxest_y + 1, 0] and grid.shape[1] > sand_y + 1:
        sand_x = maxxest_y + 1
        sand_y = 0
        while grid.shape[1] > sand_y + 1:
            sand_y += 1
            if not grid[sand_x, sand_y]:
                continue
            elif not grid[sand_x - 1, sand_y]:
                sand_x -= 1
            elif not grid[sand_x + 1, sand_y]:
                sand_x += 1
            else:
                grid[sand_x, sand_y - 1] = True
                add_count += 1
                sand_y = 0
                break

    set_count = 0
    sand_y = 0
    while (500, 0) not in grid_set and maxxest_y + 2 > sand_y:
        sand_x = 500
        sand_y = 0
        while maxxest_y + 2 > sand_y + 1:
            sand_y += 1
            if (sand_x, sand_y) not in grid_set:
                continue
            elif has_floor and sand_y == maxxest_y + 1:

            elif not grid[sand_x - 1, sand_y]:
                sand_x -= 1
            elif not grid[sand_x + 1, sand_y]:
                sand_x += 1
            else:
                grid[sand_x, sand_y - 1] = True
                add_count += 1
                sand_y = 0
                break

    assert add_count == set_count

    print(add_count)


if __name__ == "__main__":
    fill_sand("input0.txt")
    fill_sand("input0.txt", True)
    fill_sand("input1.txt")
    fill_sand("input1.txt", True)
