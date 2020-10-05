
import unittest

from combination_sum.solution import Solution


class ComboSumTest(unittest.TestCase):

    def test_solution(self):

        s = Solution()

        tests = [
            ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
            ([1, 2, 3], 3, [[3], [1,2], [1,1,1]]),
            ([2, 3, 5], 8, [[2,2,2,2],[2,3,3],[3,5]])
        ]


        for test in tests:
            vals   = test[0]
            target = test[1]
            expected = test[2]

            print("vals = " + str(vals) + " expected_list = " + str(expected))
            actual = s.combo_sum(vals, target)
            print("vals = " + str(vals) + " expected_list = " + str(expected) + " actual = " + str(actual))
            self.assertEqual(len(expected), len(actual))
            for entry in actual:
                self.assertIn(entry, expected)

            # self.assertEqual(expected_list, actual)
