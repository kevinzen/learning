
class Solution:

    from sortedcontainers.sortedlist import SortedList

    # nums = [2, 3, 6, 7], target = 7, ans = [[2, 2, 3], [7]]

    # start with 7:
    # target - nums[len-1] = 0 => got 0, return [[7]]

    # now to 6
    # target - nums[len-2] = 1. nums.lbisect(1) == [], False

    # now to 3
    # target - nums[len-3] = 4. nums.lbisect(4) == [2,3], try both
    #   (target - 3) - 3 = 1. nums.lbisect(1) = [], False
    #   (target - 3) - 2 = 2. nums.lbisect(2) = [2], continue
    #   (target - 3 - 2) - 2 = 0 => return [[3,2,2]]

    # now to 2
    # target - 2 = 5. nums.lbisect(5) = [3,2] continue only 2 since 3's are done
    # (target - 2) - 2 = 3 nums.lbisect(3) = [3,2] continue only 2 since 3' done
    # (target - 2 - 2) - 2 = 1. nums.lbisect(1) = [], stop

    # need recursive function with inputs: target, [already sub'd], [remaining vals]
    # target = orig target - all so far, number on, [remaining vals]

    def combo_sum(self, candidates: [int], target: int) -> [[int]]:
        from sortedcontainers.sortedlist import SortedList

        nums_sorted = SortedList(candidates)

        result = []
        for i in range(len(nums_sorted)-1, -1, -1):
            part_result = self.func(target, nums_sorted[i], nums_sorted )
            if part_result != False:
                result = result + part_result
            nums_sorted.remove(nums_sorted[i])

        return result

    def func(self, target, cur_num, remaining_nums: SortedList):
        from sortedcontainers.sortedlist import SortedList

        # 1. determine when we're at bottom
        # 2. determine results for this level and how to call again
        # 3. combine results and return

        # 1. return when 1) we get to 0, or 2) left bisect returns []
        new_target = target - cur_num
        if new_target == 0:
            return [[cur_num]]

        offset_to_remaining = remaining_nums.bisect_left(new_target+1)
        if offset_to_remaining == 0:
            return False
        new_remaining_nums = SortedList(remaining_nums[:offset_to_remaining])

        # 7 - 3 = 4. [1,2,3] are lower.
        # call with 3 -> [3,3,1]

        results = []
        for j in range(len(new_remaining_nums)-1,-1,-1):

            ret_val = self.func(new_target, new_remaining_nums[j], new_remaining_nums)

            # cur_num == 4,
            #  - 3 returns [[3,1]].
            #  - 2 returns [[2,2],[2,1,1]],
            #  - 1 returns [[1,1,1,1]]
            # need to return [[3,3,1], [3,2,2], [3,2,1,1], [3,1,1,1,1]]

            if ret_val != False:
                for entry in ret_val:
                    entry = entry + [cur_num]
                    entry.sort()
                    # if entry not in results:
                    if entry not in results:
                        results = results + [entry]

        return results


    def combinationSum_backtrack(self, candidates: [int], target: int) -> [[int]]:

        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], comb, i)
                # backtrack, remove the number from the combination
                comb.pop()

        backtrack(target, [], 0)

        return results


    def combinationSum_backtrack_new(self, candidates: [int], target: int) -> [[int]]:

        """
        procedure bt(c) is
            if reject(P, c) then return
            if accept(P, c) then output(P, c)
            s ← first(P, c)
            while s ≠ NULL do
                bt(s)
                s ← next(P, s)
        """

        results = []

        def backtrack(remain, comb, start):

            # backtrack general three items:
            # 1. did we find a solution? If so, 'output' it.
            # 2. If we've hit a terminal wrong move, just return
            # 3. If we can keep moving forward,
            #    -- output current state
            #    -- move forward with next option

            if remain == 0:
                # if accept(P, c) then output(P, c)
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                # if reject(P, c) then return
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], comb, i)
                # backtrack, remove the number from the combination
                comb.pop()

        backtrack(target, [], 0)

        return results
