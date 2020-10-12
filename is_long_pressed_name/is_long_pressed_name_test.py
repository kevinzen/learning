
import unittest

from is_long_pressed_name.solution import Solution



class SolutionTest(unittest.TestCase):

    def test_solution(self):

        s = Solution()

        tests = [
            ("alex", "aaleex", True),
            ("saeed", "ssaaedd", False),
            ("leelee", "lleeelee", True),
            ("laiden", "laiden", True),
            ("vtkgn", "vttkgnn", True),
            ("xnhtq", "xhhttqq", False),
            ("ppyplrza", "pyypllrza", False),
        ]

        for test in tests:
            name = test[0]
            typed = test[1]
            expected = test[2]

            print("name=" + str(name) + " typed=" + str(typed) + " expected=" + str(expected))
            actual = s.is_long_pressed_name(name, typed)
            print("name=" + str(name) + " typed=" + str(typed) + " expected=" + str(expected) + " actual = " + str(actual))
            self.assertEqual(expected, actual)

