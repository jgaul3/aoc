MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def parse_game(line: str) -> list[list[int, int, int]]:
    trimmed = line[line.find(":") + 2:]
    games = trimmed.split("; ")
    rounds = []
    for game in games:
        counts = [0, 0, 0]
        for amounts in game.strip().split(", "):
            number, color = amounts.split(" ", 1)
            match color:
                case "red":
                    counts[0] = int(number)
                case "green":
                    counts[1] = int(number)
                case "blue":
                    counts[2] = int(number)
        rounds.append(counts)
    return rounds


def game_possible(line: str) -> bool:
    parsed_game = parse_game(line)
    for game in parsed_game:
        if game[0] > MAX_RED or game[1] > MAX_GREEN or game[2] > MAX_BLUE:
            return False
    return True


def solve(filename: str) -> int:
    with open(filename) as file:
        return sum(
            index
            for index, line in enumerate(file, start=1)
            if game_possible(line)
        )


def get_power(line: str) -> int:
    parsed_game = parse_game(line)
    max_r, max_g, max_b = 0, 0, 0
    for game in parsed_game:
        max_r = max(max_r, game[0])
        max_g = max(max_g, game[1])
        max_b = max(max_b, game[2])
    return max_r * max_g * max_b


def solve2(filename: str) -> int:
    with open(filename) as file:
        return sum(get_power(line) for line in file)


if __name__ == "__main__":
    assert solve("sample0.txt") == 8
    print("Part 1: ", solve("input0.txt"))
    assert solve2("sample0.txt") == 2286
    print("Part 2: ", solve2("input0.txt"))
