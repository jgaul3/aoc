import heapq


import numpy as np


def a_star_search(grid, start_index, end_index):
    visit_queue = [(0, start_index)]
    visited = set()
    actual_dists = np.ones_like(grid, dtype=np.int32) * 100_000
    actual_dists[start_index] = 0
    while visit_queue:
        _, curr_idx = heapq.heappop(visit_queue)
        visited.add(curr_idx)
        for i_x, i_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_idx = (curr_idx[0] + i_x, curr_idx[1] + i_y)
            h = abs(next_idx[0] - end_index[0]) + abs(next_idx[1] - end_index[1])
            if (
                0 <= next_idx[0] < grid.shape[0]
                and 0 <= next_idx[1] < grid.shape[1]
                and next_idx not in visited
                and actual_dists[next_idx] > actual_dists[curr_idx] + 1
                and ord(grid[next_idx]) - ord(grid[curr_idx]) <= 1
            ):
                heapq.heappush(visit_queue, (actual_dists[curr_idx] + h, next_idx))
                actual_dists[next_idx] = actual_dists[curr_idx] + 1
                if next_idx == end_index:
                    return actual_dists[next_idx]


def get_step_count(filename: str):
    with open(filename) as file:
        grid = np.array([list(line.strip()) for line in file])

    start_index = tuple(np.argwhere(grid == "S")[0])
    end_index = tuple(np.argwhere(grid == "E")[0])
    grid[grid == "S"] = "a"
    grid[grid == "E"] = "z"

    options = [a_star_search(grid, (i, 0), end_index) for i in range(grid.shape[0])]
    print(options[start_index[0]])
    print(min(options))


if __name__ == "__main__":
    get_step_count("input0.txt")
    get_step_count("input1.txt")
