import unittest

class LinkedListTest(unittest.TestCase):

    def test_new_linked_list(self):
        ll = LinkedList()
        self.assertIsNone(ll.head)
        self.assertEqual(0,ll.size())

    def test_add_first_element(self):
        ll = LinkedList()
        ll.add(5)
        self.assertEqual(1,ll.size())

        n = ll.head
        self.assertEqual(5, n.data)
        self.assertIsNone(n.next)

    def test_add_2_elements(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        self.assertEqual(2,ll.size())

        n = ll.head
        self.assertIsNotNone(n.next)
        self.assertEqual(2,n.data)

        n = n.next
        self.assertIsNone(n.next)
        self.assertEqual(1,n.data)

    def test_search(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        self.assertEqual(2,ll.size())

        self.assertTrue(ll.search(1))
        self.assertTrue(ll.search(2))
        self.assertFalse(ll.search(3))


    def test_delete(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        self.assertEqual(2,ll.size())

        self.assertTrue(ll.delete(1))
        self.assertEqual(1, ll.size())
        self.assertTrue(ll.delete(2))
        self.assertEqual(0, ll.size())
        self.assertFalse(ll.delete(3))
