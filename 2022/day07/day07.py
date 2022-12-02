def get_sizes(filename: str):
    with open(filename) as file:
        lines = [line.strip() for line in file]
    tree = parse_lines(lines)
    savings_req = tree["size"] - 40000000
    return count_under_size(tree), find_savings(tree, savings_req)


def parse_lines(lines: [str]):
    curr_dir = {"children": {}, "size": 0}
    while lines and (line := lines.pop(0)) and line != "$ cd ..":
        if line[0:4] == "$ cd":
            child_dir_name = line.split(" ")[-1]
            child_dir = parse_lines(lines)
            curr_dir["children"][child_dir_name] = child_dir
            curr_dir["size"] += child_dir["size"]
        elif line.split(" ")[0].isdigit():
            curr_dir["size"] += int(line.split(" ")[0])
    return curr_dir


def count_under_size(tree):
    count = tree["size"] * int(tree["size"] < 100000)
    for child in tree["children"].values():
        count += count_under_size(child)
    return count


def find_savings(tree, savings_req):
    curr_min = tree["size"] if tree["size"] > savings_req else 70000000
    for child in tree["children"].values():
        size = find_savings(child, savings_req)
        curr_min = min(size, curr_min)
    return curr_min


if __name__ == "__main__":
    print(get_sizes("input0.txt"))
    print(get_sizes("input1.txt"))
