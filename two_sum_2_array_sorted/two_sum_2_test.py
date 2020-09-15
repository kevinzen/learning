import unittest

from two_sum_2_array_sorted.solution import Solution


class MyTestCase(unittest.TestCase):

    def test_two_sum(self):
        s = Solution()

        nums = [2,7,11,15]
        target = 9
        result = s.twoSum(nums, target)
        self.assertEqual( [1,2], result)


        nums = [-5,-4,-3,-2,-1]
        target = -8
        result = s.twoSum(nums, target)
        self.assertEqual([1,3], result)


    def test_two_sum_one_pass_hash(self):
        s = Solution()

        nums = [2,7,11,15]
        target = 9
        result = s.two_sum_one_pass(nums, target)
        self.assertEqual(result, [1,2])


        nums = [-5,-4,-3,-2,-1]
        target = -8
        result = s.two_sum_one_pass(nums, target)
        self.assertEqual(result, [1,3])

