import re
from functools import cache

nodes = {}


@cache
def explore(i: int, curr_node: str, total_fr: int, opened: str) -> int:
    i += 1
    opened_set = set(opened.split("."))
    for valve in opened_set:
        total_fr += nodes[valve]["rate"]

    if i == 30:
        return total_fr
    if curr_node not in opened_set and nodes[curr_node]["rate"] != 0:
        next_opened = ".".join(sorted(list(opened_set | {curr_node})))
        open_option = explore(i, curr_node, total_fr, next_opened)
    else:
        open_option = 0

    other_nodes = nodes[curr_node]["options"]

    return max(
        open_option,
        *[explore(i, other_node, total_fr, opened)
          for other_node in other_nodes]
    )


def find_beacon_better(filename: str):
    with open(filename) as file:
        while next_line := file.readline().strip():
            curr, *out = re.findall(r"([A-Z][A-Z])", next_line)
            flow_rate = int(re.findall(r"\d+", next_line)[0])
            nodes[curr] = {"rate": flow_rate, "options": out}

    print(explore(0, "AA", 0, "AA"))


if __name__ == "__main__":
    find_beacon_better("input1.txt")
    # find_beacon_better("input1.txt")
