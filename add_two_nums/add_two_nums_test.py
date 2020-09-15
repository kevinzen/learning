import unittest

from sort_insertion.solution import Solution, ListNode


class LinkedListTest(unittest.TestCase):

    def test_new_linked_list(self):
        l1_1 = ListNode(3)
        l1_2 = ListNode(4, next=l1_1)
        l1_3 = ListNode(2, next=l1_2)

        l2_1 = ListNode(4)
        l2_2 = ListNode(6, next=l2_1)
        l2_3 = ListNode(5, next=l2_2)

        s = Solution()
        result = s.addTwoNumbers(l1_3, l2_3)

        while result:
            print(result.val)
            result = result.next

        # self.assertTrue(ll.delete(1))
        # self.assertEqual(1, ll.size())
        # self.assertTrue(ll.delete(2))
        # self.assertEqual(0, ll.size())
        # self.assertFalse(ll.delete(3))
