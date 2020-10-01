
class Solution:

    def maxDistance(self, arrays) -> int:

        # [[1,2,3], [4,5], [1,2,3]]
        # i = 0, cur_min = 1, cur_max = 3, tot_min = 1, tot_max = 3, min_dist = None, max_dist = None
        # i = 1, cur_min = 4, cur_max = 5, tot_min = 1, tot_max = 3, min_dis = abs(3-4), max_dist = abs(5-1)
        # i = 2, cur_min = 1, cur_max = 3, tot_min = 1, tot_max = 5, min_dis = abs(5-1), max_dist = abs(3-1)
        # general: cur_min = 1, cur_max = 3, tot_min = 1, tot_max = 5, min_dis = abs(tot_max-cur_min), max_dist = abs(cur_max-tot_min)

        # [[1,4], [0,5]], expected = 4
        # i = 0, min = 1, max = 4, min_dist = None, max_dist = None
        # i = 1, min = 1, max = 5, min_dis = abs(0-4), max_dist = abs(5-1)
        # i = 2, min = 1, max = 5
        # distance = max - min = 4

        # [[-1, 1], [-3, 1, 4], [-2, -1, 0, 2]], expected = 6
        # i = 0, cur_min = -1, cur_max = 1, min_dist = None, max_dist = None
        # i = 1, cur_min = -3, cur_max = 4, min_dis = abs(1-(-3)), max_dist = abs(4-(-1)), dist = 5
        # i = 2, cur_min = -2, cur_max = 2, min_dis = abs(4-(-2))
        # distance = max - min = 4

        tot_max = tot_min = None
        distance = min_dist = max_dist = 0

        for i in range(len(arrays)):
            array = arrays[i]
            cur_min = array[0]
            cur_max = array[len(array) - 1]

            if tot_min != None:
                min_dist = abs(tot_max - cur_min)
                max_dist = abs(cur_max - tot_min)
                if distance < min_dist:
                    distance = min_dist
                if distance < max_dist:
                    distance = max_dist

            if tot_min == None or cur_min < tot_min:
                tot_min = cur_min

            if tot_max == None or cur_max > tot_max:
                tot_max = cur_max

        return distance

