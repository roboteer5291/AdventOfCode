import unittest
from solution import parse_file, parse_other_input, solve_part_1, solve_part_2


part_1_tests = [[["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"], 12]]
part_2_tests = [[["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"], "fgij"]]


class TestPart1(unittest.TestCase):
    def test_pass_1(self):
        for i in part_1_tests:
            input = i[0]
            correct = i[1]
            data = parse_other_input(input)
            answer = solve_part_1(data)
            self.assertEqual(correct, answer)


class TestPart2(unittest.TestCase):
    def test_pass_2(self):
        for i in part_2_tests:
            input = i[0]
            correct = i[1]
            data = parse_other_input(input)
            answer = solve_part_2(data)
            self.assertEqual(correct, answer)


if __name__ == '__main__':
    unittest.main()
