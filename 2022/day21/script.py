import operator

op_dict = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}
monkey_dict = {}


class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.value = self.op = self.left = self.right = None
        if isinstance(monkey_dict[name], int):
            self.value = monkey_dict[name]
        else:
            left, self.op, right = monkey_dict[name]
            self.left = Node(left, self)
            self.right = Node(right, self)


def solve_tree(monkey_tree: Node):
    if monkey_tree.value:
        return monkey_tree.value
    left = solve_tree(monkey_tree.left)
    right = solve_tree(monkey_tree.right)
    return op_dict[monkey_tree.op](left, right)


def solve_tree_backwards(tree: Node, parent_name: str):
    if tree.value:
        return tree.value

    is_left = tree.left.name == parent_name
    if tree.name == "root":
        return solve_tree(tree.right) if is_left else solve_tree(tree.left)

    parent = solve_tree_backwards(tree.parent, tree.name)
    other = solve_tree(tree.right if is_left else tree.left)

    match tree.op, is_left:
        case "+", _:
            return parent - other
        case "-", True:
            return parent + other
        case "-", False:
            return other - parent
        case "*", _:
            return parent // other
        case "/", True:
            return parent * other
        case "/", False:
            return other // parent


def get_nums(filename: str):
    with open(filename) as file:
        for line in file:
            monkey, action = line.strip().split(": ")
            monkey_dict[monkey] = action.split(" ") if not action.isdigit() else int(action)

    tree = Node("root", None)

    humn_tree = None
    humn_stack = [tree]
    while curr := humn_stack.pop():
        if curr.name == "humn":
            humn_tree = curr
            break
        if not curr.value:
            humn_stack.extend([curr.left, curr.right])

    print(solve_tree(tree))
    print(solve_tree_backwards(humn_tree.parent, "humn"))


if __name__ == "__main__":
    get_nums("input0.txt")
    get_nums("input1.txt")
