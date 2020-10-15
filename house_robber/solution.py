from collections import deque

class Solution:

    def rob(self, nums: [int]) -> int:

        if len(nums) == 0:
            return 0
        length = len(nums)
        if length == 1:
            return nums[0]
        elif length == 2:
            return max(nums)

        def try_it(nums: [int]) -> int:
            if len(nums) == 0:
                return 0
            length = len(nums)
            if length == 1:
                return nums[0]
            elif length == 2:
                return max(nums)
            length = len(nums)
            results = [0] * length
            results[0] = nums[0]
            results[1] = nums[1]
            results[2] = nums[0] + nums[2]
            for i in range(3, length):
                results[i] = max(results[i - 2], results[i - 3]) + nums[i]
            # for i in range(len(nums)):
            #     print("i / val / sum " + str(i) + ' / ' + str(nums[i]) + ' / ' + str(results[i]))

            return max(results[-1], results[-2])

        run1 = try_it(nums[:len(nums) - 1])
        run2 = try_it(nums[1:len(nums)])

        return max(run1, run2)

    def rob_orig(self, nums: [int]) -> int:

        length = len(nums)
        if length == 1:
            return nums[0]
        elif length == 2:
            return max(nums)

        valid_sums = deque()

        def try_next(start: int, index: int, sum_to_here: int):

            if start == 0 and index > length - 2:
                valid_sums.append(sum_to_here)
                return
            elif index > length - 1:
                valid_sums.append(sum_to_here)
                return

            sum_to_here = sum_to_here + nums[index]

            try_next(start, index + 2, sum_to_here)
            try_next(start, index + 3, sum_to_here)

        try_next(0, 0, 0)
        try_next(1, 1, 0)
        try_next(2, 2, 0)

        return max(valid_sums)



