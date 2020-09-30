"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':

        if not head or head.next == None:
            head = Node(val=insertVal)
            head.next = head
            return head

        init_val = None
        node = head
        while not (node.val == init_val and node == head):

            if init_val == None:
                init_val = node.val
            cur_node = node
            next_node = node.next

            if cur_node.next == next_node.next:
                new_node = Node(val=insertVal, next=next_node)
                cur_node.next = new_node
                return head

            # [3, 4, 1] 2
            if cur_node.val <= insertVal and next_node.val > insertVal:
                new_node = Node(val=insertVal, next=next_node)
                cur_node.next = new_node
                return head

            # [3,5,1] 0 -> [3,5,0,1]
            if cur_node.val > insertVal and next_node.val > insertVal and cur_node.val > next_node.val:
                new_node = Node(val=insertVal, next=next_node)
                cur_node.next = new_node
                return head

            # [3,5,1] 6
            # [3,5,1] 5 -> [3,5,5,1]
            if cur_node.val <= insertVal and next_node.val < insertVal and cur_node.val > next_node.val:
                new_node = Node(val=insertVal, next=next_node)
                cur_node.next = new_node
                return head

            if next_node == head:
                new_node = Node(val=insertVal, next=next_node)
                cur_node.next = new_node
                return head

            node = next_node

        return head


