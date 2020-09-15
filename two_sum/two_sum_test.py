import unittest

from two_sum.solution import Solution


class MyTestCase(unittest.TestCase):

    def test_two_sum(self):
        s = Solution()

        nums = [2,7,11,15]
        target = 9
        result = s.twoSum(nums, target)
        self.assertEqual(result, [0,1])


        nums = [-1,-2,-3,-4,-5]
        target = -8
        result = s.twoSum(nums, target)
        self.assertEqual(result, [2,4])


    def test_two_sum_two_pass_hash(self):
        s = Solution()

        nums = [2,7,11,15]
        target = 9
        result = s.twoSumTwoPassHash(nums, target)
        self.assertEqual(result, [0,1])


        nums = [-1,-2,-3,-4,-5]
        target = -8
        result = s.twoSumTwoPassHash(nums, target)
        self.assertEqual(result, [2,4])


    def test_two_sum_one_pass_hash(self):
        s = Solution()

        # nums = [2,7,11,15]
        # target = 9
        # result = s.twoSumOnePassHash(nums, target)
        # self.assertEqual(result, [0,1])
        #
        #
        # nums = [-1,-2,-3,-4,-5]
        # target = -8
        # result = s.twoSumOnePassHash(nums, target)
        # self.assertEqual(result, [2,4])
        #

        nums = [3,3]
        target = 6
        result = s.twoSumOnePassHash(nums, target)
        self.assertEqual(result, [0,1])

