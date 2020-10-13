
import unittest

from canonical_path.solution import Solution


class SolutionTest(unittest.TestCase):

    def test_solution(self):

        s = Solution()

        tests = [
            ('/..', '/'),
            ('/.', '/'),
            ('/../', '/'),
            ('/.././', '/'),
            ('/../././/', '/'),
            ('/a//b//./c/d/../d/e//.////.//', '/a/b/c/d/e'),
            ('/.././GVzvE/./xBjU///../..///././//////T/../../.././zu/q/e', '/zu/q/e')
        ]

        for test in tests:
            input = test[0]
            expected = test[1]

            print("input=" + str(input) + " expected=" + str(expected))
            actual = s.simplify_path(input)
            print("input=" + str(input) + " expected=" + str(expected) + " actual = " + str(actual))
            self.assertEqual(expected, actual)

