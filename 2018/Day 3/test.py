import unittest
from solution import parse_file, parse_other_input, solve_part_1, solve_part_2


part_1_tests = [[["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"], 4]]
part_2_tests = [[["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"], 3]]


class TestPart1(unittest.TestCase):
    def test_pass(self):
        for i in part_1_tests:
            input = i[0]
            correct = i[1]
            data = parse_other_input(input)
            answer = solve_part_1(data)
            self.assertEqual(correct, answer)


class TestPart2(unittest.TestCase):
    def test_pass(self):
        for i in part_2_tests:
            input = i[0]
            correct = i[1]
            data = parse_other_input(input)
            answer = solve_part_2(data)
            self.assertEqual(correct, answer)


if __name__ == '__main__':
    unittest.main()
