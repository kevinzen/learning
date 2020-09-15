# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):


    def merge_sort(self,list):

        # 1. return if at the bottom
        #  -- In this case, we are at the bottom when the list size is one (or zero)
        # 2. Divide
        #  -- In this case, we divide into two pieced, left and right, and then pass each to be further divided
        # 3. Conquer
        #  -- In this case, we merge by looping thru left and right and iteratively building a new array

        # a list of 1 or zero is already sorted
        if len(list) <= 1:
            print("one or zero length - at bottom ", end=': ')
            print(list)
            return list

        extra = len(list) % 2                     # 0 if even, 1 if odd
        mid_index = len(list)//2 + extra          # note 4//2 = 2, 5//2 = 2, 6//2 = 3, 7//2 = 3, etc

        left = list[:mid_index]
        right = list[mid_index:]

        print("list",list,"left",left,"right",right,  end=': ')
        print("")
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        result = self.merge(left, right)
        return result

    def merge(self, left, right):

        print("in merge ")
        result = []
        while len(left) != 0 and len(right) != 0:

            if left[0] <= right[0]:                          # [1,2] -v- [3] => [1], then [1,2], then below => [1,2,3]
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        # add the remainders together. note: At this point, either left or right is an empty list ([])
        result = result + left + right
        return result


    # test just the splitting up part
    def split_list(self, l):

        extra = len(l) % 2                     # 0 if even, 1 if odd
        mid_index = len(l)//2 + extra          # note 4//2 = 2, 5//2 = 2, 6//2 = 3, 7//2 = 3, etc

        left = l[:mid_index]
        right = l[mid_index:]

        return left, right



