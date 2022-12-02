import re


def solve(filename: str) -> int:
    with open(filename) as file:
        cards = [line.strip() for line in file]
    total = 0
    for card in cards:
        winners, ours = card.split(": ")[1].split(" | ")
        win_set = set(map(int, re.split(r" +", winners.strip())))
        our_set = set(map(int, re.split(r" +", ours.strip())))
        if overlap := win_set & our_set:
            total += 2 ** (len(overlap) - 1)

    return total


def solve2(filename: str) -> int:
    with open(filename) as file:
        cards = [line.strip() for line in file]
    card_count = [1 for _ in range(len(cards))]
    for idx, card in enumerate(cards):
        winners, ours = card.split(": ")[1].split(" | ")
        win_set = set(map(int, re.split(r" +", winners.strip())))
        our_set = set(map(int, re.split(r" +", ours.strip())))
        if overlap := win_set & our_set:
            curr_count = card_count[idx]
            for j in range(idx + 1, idx + 1 + len(overlap)):
                card_count[j] += curr_count

    return sum(card_count)


if __name__ == "__main__":
    assert solve("sample0.txt") == 13
    print("Part 1: ", solve("input0.txt"))
    assert solve2("sample0.txt") == 30
    print("Part 2: ", solve2("input0.txt"))
