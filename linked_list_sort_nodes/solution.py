
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        def merge(left: [], right: []) -> []:

            result = []
            while len(left) > 0 and len(right) > 0:
                if left[0] <= right[0]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))

            result = result + left + right
            return result

        def sort(vals: []) -> []:

            if len(vals) in [0, 1]:
                return vals

            count = len(vals)
            extra = count % 2
            half_size = count // 2
            mid_index = half_size + extra

            left = sort(vals[:mid_index])
            right = sort(vals[mid_index:])

            result = merge(left, right)

            return result


        node = head
        vals = []
        while node:
            vals.append(node.val)
            node = node.next

        # sort the values
        sorted_vals = sort(vals)

        # now walk the list and replace the values with the sorted values
        # this updates the linked list in place
        node = head
        for i in range(len(sorted_vals)):
            node.val = sorted_vals[i]
            node = node.next

        return head








