# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        carry = 0
        last_node = None
        return_node = None
        while l1 or l2 or carry == 1:

            if l1:
                l1_val = l1.val
            else:
                l1_val = 0

            if l2:
                l2_val = l2.val
            else:
                l2_val = 0

            sum =  l1_val + l2_val + carry
            if sum >= 10:
                sum = sum - 10
                carry = 1
            else:
                carry = 0

            if last_node:
                last_node.next = ListNode(val=sum)
                last_node = last_node.next
            else:
                last_node = ListNode(val=sum)
                return_node = last_node

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return return_node


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val
