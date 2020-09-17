import unittest

from tree_binary_search.binary_search_tree import BinarySearchTree, Node


class BinarySearchTest(unittest.TestCase):

    def test_bst_init(self):
        node = Node(10, '10')
        bst = BinarySearchTree(node)

        root = bst.root
        self.assertIsNotNone(root)
        self.assertEqual(10, root.key)
        self.assertEqual(1,bst.node_count(bst.root))

    def test_bst_insert(self):

        root = Node(5, '5')
        bst = BinarySearchTree(root)

        nodes = [
            Node(1, '1'),
            Node(3, '3'),
            Node(2, '2'),
            Node(10, '10'),
            Node(4, '4'),
            Node(6, '6')
        ]

        for new_node in nodes:
            bst.insert(new_node)
            n = bst.search(new_node.key)
            self.assertEqual(new_node.key, n.key)
            self.assertEqual(new_node.value, n.value)
        self.assertEqual(7,bst.node_count(bst.root))

    def test_bst_minimum(self):

        root = Node(5, '5')
        bst = BinarySearchTree(root)

        nodes = [
            (Node(3, '3'),3),
            (Node(2, '2'),2),
            (Node(10, '10'),2),
            (Node(1, '1'),1),
            (Node(4, '4'),1),
            (Node(6, '6'),1)
        ]

        for pair in nodes:
            new_node   = pair[0]
            minimum_key = pair[1]
            bst.insert(new_node)
            n = bst.minimum()
            self.assertEqual(minimum_key, n.key)

    def test_bst_maximum(self):

        root = Node(5, '5')
        bst = BinarySearchTree(root)

        nodes = [
            (Node(3, '3'),5),
            (Node(2, '2'),5),
            (Node(6, '6'),6),
            (Node(1, '1'),6),
            (Node(10, '10'),10),
            (Node(4, '4'),10),
        ]

        for pair in nodes:
            new_node   = pair[0]
            maximum_key = pair[1]
            bst.insert(new_node)
            n = bst.maximum()
            self.assertEqual(maximum_key, n.key)

        self.assertEqual(bst.node_count(bst.root), 7)

    def test_count(self):

        root = Node(5, '5')
        bst = BinarySearchTree(root)
        self.assertEqual(1,bst.node_count(bst.root))

        nodes = [
            (Node(3, '3'),2),
            (Node(2, '2'),3),
            (Node(6, '6'),4),
            (Node(1, '1'),5),
            (Node(10, '10'),6),
            (Node(4, '4'),7)
        ]

        for pair in nodes:
            new_node   = pair[0]
            node_count   = pair[1]
            bst.insert(new_node)
            n = bst.node_count(bst.root)
            self.assertEqual(node_count, n)

    def test_in_order_tree_walk(self):

        root = Node(5, '5')
        bst = BinarySearchTree(root)

        nodes = [
            (Node(3, '3'),5),
            (Node(2, '2'),5),
            (Node(6, '6'),6),
            (Node(1, '1'),6),
            (Node(10, '10'),10),
            (Node(4, '4'),10),
        ]

        for pair in nodes:
            new_node   = pair[0]
            maximum_key = pair[1]
            bst.insert(new_node)
            n = bst.maximum()
            self.assertEqual(maximum_key, n.key)

        self.assertEqual(bst.node_count(bst.root), 7)

        bst.in_order_tree_walk(bst.root)

    def test_successor(self):

        root = Node(5, '5')
        bst = BinarySearchTree(root)

        nodes = [
            (Node(3, '3'),5),
            (Node(2, '2'),5),
            (Node(10, '10'),10),
            (Node(1, '1'),10),
            (Node(6, '6'),10),
            (Node(8, '8'),10),
            (Node(4, '4'),10),
        ]

        for pair in nodes:
            new_node   = pair[0]
            maximum_key = pair[1]
            bst.insert(new_node)
            n = bst.maximum()
            self.assertEqual(maximum_key, n.key)

        node = bst.search(1)
        successor = bst.successor_node(node)
        self.assertEqual('2',successor.value)

        node = bst.search(2)
        successor = bst.successor_node(node)
        self.assertEqual('3',successor.value)

        node = bst.search(3)
        successor = bst.successor_node(node)
        self.assertEqual('4', successor.value)

        node = bst.search(3)
        successor = bst.successor_node(node)
        self.assertEqual('4', successor.value)

        node = bst.search(4)
        successor = bst.successor_node(node)
        self.assertEqual('5', successor.value)

        node = bst.search(5)
        successor = bst.successor_node(node)
        self.assertEqual('6', successor.value)

        node = bst.search(6)
        successor = bst.successor_node(node)
        self.assertEqual('8',successor.value)

        node = bst.search(8)
        successor = bst.successor_node(node)
        self.assertEqual('10',successor.value)

        node = bst.search(10)
        successor = bst.successor_node(node)
        self.assertIsNone(successor)

        self.assertEqual(bst.node_count(bst.root), 8)


    def test_predecessor(self):

        root = Node(5, '5')
        bst = BinarySearchTree(root)

        nodes = [
            (Node(3, '3'),5),
            (Node(2, '2'),5),
            (Node(10, '10'),10),
            (Node(1, '1'),10),
            (Node(6, '6'),10),
            (Node(8, '8'),10),
            (Node(4, '4'),10),
        ]

        for pair in nodes:
            new_node   = pair[0]
            maximum_key = pair[1]
            bst.insert(new_node)
            n = bst.maximum()
            self.assertEqual(maximum_key, n.key)

        node = bst.search(1)
        predecessor = bst.predecessor_node(node)
        self.assertEqual(None,predecessor)

        node = bst.search(2)
        predecessor = bst.predecessor_node(node)
        self.assertEqual('1',predecessor.value)

        node = bst.search(3)
        predecessor = bst.predecessor_node(node)
        self.assertEqual('2', predecessor.value)

        node = bst.search(3)
        predecessor = bst.predecessor_node(node)
        self.assertEqual('2', predecessor.value)

        node = bst.search(4)
        predecessor = bst.predecessor_node(node)
        self.assertEqual('3', predecessor.value)

        node = bst.search(5)
        predecessor = bst.predecessor_node(node)
        self.assertEqual('4', predecessor.value)

        node = bst.search(6)
        predecessor = bst.predecessor_node(node)
        self.assertEqual('5',predecessor.value)

        node = bst.search(8)
        predecessor = bst.predecessor_node(node)
        self.assertEqual('6',predecessor.value)

        node = bst.search(10)
        predecessor = bst.predecessor_node(node)
        self.assertEqual('8',predecessor.value)

        self.assertEqual(bst.node_count(bst.root), 8)


