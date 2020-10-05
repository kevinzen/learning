"""
procedure bt(c) is
    if reject(P, c) then return
    if accept(P, c) then output(P, c)
    s ← first(P, c)
    while s ≠ NULL do
        bt(s)
        s ← next(P, s)
"""

class Solution:

        # backtrack:
        # 1. Reject if we can determine not a solution path, then return
        # 2. Accept if we have found a solution, then return
        # 3. Else, s = first potential solution
        # 4. While still have potential solutions,
        #    - Call bt for next solution
        #    - Get next potential solution
        #    - 'pop' to backtrack

    def combo_sum(self, candidates, target):

        results = []

        def backtrack(target: int, combo: [], current_offset: int):

            if target == 0:
                results.append(list(combo))
                return
            elif target < 0:
                return

            for i in range(current_offset, len(candidates)):

                combo.append(candidates[i])

                backtrack(target-candidates[i], combo, i)

                combo.pop()

            return

        backtrack(target, [], 0)

        return results
