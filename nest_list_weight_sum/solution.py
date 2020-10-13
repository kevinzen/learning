
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """
       pass

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """
       pass

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """
       pass

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """
       pass

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """
       pass

   def getList(self) -> []:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """
       pass


class Solution:
    def depthSumInverse(self, nestedList: [NestedInteger]) -> int:

        sums = []

        def next_depth(depth: int, element: NestedInteger):

            if not element:
                return

            # if we've got an integer, return val*depth, else dig deeper

            if element.getInteger():
                sums.append((depth, element.getInteger()))
            else:
                list_val = element.getList()
                for i in range(len(list_val)):
                    print(str(list_val[i]))
                    next_depth(depth + 1, list_val[i])

        for i in range(len(nestedList)):
            print(str(nestedList[i]))
            next_depth(1, nestedList[i])

        total = 0
        max_depth = 0
        for val in sums:
            if val[0] > max_depth:
                max_depth = val[0]

        for val in sums:
            total = total + (max_depth - val[0] + 1) * val[1]

        return total

