
import unittest

from license_key_processing.solution import Solution


class SolutionTest(unittest.TestCase):

    def test_solution(self):

        s = Solution()


        tests = [
            ("5F3Z-2e-9-w", 4, "5F3Z-2E9W"),
            ( "2-5g-3-J", 2, "2-5G-3J")
        ]

        for test in tests:
            input = test[0]
            k = test[1]
            expected = test[2]

            print("input=" + str(input) + " expected=" + str(expected))
            actual = s.licenseKeyFormatting(input, k)
            print("input=" + str(input) + " expected=" + str(expected) + " actual = " + str(actual))
            self.assertEqual(expected, actual)


