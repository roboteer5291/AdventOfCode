from math import floor


def parse_file(file_name):
    file = open(file_name)
    values = []
    for line in file:
        values.append(int(line))
    return values


vals = parse_file("2019Day1Input.txt")
total1 = 0
total2 = 0
for i in vals:
    fuel = floor(i / 3) - 2
    total1 += fuel
    while fuel >= 0:
        total2 += fuel
        fuel = floor(fuel / 3) - 2
print(total1)
print(total2)
