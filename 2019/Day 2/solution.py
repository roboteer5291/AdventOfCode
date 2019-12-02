def parse_file(file_name):  # File to data format
    file = open(file_name)
    text = file.read()
    return parse_other_input(text)


def parse_other_input(text):  # Other input to data format
    vals = text.split(",")
    ints = []
    for i in vals:
        ints.append(int(i))
    return ints


def solve_part_1(data):
    pointer_location = 0
    while True:
        if pointer_location >= len(data):
            print(str(data))
            print(pointer_location)
            print("We went too far")
            return -1
        opcode = int(data[pointer_location])
        if opcode == 99:
            # print("99: " + str(data[0]))
            return data[0]
        if pointer_location >= len(data) - 3:
            print("We went to far 2")
            return -1
        arg_1_pos = data[pointer_location + 1]
        arg_2_pos = data[pointer_location + 2]
        result_pos = data[pointer_location + 3]
        if arg_1_pos >= len(data) or arg_2_pos >= len(data) or result_pos >= len(data):
            print(str(data))
            print(pointer_location)
            print(arg_1_pos)
            print(arg_2_pos)
            print(result_pos)
            print("args are too far")
            return -1
        elif opcode == 1:
            arg_1 = data[data[pointer_location + 1]]
            arg_2 = data[data[pointer_location + 2]]
            data[data[pointer_location + 3]] = arg_1 + arg_2
        elif opcode == 2:
            arg_1 = data[data[pointer_location + 1]]
            arg_2 = data[data[pointer_location + 2]]
            data[data[pointer_location + 3]] = arg_1 * arg_2
        else:
            # print("Bad opcode pos: " + str(pointer_location) + " val: " + str(data[pointer_location]))
            return -1
        pointer_location += 4


def solve_part_2(data):
    for noun in range(0, 100):
        for verb in range(0, 100):
            new_data = data.copy()
            new_data[1] = noun
            new_data[2] = verb
            print(str(noun) + " " + str(verb))
            if solve_part_1(new_data) == 19690720:
                print(str(noun) + " " + str(verb))
                return 100 * noun + verb
    print("Not found yet")
    return -1


print("Part 1: " + str(solve_part_1(parse_file("input.txt"))))
# print("Part 2: " + str(solve_part_2(parse_file("input.txt"))))
