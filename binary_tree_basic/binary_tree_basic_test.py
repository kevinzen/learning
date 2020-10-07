import unittest

from complement_of_base_10_integer.solution import Solution


class ComplementTest(unittest.TestCase):

    def test_solution(self):

        s = Solution()

        tests = [
            (5, 2),
            (7,0),
            (10, 5)
        ]

        for test in tests:
            val = test[0]
            expected = test[1]

            print("val = " + str(val) + " expected = " + str(expected))
            actual = s.complement(val)
            print("val = " + str(val) + " expected = " + str(expected)  + " actual = " + str(actual))
            self.assertEqual(expected, actual)

            # self.assertEqual(expected_list, actual)
