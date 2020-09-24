# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def contains_nearby_almost_duplicate(self, nums, k, t):

        # [2, 1, 3, 1], k = 3, t = 0, True
        # [1, 5, 9, 1, 5, 9], 2, 3, False
        # [0, 5, 0], k = 2, t = 4, True

        seen = {}
        for i in range(len(nums)):

            min = i - k
            if min <= 0:
                min = 0

            # work with indexes only -- range => 0..len(nums)-1
            cur_num = nums[i]
            for j in range(min,i):  # max value of range(0,n) = n-1
                if seen.get(nums[j], None) != None and i != j:
                    if abs(nums[j] - cur_num) <= t:
                        print(nums, i, nums[i])
                        return True

            seen[nums[i]] = nums[i]

        return False

    def contains_nearby_almost_duplicate_sortedset(self, nums, k, t):
        from sortedcontainers import SortedList

        if k == 0:
            return False

        # For each item in nums, up to k before the end
        s_list = SortedList(nums[1:k])
        length = len(nums)
        for i in range(len(nums)-1):

            if i+k < length:
                s_list.add(nums[i+k])

            num = nums[i]

            s_left  = s_list.bisect_left(num)
            s_right = s_list.bisect_right(num)

            if s_left != s_right:  # number is in list, return true
                return True
            elif s_left == 0:
                if abs(num - s_list[s_left]) <= t:
                    return True
            elif s_left == len(s_list):
                if abs(num - s_list[s_left-1]) <= t:
                    return True
            else:
                if abs(num - s_list[s_left]) <= t or abs(num - s_list[s_left-1]) <= t:
                    return True

            s_list.remove(nums[i+1])

        return False

    def contains_nearby_almost_duplicate_merge(self, nums, k, t):
        if k == 0 or len(nums) in [0,1]:
            return False

        for i in range(len(nums) - k):

            if i + k >= len(nums):
                end = len(nums)
            else:
                end = i + k + 1

            sorted = self.sort(nums[i:end])
            for j in range(len(sorted)-1):
                if abs(sorted[j] - sorted[j+1]) <= t:
                    return True
        return False

    def sort(self, list):
        # a list of one is already sorted
        if len(list) <= 1:
            return list

        # if len = 11, then extra = 1, half = 5, left = list[:5], right = [6:]
        extra = len(list) % 2
        half_size = len(list) // 2
        mid_index = half_size + extra

        left = list[:mid_index]
        right = list[mid_index:]

        left = self.sort(left)
        right = self.sort(right)

        return self.merge(left, right)

        # 1. return if at the bottom
        # 2. Divide
        # 3. Conquer

    def merge(self, left, right):
        result = []
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        result = result + left + right
        return result

