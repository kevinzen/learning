class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    # need to know:
    # how to find tail
    # how to keep node before tail

    def rotate_linked_list(self, head: ListNode, k: int) -> ListNode:

        # a one-element list stays the same no matter how many times rotated.
        node = head
        nodes = []
        while(node):
            nodes.append(node)
            node = node.next

        length = len(nodes)
        if length == 0:
            return head

        new_k = k % length

        # implies rotation back to where it started
        if new_k == 0:
            return head

        new_head = nodes[length-new_k]
        nodes[length - new_k - 1].next = None
        nodes[length - 1].next = nodes[0]

        return new_head
