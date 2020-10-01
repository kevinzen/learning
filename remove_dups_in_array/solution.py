
class Solution:

    def removeDuplicates(self, nums) -> int:

        # [1,2,2]
        # i = 1, cur_val = 2 -> cur_val == nums[1], remove(2)
        # i = 0, cur_val = 1 -> cur_val != nums[0] -> cur_val = 1

        # [2,2,2]
        # i = 1, cur_val = 2 -> cur_val == nums[1], remove(2)
        # i = 0, cur_val = 1 -> cur_val == nums[0], remove(2)

        # [1,2,3]
        # i = 1, cur_val = 3 -> cur_val != nums[1], cur_val = 2
        # i = 0, cur_val = 2 -> cur_val != nums[0], cur_val = 1

        # [1,2,2]
        # i = 1, cur_val = 2 (nums(len-1)) -> cur_val == nums[i], remove cur_val
        # i = 0, cur_val = 2 -> cur_val != nums[i], set cur_val = 1

        length = len(nums)
        if length in [0,1]:
            return length

        # has at least 2 values
        cur_val = nums[length-1]
        for i in range(length-2, -1, -1):
            if cur_val != nums[i]:
                cur_val = nums[i]
            else:
                nums.remove(cur_val)

        return len(nums)
