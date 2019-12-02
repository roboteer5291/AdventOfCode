import unittest
from solution import parse_file, parse_other_input, solve_part_1, solve_part_2


part_1_tests = [["1,9,10,3,2,3,11,0,99,30,40,50", 3500], ["1,0,0,0,99", 2], ["2,3,0,3,99", 2], ["2,4,4,5,99,0", 2], ["1,1,1,4,99,5,6,0,99", 30]]
part_2_tests = [[]]


class TestPart1(unittest.TestCase):
    def test_pass(self):
        for i in part_1_tests:
            input = i[0]
            correct = i[1]
            data = parse_other_input(input)
            answer = solve_part_1(data)
            self.assertEqual(correct, answer)


# class TestPart2(unittest.TestCase):
#     def test_pass(self):
#         for i in part_2_tests:
#             input = i[0]
#             correct = i[1]
#             data = parse_other_input(input)
#             answer = solve_part_2(data)
#             self.assertEqual(correct, answer)


if __name__ == '__main__':
    unittest.main()
