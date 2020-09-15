import unittest

from median_sorted_arrays.solution import Solution


class MedianSortedArraysTest(unittest.TestCase):

    def test_median_sorted_arrays_test(self):
        s = Solution()

        tests = [
            ([1, 3], [2],    2.00000),
            ([1, 2], [3, 4], 2.50000),
            ([0, 0], [0, 0], 0.00000),
            ([],     [1],    1.00000),
            ([2],    [],     2.00000)
        ]

        for test in tests:
            nums1  = test[0]
            nums2  = test[1]
            result = test[2]

            median = s.median_sorted_arrays(nums1, nums2)
            self.assertEqual(result, median)
