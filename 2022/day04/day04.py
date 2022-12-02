import re


def get_count(filename: str):
    count1 = 0
    count2 = 0
    with open(filename) as file:
        while nextline := file.readline().strip():
            elf1_low, elf1_high, elf2_low, elf2_high = map(int, re.split("[-,]", nextline))
            if (
                elf1_low <= elf2_low and elf1_high >= elf2_high
                or elf2_low <= elf1_low and elf2_high >= elf1_high
            ):
                count1 += 1
            if (
                elf1_low <= elf2_low <= elf1_high
                or elf1_low <= elf2_high <= elf1_high
                or elf2_low <= elf1_low <= elf2_high
                or elf2_low <= elf1_high <= elf2_high
            ):
                count2 += 1

    return count1, count2


if __name__ == "__main__":
    print(get_count("input0.txt"))
    print(get_count("input1.txt"))
