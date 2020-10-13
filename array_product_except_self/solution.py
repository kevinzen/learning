
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def array_product_except_self(self, nums: [int]) -> [int]:

        output = [1]*len(nums)

        cumulative = 1
        for i in range(1, len(nums)):
            cumulative = cumulative * nums[i-1]
            output[i] = cumulative

        cumulative = 1
        for i in range(len(nums) - 2, -1, -1):
            cumulative = cumulative * nums[i+1]
            output[i] = cumulative * output[i]

        return output








