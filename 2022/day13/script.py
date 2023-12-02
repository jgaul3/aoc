from functools import cmp_to_key


def compare_arrays(left, right):
    if left == right:
        return 0
    if not left or not right:
        return -1 if not left else 1

    left_elem = left[0]
    right_elem = right[0]

    if isinstance(left_elem, int) and isinstance(right_elem, int):
        if left_elem != right_elem:
            return -1 if left_elem < right_elem else 1
    else:
        outcome = compare_arrays(
            [left_elem] if isinstance(left_elem, int) else left_elem,
            [right_elem] if isinstance(right_elem, int) else right_elem,
        )
        if outcome != 0:
            return outcome

    return compare_arrays(left[1:], right[1:])


def get_correct_count(filename: str):
    count = index = 0
    packet_array = [[], [[2]], [[6]]]  # index-from-one fix and spacers
    with open(filename) as file:
        while next_line := file.readline().strip():
            left_array = eval(next_line)
            right_array = eval(file.readline().strip())

            packet_array.extend([left_array, right_array])
            correct_order = compare_arrays(left_array, right_array) == -1

            index += 1
            count += correct_order * index
            file.readline()

    packet_array.sort(key=cmp_to_key(compare_arrays))
    return count, packet_array.index([[2]]) * packet_array.index([[6]])


if __name__ == "__main__":
    print(get_correct_count("input0.txt"))
    print(get_correct_count("input1.txt"))
