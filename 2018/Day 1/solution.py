def parse_file(file_name):  # File to data format
    file = open(file_name)
    values = []
    for line in file:
        values.append(int(line))
    return values


def parse_other_input(text):  # Other input to data format
    values = []
    split = text.split(", ")
    for t in split:
        values.append(int(t))
    return values


def solve_part_1(data):
    total = 0
    for i in data:
        total += i
    return total


def solve_part_2(data):
    total = 0
    seen = {0}
    while True:
        for i in data:
            total += i
            if total in seen:
                return total
            else:
                seen.add(total)


print("Part 1: " + str(solve_part_1(parse_file("input.txt"))))
print("Part 2: " + str(solve_part_2(parse_file("input.txt"))))
