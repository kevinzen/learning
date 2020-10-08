
from sortedcontainers.sortedlist import SortedList


class TwoSum:

    # Your TwoSum object will be instantiated and called as such:
    # obj = TwoSum()
    # obj.add(number)
    # param_2 = obj.find(value)

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = SortedList()

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.data.add(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for val in set(self.data):

            to_find = value - val
            left = self.data.bisect_left(to_find)
            right = self.data.bisect_right(to_find)

            diff = right - left # always 0 or greater

            if diff == 0:
                continue
            if diff == 1 and val != to_find: # value exists in set, and not searching for itself (like 4 + 4 == 8)
                return True
            if diff > 1 :  # handle 0 + 0 = 0 (but require more than a single 0)
                return True

        return False






