def get_text(filename: str):
    with open(filename) as file:
        lines = [line.strip() for line in file]

    register_x = 1
    to_add = total = 0
    image = ""
    for i in range(6):
        for j in range(40):
            total += (i * 40 + j + 1) * register_x if j == 19 else 0
            image += "█" if register_x - 1 <= j <= register_x + 1 else " "

            if to_add:
                register_x += to_add
                to_add = 0
            else:
                action, *amt = lines.pop(0).split(" ")
                to_add = int(amt[0]) if amt else 0

        image += "\n"

    print(total)
    print(image)


if __name__ == "__main__":
    get_text("input0.txt")
    get_text("input1.txt")
