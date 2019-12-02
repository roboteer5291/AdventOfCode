from collections import defaultdict

# #2 @ 791,235: 17x27
def parse_file(file_name):  # File to data format
    file = open(file_name)
    lines = []
    for line in file:
        lines.append(line)
    return parse_other_input(lines)


def parse_other_input(text):  # Other input to data format
    data = []
    for line in text:
        sec_id = int(line.split(" ")[0][1:])
        x = int(line.split(" ")[2].split(",")[0])
        y = int(line.split(" ")[2].split(",")[1][:-1])
        width = int(line.split(" ")[3].split("x")[0])
        height = int(line.split(" ")[3].split("x")[1])
        data.append([sec_id, x, y, width, height])
        print(str(sec_id))
    return data


def solve_part_1(data):
    grid = defaultdict(int)
    for entry in data:
        for dx in range(entry[3]):
            for dy in range(entry[4]):
                grid[(entry[1] + dx, entry[2] + dy)] += 1
    total = 0
    for (x, y), count in grid.items():
        if count >= 2:
            total += 1
    return total


def solve_part_2(data):
    grid = defaultdict(int)
    for entry in data:
        for dx in range(entry[3]):
            for dy in range(entry[4]):
                grid[(entry[1] + dx, entry[2] + dy)] += 1
    for entry in data:
        overlapped = False
        for dx in range(entry[3]):
            for dy in range(entry[4]):
                if grid[(entry[1] + dx, entry[2] + dy)] > 1:
                    overlapped = True
        if not overlapped:
            return entry[0]


# print("Part 1: " + str(solve_part_1(parse_file("input.txt"))))
print("Part 2: " + str(solve_part_2(parse_file("input.txt"))))
