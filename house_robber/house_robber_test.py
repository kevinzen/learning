
import unittest

from house_robber.solution import Solution


class SolutionTest(unittest.TestCase):

    def test_solution(self):

        s = Solution()


        tests = [
            ([1,1,3,6,7,10,7,1,8,5,9,1,4,4,3], 41),
            ([1,1,3,6,7,10,7,1,8,5,9,1,4,4,3], 41),
            # ([94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61, 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397, 52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72],2926)
        ]

        for test in tests:
            input = test[0]
            expected = test[1]

            print("input=" + str(input) + " expected=" + str(expected))
            actual = s.rob(input)
            print("input=" + str(input) + " expected=" + str(expected) + " actual = " + str(actual))
            self.assertEqual(expected, actual)


