
import unittest

from nest_list_weight_sum.solution import Solution


class SolutionTest(unittest.TestCase):

    def test_solution(self):

        s = Solution()

        tests = [
            ([[1, 1], 2, [1, 1]], 8),
            ([1, [4, [6]]], 17),
        ]

        for test in tests:
            input = test[0]
            expected = test[1]

            print("input=" + str(input) + " expected=" + str(expected))
            actual = s.depthSumInverse(input)
            print("input=" + str(input) + " expected=" + str(expected) + " actual = " + str(actual))
            self.assertEqual(expected, actual)

