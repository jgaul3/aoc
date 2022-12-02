import numpy as np


def get_visible(filename: str):
    with open(filename) as file:
        heights = np.array([list(map(int, list(line.strip()))) for line in file])

    count = 2 * heights.shape[0] + 2 * heights.shape[1] - 4
    for x in range(1, heights.shape[0] - 1):
        for y in range(1, heights.shape[1] - 1):
            curr_height = heights[x, y]
            sightlines = [
                heights[x, :y].max(), heights[x, y + 1:].max(), heights[:x, y].max(), heights[x + 1:, y].max()
            ]
            count += int(curr_height > min(sightlines))

    score = 0
    heights[0, :] = heights[-1, :] = heights[:, 0] = heights[:, -1] = 10
    for x in range(1, heights.shape[0] - 1):
        for y in range(1, heights.shape[1] - 1):
            curr_height = heights[x, y]
            up_offset = down_offset = left_offset = right_offset = 1
            while heights[x - up_offset, y] < curr_height:
                up_offset += 1
            while heights[x + down_offset, y] < curr_height:
                down_offset += 1
            while heights[x, y - left_offset] < curr_height:
                left_offset += 1
            while heights[x, y + right_offset] < curr_height:
                right_offset += 1
            score = max(score, up_offset * down_offset * left_offset * right_offset)
    return count, score


if __name__ == "__main__":
    print(get_visible("input0.txt"))
    print(get_visible("input1.txt"))
