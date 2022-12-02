def get_totals(filename: str):
    totals = []
    with open(filename) as file:
        current_elf = 0
        for line in file:
            if line.strip():
                current_elf += int(line)
            else:
                totals.append(current_elf)
                current_elf = 0
        totals.append(current_elf)
    return totals


def get_solutions(filename: str):
    totals = get_totals(filename)
    totals.sort()
    return totals[-1], sum(totals[-3:])


if __name__ == "__main__":
    print(get_solutions("input0.txt"))
    print(get_solutions("input1.txt"))
