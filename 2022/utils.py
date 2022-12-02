def read_lines(name: str) -> [str]:
    with open(name) as file:
        return [line for line in file]
