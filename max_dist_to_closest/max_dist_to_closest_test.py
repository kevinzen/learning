
import unittest

from max_dist_to_closest.solution import Solution


class MaxDistToClosestTest(unittest.TestCase):

    def test_solution(self):

        s = Solution()

        tests = [
            ([1, 0, 0, 0, 1, 0, 1], 2),
            ([0, 1], 1),
        ]

        for test in tests:
            input = test[0]
            expected = test[1]

            # print("input=" + str(input) + " expected=" + str(expected))
            actual = s.max_distance_to_closes(input)
            # print("input=" + str(input) + " expected=" + str(expected) + " actual = " + str(actual))
            self.assertEqual(expected, actual)

