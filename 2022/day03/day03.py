priority = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_scores(filename: str):
    total = 0
    with open(filename) as file:
        for line in file:
            total += priority.index(
                (set(line[:len(line) // 2]) & set(line[len(line) // 2:])).pop()
            )

    return total


def get_scores2(filename: str):
    total = 0
    with open(filename) as file:
        while nextline := file.readline():
            total += priority.index(
                (set(nextline.strip()) & set(file.readline().strip()) & set(file.readline().strip())).pop()
            )

    return total


if __name__ == "__main__":
    print(get_scores("input0.txt"), get_scores2("input0.txt"))
    print(get_scores("input1.txt"), get_scores2("input1.txt"))
