
import unittest

from linked_list_sort_nodes.solution import Solution


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SolutionTest(unittest.TestCase):

    def list_from_array(self, vals: []) -> ListNode:

        next = None
        for i in range(len(vals) - 1, -1, -1):
            next = ListNode(vals[i], next=next)

            # since we init backwards, this will be HEAD
        return next

    def compare_linked_lists(self, expected: ListNode, actual: ListNode):

        while (expected):
            print("expected.val = " + str(expected.val) + " actual.val = " + str(actual.val))
            self.assertEqual(expected.val, actual.val)
            if not expected.next:
                self.assertIsNone(actual.next)  # should also be None
                return
            expected, actual = expected.next, actual.next


    def test_solution(self):

        s = Solution()

        tests = [
            ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5])
        ]

        for test in tests:
            input = test[0]
            expected = test[1]

            print("input=" + str(input) + " expected=" + str(expected))
            head = self.list_from_array(input)
            expected_ll = self.list_from_array(expected)

            actual = s.sortList(head)
            self.compare_linked_lists(expected_ll, actual)

