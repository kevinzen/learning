import unittest

from sort_insertion.solution import Solution


class SortInsertionTest(unittest.TestCase):

    def test_sort_insertion(self):
        s = Solution()

        tests = [
            ([2, 3, 9, 1, 4, 5, 7, 6, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
            ([-1, 2, 0, -2, 1, 4, -3, 3], [-3, -2, -1, 0, 1, 2, 3, 4])
        ]

        for test in tests:
            nums   = test[0]
            result = test[1]

            print(nums)
            output = s.sort_insertion(nums)
            self.assertEqual(result, output)

    def test_ranges(self):
        print("\nrange(stop)")
        stop = 5
        for i in range(stop):  # => 0,1,2,3,4
            print(i, end=',')

        stop = 5
        start = 2
        print("\nrange(start, stop)")
        for i in range(start, stop):  # => 2,3,4
            print(i, end=',')

        start = 5
        stop = 0
        step = -1
        print("\nrange(start, stop, step)")
        for i in range(start, stop, step):  # => 5,4,3,2,1
            print(i, end=',')
