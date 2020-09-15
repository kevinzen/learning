import unittest

from reverse_integer.solution import Solution


class ReverseIntegerTest(unittest.TestCase):

    def test_reverse_integer(self):
        s = Solution()

        tests = [
            (0, 0),
            (123, 321),
            (123456789, 987654321),
            (-1,-1),
            (-123,-321),
            (1534236469,0),
            (2147483647,0),
            (1463847412, 2147483641)
        ]

        for test in tests:
            input   = test[0]
            expected = test[1]

            actual = s.reverse_integer(input)
            print("input = " + str(input) + ", actual = " + str(actual) + ", expected = " + str(expected))
            self.assertEqual(expected, actual)
