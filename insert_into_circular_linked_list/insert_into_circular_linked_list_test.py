import unittest

from insert_into_circular_linked_list.solution import Solution


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class InsertIntoCircularLinkedListTest(unittest.TestCase):

    def test_solution(self):

        s = Solution()

        """
        Input: head = [3,4,1], insertVal = 2
        Output: [3,4,1,2]
        """
        tests = [
            ([3,4,1], 2, [3,4,1,2]),
            ([3,4,1], 1, [3,4,1,1]),
            ([3,4,1,2], 1, [3,4,1,1,2]),
            ([], 2, [2]),
            ([1,1], 2, [1,1,2]),
            ([1,1], 0, [1,1,0]),
            ([1, 1,  1], 1, [1, 1, 1, 1]),
            ([3, 5, 1], 0, [3, 5, 0, 1]),
            ([3, 5, 1], 6, [3, 5, 6, 1]),
            ([3, 5, 1], 5, [3, 5, 5, 1]),
        ]

        for test in tests:
            vals   = test[0]
            insertVal = test[1]
            expected_list = test[2]

            head = self.listToLinkedList(vals)
            expected_linked_list = self.listToLinkedList(expected_list)

            print("vals = " + str(vals) + " insertVal = " + str(insertVal))
            actual = s.insert(head=head, insertVal=insertVal)
            actual_list = self.linked_list_to_list(actual)
            print("vals = " + str(vals) + " insertVal = " + str(insertVal) + " actual = " + str(actual_list))
            self.assertTrue(self.compare_lists(expected=expected_linked_list, actual=actual))

            # self.assertEqual(expected_list, actual)

    def linked_list_to_list(self, linked_list) -> list:

        if linked_list.next == None:
            return []

        head = linked_list
        node = head
        end_node = None
        ret_val = []
        while node != end_node:
            if end_node == None:
                end_node = head
            ret_val.append(node.val)
            node = node.next

        return ret_val

    def compare_lists(self, expected, actual) -> bool :

        head = expected
        end_node = None
        while expected != end_node:
            end_node = head
            if expected.val  !=  actual.val:
                return False
            actual, expected = actual.next, expected.next

        return True

    def listToLinkedList(self, list) -> Node :

        if not list:
            return Node()

        is_first = True
        tail = None
        node = None
        for val in reversed(list):
            node = Node(val=val, next=node)
            if is_first:
                tail = node
                is_first = False
        tail.next = node

        return node


