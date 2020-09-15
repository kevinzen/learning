class Solution(object):

    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # brute force
        for index1 in range(len(nums)):
            for index2 in range(len(nums)):
                if index1 != index2 and (nums[index1] + nums[index2]) == target:
                    return [index1 + 1, index2 + 1]


    def two_sum_one_pass(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for index in range(len(nums)):
            lookup[nums[index]] = index
            compliment = target - nums[index]
            comp_index = lookup.get(compliment, None)
            if comp_index != None and comp_index != index:
                return [comp_index+1, index+  1]





