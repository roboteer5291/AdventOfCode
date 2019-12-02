def parse_file(file_name):  # File to data format
    file = open(file_name)
    lines = []
    for l in file:
        lines.append(l)
    return lines


def parse_other_input(text):  # String Array to data format
    return text


def solve_part_1(data):
    two_count = 0
    three_count = 0
    for box in data:
        two = False
        three = False
        for l in box:
            if box.count(l) == 2:
                two = True
            if box.count(l) == 3:
                three = True
        if two:
            two_count += 1
        if three:
            three_count += 1
    return two_count * three_count


def solve_part_2(data):
    for box in data:
        for box2 in data:
            if box == box2:
                break
            not_matching = 0
            not_matching_index = 0
            for i in range(0, len(box) - 1):
                if box[i] != box2[i]:
                    not_matching += 1
                    not_matching_index = i
            if not_matching == 1:
                string = ""
                for i in range(0, len(box) - 1):
                    if i == not_matching_index:
                        continue
                    string += box[i]
                return string


print("Part 1: " + str(solve_part_1(parse_file("input.txt"))))
print("Part 2: " + str(solve_part_2(parse_file("input.txt"))))
