# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def sort_insertion(self, nums):
        """
        :type nums: List
        :rtype: List
        """
        '''
        i ← 1
        while i < length(A)
            j ← i
            while j > 0 and A[j-1] > A[j]
                swap A[j] and A[j-1]
                j ← j - 1
            end while
            i ← i + 1
        end while
        '''

        # [3,2,1,0]
        # [2,3,1,0]
        nums_init = nums
        for i in range(1, len(nums)): # 1, 2, 3
            for j in range(i-1, -1, -1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        # print(nums, nums_init)
        return nums

        # learned:
        # - walk thru multiple loops
        # - use specific examples and walk thru
        # - use range to control looping thru arrays











