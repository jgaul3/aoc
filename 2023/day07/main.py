from collections import Counter


TYPE = ["HC", "1P", "2P", "3K", "FH", "4K", "5K"]
CARD = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
CARD_JOKER = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

def vanilla_hand_type(elems) -> str:
    if elems[0][1] == 5:
        return "5K"
    elif elems[0][1] == 4:
        return "4K"
    elif elems[0][1] == 3 and elems[1][1] == 2:
        return "FH"
    elif elems[0][1] == 3:
        return "3K"
    elif elems[0][1] == 2 and elems[1][1] == 2:
        return "2P"
    elif elems[0][1] == 2:
        return "1P"
    else:
        return "HC"


def hand_value(hand: str) -> tuple[int]:
    hand = hand.split(" ")[0]
    elems = Counter(hand.split(" ")[0]).most_common()

    hand_type = vanilla_hand_type(elems)

    level = TYPE.index(hand_type)

    tie_breakers = (CARD.index(card) for card in hand)

    return level, *tie_breakers


def hand_value_joker(hand: str) -> tuple[int]:
    hand = hand.split(" ")[0]
    count = Counter(hand.split(" ")[0])
    elems = count.most_common()
    jokers = count["J"]

    hand_type = "HC"
    match jokers:
        case 5 | 4:
            hand_type = "5K"
        case 3 if elems[1][1] == 2:
            hand_type = "5K"
        case 3:
            hand_type = "4K"
        case 2 if elems[0][1] == 3:
            hand_type = "5K"
        case 2 if elems[0][1] == 2 and elems[1][1] == 2:
            hand_type = "4K"
        case 2:
            hand_type = "3K"
        case 1:
            if elems[0][1] == 4:
                hand_type = "5K"
            elif elems[0][1] == 3:
                hand_type = "4K"
            elif elems[0][1] == 2 and elems[1][1] == 2:
                hand_type = "FH"
            elif elems[0][1] == 2:
                hand_type = "3K"
            else:
                hand_type = "1P"
        case 0:
            hand_type = vanilla_hand_type(elems)

    level = TYPE.index(hand_type)

    tie_breakers = (CARD_JOKER.index(card) for card in hand)

    return level, *tie_breakers


def solve(filename: str, part_2: bool = False) -> int:
    with open(filename) as file:
        lines = [line.strip() for line in file]

    list.sort(lines, key=hand_value_joker if part_2 else hand_value)
    result = 0
    for idx, line in enumerate(lines, start=1):
        result += idx * int(line.split(" ")[1])
    return result


if __name__ == "__main__":
    assert solve("sample0.txt") == 6440
    print("Part 1: ", solve("input0.txt"))
    assert solve("sample0.txt", part_2=True) == 5905
    print("Part 2: ", solve("input0.txt", part_2=True))
