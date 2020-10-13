
import unittest

from array_product_except_self.solution import Solution


class SolutionTest(unittest.TestCase):

    def test_solution(self):

        s = Solution()

        tests = [
            ([1, 2, 3, 4], [24, 12, 8, 6]),
        ]

        for test in tests:
            input = test[0]
            expected = test[1]

            print("input=" + str(input) + " expected=" + str(expected))
            actual = s.array_product_except_self(input)
            print("input=" + str(input) + " expected=" + str(expected) + " actual = " + str(actual))
            self.assertEqual(expected, actual)


