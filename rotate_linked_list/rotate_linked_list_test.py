import unittest

from rotate_linked_list.solution import Solution, ListNode


class RotateLinkedListTest(unittest.TestCase):

    def test_solution(self):

        def compare_linked_lists(expected: ListNode, actual: ListNode):

            while (expected):
                print("expected.val = " + str(expected.val) + " actual.val = " + str(actual.val))
                self.assertEqual(expected.val, actual.val)
                if not expected.next:
                    self.assertIsNone(actual.next)  # should also be None
                    return
                expected, actual = expected.next, actual.next


        def list_from_array(vals: []) -> ListNode:

            next = None
            for i in range(len(vals)-1, -1, -1):
                next = ListNode(vals[i], next=next)       
            
            # since we init backwards, this will be HEAD
            return next
            
        s = Solution()

        tests = [
            ([1, 2, 3, 4, 5], 2, [4,5,1,2,3]),
            ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
            ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),
            ([1, 2, 3, 4, 5], 10, [1, 2, 3, 4, 5]),
            ([0, 1, 2], 4, [2, 0, 1]),
            ([1], 99, [1]),
            ([], 0, []),
        ]

        for test in tests:
            vals = test[0]
            rotate = test[1]
            expected = test[2]

            vals_ll, expected_ll = list_from_array(vals), list_from_array(expected) 

            print("val = " + str(vals) + " rotate = " + str(rotate))
            actual = s.rotate_linked_list(vals_ll, rotate)
            compare_linked_lists(expected_ll, actual)

            # self.assertEqual(expected_list, actual)
