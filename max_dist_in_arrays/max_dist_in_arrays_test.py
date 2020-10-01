import unittest

from max_dist_in_arrays.solution import Solution


class MaxDistInArraysTest(unittest.TestCase):

    def test_solution(self):

        s = Solution()

        tests = [
            ([[1,2,3], [4,5], [1,2,3]], 4),
            ([[1, 4], [0, 5]], 4),
            ([[-1,1],[-3,1,4],[-2,-1,0,2]], 6),

        ]

        for test in tests:
            vals   = test[0]
            expected = test[1]

            print("vals = " + str(vals) + " expected_list = " + str(expected))
            actual = s.maxDistance(vals)
            self.assertEqual(expected, actual)
            print("vals = " + str(vals) + " expected_list = " + str(expected) + " actual = " + str(actual))

            # self.assertEqual(expected_list, actual)
