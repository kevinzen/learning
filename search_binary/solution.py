class Solution(object):

    def binary_search(self, list, target):

        length = len(list)
        min = 0
        max = length - 1
        if length == 0:
            return -1

        # [2, 3, 4, 6, 9, 11, 12, 17, 18]
        # 1: min = 0, max = 7, m = 4, list[m] = 9
        # 2: min = 4, max = 7, m = 5, list[m] = 11
        while max >= min:
            m = (min + max) // 2   # floor
            if list[m] < target:
                min = m + 1
            elif list[m] > target:
                max = m - 1
            else:
                return m

        # not found
        return -1 # not found

    def binary_search_leftmost(self, list, target):

        length = len(list)
        min = 0
        max = length
        if length == 0:
            return -1

        # [2, 3, 4, 6, 9, 11, 12, 17, 18]
        # 1: min = 0, max = 8, m = 4, list[m] = 9
        # 2: min = 5, max = 8, m = 6, list[m] = 12
        # 3: min = 5, max = 6, m = 5, list[m] = 11
        # 4: min = 5, max = 5, m = 5, list[m] = 11
        while max > min:
            m = (min + max) // 2   # floor
            if list[m] < target:
                min = m + 1
            else:
                max = m

        # not found
        if list[m] == target:
            return m
        else:
            return -1 # not found

    def binary_search_rightmost(self, list, target):

        length = len(list)
        min = 0
        max = length
        if length == 0:
            return -1

        # [2, 3, 4, 6, 9, 11, 12, 17, 18]
        # 1: min = 0, max = 8, m = 4, list[m] = 9
        # 2: min = 5, max = 8, m = 6, list[m] = 12
        # 3: min = 5, max = 6, m = 5, list[m] = 11
        # 4: min = 6, max = 6, m = 5
        while max > min:
            m = (min + max) // 2
            if list[m] > target:
                max = m
            else:
                min = m + 1

        # not found
        if list[m] == target:
            return m
        else:
            return -1 # not found




