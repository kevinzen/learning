
import unittest

from rotated_digits.solution import Solution


class RotatedDigitsTest(unittest.TestCase):

    def test_solution(self):

        s = Solution()

        tests = [
            (10, 4)
        ]

        for test in tests:
            number = test[0]
            good_numbers_count = test[1]

            print("number=" + str(number) + " good_numbers_count=" + str(good_numbers_count))
            actual = s.good_numbers(number)
            print("number=" + str(number) + " good_numbers_count=" + str(good_numbers_count) + " actual = " + str(actual))
            self.assertEqual(good_numbers_count, actual)

