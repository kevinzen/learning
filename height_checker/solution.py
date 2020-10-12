

# [1,1,4,2,1,3]
# Move 4, 1, 3 => [1,1,1,2,3,4]
# pull 1 and put at end of lowest
# 3)

# => create a set
# get counts for each
# create the ideal set
# find the number of changes
# [1,1,4,2,1,3]
# [1,1,1,2,3,4]

from collections import deque
from sortedcontainers.sortedset import SortedList
class Solution:

    def height_checker(self, heights: []) -> int:

        height_counts = {}
        for height in heights:
            cur_count = height_counts.get(height, 0)
            height_counts[height] = cur_count + 1

        sorted_heights = sorted(height_counts.keys())
        in_order = deque()
        for sorted_height in sorted_heights:
            in_order = in_order + deque([sorted_height]*height_counts.get(sorted_height,0))

        movers = 0
        for student in heights:
            in_order_height = in_order.popleft()
            if student != in_order_height:
                movers = movers + 1

        return movers










