p1_dict = {
    "A": {"X": 1+3, "Y": 2+6, "Z": 3+0},
    "B": {"X": 1+0, "Y": 2+3, "Z": 3+6},
    "C": {"X": 1+6, "Y": 2+0, "Z": 3+3},
}

p2_dict = {
    "A": {"X": 0+3, "Y": 3+1, "Z": 6+2},
    "B": {"X": 0+1, "Y": 3+2, "Z": 6+3},
    "C": {"X": 0+2, "Y": 3+3, "Z": 6+1},
}


def get_scores(filename: str):
    p1_score = p2_score = 0
    with open(filename) as file:
        for line in file:
            elf = line[0]
            resp = line[2]
            p1_score += p1_dict[elf][resp]
            p2_score += p2_dict[elf][resp]
    return p1_score, p2_score


if __name__ == "__main__":
    print(get_scores("input0.txt"))
    print(get_scores("input1.txt"))
