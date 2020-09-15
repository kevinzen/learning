import unittest

from sort_merge.solution import Solution


class SortMergeTest(unittest.TestCase):

    def test_sort_merge(self):
        s = Solution()

        tests = [
            ([2, 3, 9, 1, 4, 5, 7, 6, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
            # ([-1, 2, 0, -2, 1, 4, -3, 3], [-3, -2, -1, 0, 1, 2, 3, 4])
        ]

        for test in tests:
            nums   = test[0]
            result = test[1]

            print(nums)
            output = s.merge_sort(nums)
            self.assertEqual(result, output)

    def test_left_right(self):

        # array, left split, right split
        tests = [
            ([2, 3, 9, 1, 5, 7, 6, 8], [2, 3, 9, 1], [5, 7, 6, 8]),
            ([2, 3, 9, 1, 4, 5, 7, 6, 8], [2, 3, 9, 1, 4], [5, 7, 6, 8]),
            ([1, 2], [1], [2]),
            ([2], [2], []),
            ([], [], []),
        ]

        for test in tests:
            l   = test[0]
            left = test[1]
            right = test[2]

            s = Solution()
            left_return, right_return = s.split_list(l)
            print(l,  end='--> ')
            print(left_return, right_return, end=', ')
            print("")
            self.assertEqual(left, left_return)
            self.assertEqual(right, right_return)
