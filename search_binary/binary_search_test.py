import unittest

from search_binary.solution import Solution


class BinarySearchTest(unittest.TestCase):

    def test_binary_search(self):
        s = Solution()

        tests = [
            ([2, 3, 4, 6, 9, 11, 12, 17, 18], 11, [5]),      # 11 is at index 5
            ([2, 3, 4, 6, 9, 11, 12, 17, 18], 2, [0]),       # 2 is at index 0
            ([2, 3, 4, 6, 9, 11, 12, 17, 18], 18, [8]),      # 18 is at index 8
            ([2, 3, 4, 6, 9, 11, 12, 17, 18], 10, [-1]),       # 10 is not in list
            ([2, 3, 4, 6, 9, 11, 11, 17, 18], 11, [5,6]),    # 11 is at index 5 or 6
        ]

        for test in tests:
            nums   = test[0]
            target = test[1]
            result = test[2]

            print(nums)
            output = s.binary_search(nums, target)
            self.assertIn( output, result)

    def test_binary_search_leftmost(self):
        s = Solution()

        tests = [
            ([2, 3, 4, 6, 9, 11, 12, 17, 18], 11, [5]),      # 11 is at index 5
            ([2, 3, 4, 6, 9, 11, 12, 17, 18], 2, [0]),       # 2 is at index 0
            ([2, 3, 4, 6, 9, 11, 12, 17, 18], 18, [8]),      # 18 is at index 8
            ([2, 3, 4, 6, 9, 11, 12, 17, 18], 10, [-1]),       # 10 is not in list
            ([2, 3, 4, 6, 9, 11, 11, 17, 18], 11, [5]),    # 11 is at index 5 or 6, but leftmost is 5
            ([2, 2, 2, 2, 2, 2, 2, 2, 2], 2, [0]),  # 11 is at index 5 or 6, but leftmost is 5
        ]

        for test in tests:
            nums   = test[0]
            target = test[1]
            result = test[2]

            print(nums)
            output = s.binary_search_leftmost(nums, target)
            self.assertIn( output, result)

    def test_binary_search_rightmost(self):
        s = Solution()

        tests = [
            ([2, 3, 4, 6, 9, 11, 12, 17, 18], 11, [5]),      # 11 is at index 5
            ([2, 3, 4, 6, 9, 11, 12, 17, 18], 2, [0]),       # 2 is at index 0
            ([2, 3, 4, 6, 9, 11, 12, 17, 18], 18, [8]),      # 18 is at index 8
            ([2, 3, 4, 6, 9, 11, 12, 17, 18], 10, [-1]),       # 10 is not in list
            ([2, 3, 4, 6, 9, 11, 11, 17, 18], 11, [6]),    # 11 is at index 5 or 6, but leftmost is 5
            ([2, 2, 2, 2, 2, 2, 2, 2, 2], 2, [8]),  # 11 is at index 5 or 6, but leftmost is 5
        ]

        for test in tests:
            nums   = test[0]
            target = test[1]
            result = test[2]

            print(nums)
            output = s.binary_search_rightmost(nums, target)
            self.assertIn( output, result)
