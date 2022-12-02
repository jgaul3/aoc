import re


def solve(filename: str) -> int:
    total = 0
    with open(filename) as file:
        for line in file:
            matches = re.findall(r"(?:\D*(\d))", line)
            total += int(matches[0] + matches[-1])
    return total


def solve2(filename: str) -> int:
    total = 0
    with open(filename) as file:
        for line in file:
            found = []
            while line:
                if line.startswith("one") or line[0] == "1":
                    found.append(1)
                elif line.startswith("two") or line[0] == "2":
                    found.append(2)
                elif line.startswith("three") or line[0] == "3":
                    found.append(3)
                elif line.startswith("four") or line[0] == "4":
                    found.append(4)
                elif line.startswith("five") or line[0] == "5":
                    found.append(5)
                elif line.startswith("six") or line[0] == "6":
                    found.append(6)
                elif line.startswith("seven") or line[0] == "7":
                    found.append(7)
                elif line.startswith("eight") or line[0] == "8":
                    found.append(8)
                elif line.startswith("nine") or line[0] == "9":
                    found.append(9)
                elif line.startswith("zero") or line[0] == "0":
                    found.append(0)
                line = line[1:]
            total += found[0] * 10 + found[-1]
    return total


if __name__ == "__main__":
    assert solve("sample0.txt") == 142
    print("Part 1: ", solve("input0.txt"))
    assert solve2("sample1.txt") == 281
    print("Part 2: ", solve2("input0.txt"))
