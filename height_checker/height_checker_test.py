
import unittest

from height_checker.solution import Solution


class SolutionTest(unittest.TestCase):

    def test_solution(self):

        s = Solution()

        tests = [
            ([1,1,4,2,1,3], 3),
        ]

        for test in tests:
            input = test[0]
            expected = test[1]

            # print("input=" + str(input) + " expected=" + str(expected))
            actual = s.height_checker(input)
            # print("input=" + str(input) + " expected=" + str(expected) + " actual = " + str(actual))
            self.assertEqual(expected, actual)

