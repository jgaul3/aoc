def get_tops(filename: str):
    with open(filename) as file:
        start_lines = []
        while nextline := file.readline().strip('\n'):
            start_lines.append(nextline)
        rows = int(start_lines.pop()[-1])
        stacks1 = [[] for _ in range(rows)]
        stacks2 = [[] for _ in range(rows)]
        for line in start_lines:
            for idx, value in enumerate(range(1, len(line), 4)):
                if line[value] != " ":
                    stacks1[idx].insert(0, line[value])
                    stacks2[idx].insert(0, line[value])

        while nextline := file.readline().strip('\n'):
            amt, from_stack, to_stack = map(int, nextline.split(" ")[1::2])
            for i in range(amt):
                stacks1[to_stack - 1].append(stacks1[from_stack - 1].pop())

            stacks2[to_stack - 1].extend(stacks2[from_stack - 1][-amt:])
            del stacks2[from_stack - 1][-amt:]

    return "".join([stack[-1] for stack in stacks1]), "".join([stack[-1] for stack in stacks2])


if __name__ == "__main__":
    print(get_tops("input0.txt"))
    print(get_tops("input1.txt"))
