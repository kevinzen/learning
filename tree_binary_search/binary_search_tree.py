class Node:
    def __init__(self, key, value, left = None, right = None, parent = None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

class BinarySearchTree(object):

    def __init__(self, root_node):
        self.root = root_node

    # insertion of elements, deletion of elements, and lookup
    def insert(self, new_node) -> Node:

        x, y = self.root, None

        if not x: # no root new_node, make this new_node the root new_node and return
            self.root = new_node
            return new_node

        while x:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node

        return new_node

    def minimum(self):
        node = self.root
        while node.left:
            node = node.left
        return node

    def maximum(self):
        node = self.root
        while node.right:
            node = node.right
        return node

    def node_count(self, node = None):
        # 1. return?
        # 2. determine how to break down
        # 3. combine

        root, count = self.root, 0
        if not root or not node:
            return 0

        # this counts for one
        count = 1

        # add em up
        count = count + self.node_count(node.left)
        count = count + self.node_count(node.right)

        return count

    def delete(self, root, key):
        pass

    def search(self, key):
        node = self.root

        while node and node.key != key:
            if key < node.key:
                node = node.left
            else:
                node = node.right

        return node
