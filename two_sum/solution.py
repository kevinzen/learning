class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # time complexity O(n^2)
        # space complexity O(1)
        for index in range(len(nums)):
            # if nums[index] <= target:
            for index_1 in range(len(nums)):
                if index != index_1:
                    if nums[index] + nums[index_1] == target:
                        return [index, index_1]

    def twoSumTwoPassHash(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # time complexity = O(n) - one full pass required
        # space complexity = O(n) - requires one space per item

        # create lookup hash
        lookup_1 = {}
        for index in range(len(nums)):
            lookup_1[nums[index]] = index

        # Second pass thru
        for index in range(len(nums)):
            if lookup_1.get(target - nums[index]) and nums[index] != lookup_1.get(target - nums[index]):
                return [index, lookup_1[target - nums[index]]]

    def twoSumOnePassHash(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # time complexity = O(n)
        # space complexity = O(n)

        # nums = [2,7,11,15], target 9
        # create lookup hash
        lookup = {}
        for index in range(len(nums)):
            compliment = target - nums[index]
            if lookup.get(compliment) != None and lookup.get(compliment) != index:
                return [lookup[compliment], index]
            lookup[nums[index]] = index

