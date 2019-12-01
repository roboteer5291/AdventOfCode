from math import floor


def parse_file(file_name):
    file = open(file_name)
    values = []
    for line in file:
        values.append(int(line))
    return values


def parse_string(text):
    return [int(text)]


def solve_part_1(input):
    total = 0
    for i in input:
        fuel = floor(i/3) - 2
        total += fuel
    return total


def solve_part_2(input):
    total = 0
    for i in input:
        fuel = floor(i/3) - 2
        while fuel >= 0:
            total += fuel
            fuel = floor(fuel/3) - 2
    return total


print("Part 1: " + str(solve_part_1(parse_file("input.txt"))))
print("Part 2: " + str(solve_part_2(parse_file("input.txt"))))
