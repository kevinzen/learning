# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def reverse_integer(self,x):

        if x >= 2**31-1 or x <= -2**31:
            return 0
        neg = x < 0
        s = str(abs(x))
        s = s[::-1]
        while s[0] == '0' and len(s) > 1:
            s = s[1:len(s)]
        if neg:
            s = '-' + s
        return_val = int(s)
        if x >= 2**31-1 or x <= -2**31 or return_val >= 2**31-1 or return_val <= -2**31:
            return 0
        else:
            return return_val

