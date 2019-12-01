def parse_file(file_name):
    file = open(file_name)
    values = []
    for line in file:
        values.append(int(line))
    return values


vals = parse_file("2018Day1Input.txt")
print(len(vals))
total = 0
results = []
seen = {0}
part2result = 0
duplicate = False
run = False
while not duplicate:
    for i in vals:
        total += i
        if total in seen and not duplicate:
            print("pt2 " + str(total))
            duplicate = True
        else:
            seen.add(total)
    if not run:
        print("pt1 " + str(total))
    run = True