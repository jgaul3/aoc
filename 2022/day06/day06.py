import timeit


def get_index(filename: str, size: int):
    with open(filename) as file:
        line = file.read().strip()
    window = list(line[:size])
    for i in range(size, len(line)):
        if len(set(window)) == size:
            return i
        window.append(line[i])
        window.pop(0)


def get_index_interesting(filename: str, size: int):
    with open(filename) as file:
        line = file.read()
    last_seen = [0 for _ in range(26)]
    last_dupe = 0
    for i in range(len(line)):
        curr_char = line[i]
        last_dupe = max(last_seen[ord(curr_char) - ord('a')], last_dupe)
        if i - last_dupe >= size:
            return i + 1
        last_seen[ord(curr_char) - ord('a')] = i


if __name__ == "__main__":
    print(get_index("input0.txt", 4), get_index("input0.txt", 14))
    print(get_index("input1.txt", 4), get_index("input1.txt", 14))
    print(timeit.timeit("get_index('input1.txt', 14)", setup='from __main__ import get_index', number=1000))
    print(timeit.timeit("get_index_interesting('input1.txt', 14)", setup='from __main__ import get_index_interesting', number=1000))
