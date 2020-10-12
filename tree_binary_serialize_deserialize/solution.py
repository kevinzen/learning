# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Codec:

    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""

        node_data = deque()

        def node_walk(node: TreeNode, par_val: str, last_turn: str):

            if node:
                path_to_here = par_val + last_turn + str(node.val)
                node_data.append(path_to_here)
                node_walk(node.left, str(node.val), 'L')
                # print("node = " + str(node.val) + ' last_turn = ' + last_turn + " node.val = " + str(node.val))
                node_walk(node.right, str(node.val), 'R')

        node_walk(root, '', 'ROOT')
        ret_val = '.'.join(node_data)

        return ret_val

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        # example
        # ROOT0.0L1.1L3.3L7.7L15.7R16.3R8.8L17.8R18.1R4.4L9.9L19.4R10.0R2.2L5.5L11.5R12.2R6.6L13.6R14
        # meaning: root val = 0, 0.left = 3, 3.left = 7, etc.
        # first parse to dict: { 0: ( {.right_val} , { left_val } ), 1: etc... }

        if data == "":
            return None

        val_dict = {}
        # First, parse into a deque of all elements, in order
        nodes = deque(x for x in data.split('.'))

        # process root node first, and remove from deque
        root_val = int(nodes.popleft()[len('ROOT'):])
        val_dict['ROOT'] = root_val
        val_dict[root_val] = TreeNode(root_val)

        # process remaining, non-root, nodes
        for node in nodes:
            if node.count('R'):
                key, val = int(node.split('R')[0]), int(node.split('R')[1])
                val_node = TreeNode(val)
                val_dict[key].right = val_node
            else:
                key, val = int(node.split('L')[0]), int(node.split('L')[1])
                val_node = TreeNode(val)
                val_dict[key].left = val_node

            val_dict[val] = val_node

        head = val_dict[val_dict['ROOT']]
        return head

    def build_tree_breadth_first(self, node_vals: []):

        if len(node_vals) == 0:
            return []

        count = len(node_vals)
        nodes = {}

        RIGHT = 1
        LEFT = 2
        def build_tree(parent_node_index, node_index, r_or_l):

            if node_index >= count or node_vals[node_index] is None:
                return

            node_val = int(node_vals[node_index])
            nodes[node_index] = TreeNode(node_val)

            if r_or_l == LEFT:
                nodes[parent_node_index].left = nodes[node_index]
            else:
                nodes[parent_node_index].right = nodes[node_index]

            build_tree(node_index, 2*node_index+1, LEFT)
            build_tree(node_index, 2*node_index+2, RIGHT)

        # first, capture the tree head
        head_val = int(node_vals[0])
        nodes[0] = TreeNode(head_val)
        build_tree(0,1,LEFT)
        build_tree(0,2,RIGHT)

        return nodes[0]

class CodecOrig:

    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""

        def node_count(node: TreeNode, direction: str) -> int:

            count = 0
            if node:
                count = count + node_count(node.left)
                count = count + 1
                count = count + node_count(node.right)
            return count

        count = node_count(root)

        node_queue = deque()
        used_node_queue = deque()

        node_queue.append(root)
        i, nodes_left = 0, count - 1
        while nodes_left > 0:

            cur_node = node_queue.popleft()

            if not cur_node:
                node_queue.append(None)
                node_queue.append(None)
            else:
                if cur_node.left:
                    node_queue.append(cur_node.left)
                    nodes_left = nodes_left - 1
                else:
                    node_queue.append(None)

                if cur_node.right:
                    node_queue.append(cur_node.right)
                    nodes_left = nodes_left - 1
                else:
                    node_queue.append(None)

            used_node_queue.append(cur_node)

        all_nodes = used_node_queue + node_queue

        # vals = [str(node.val) if node != None else '' for node in node_list]
        #vals = deque(str(node.val) if node != None else '' for node in all_nodes)

        ret_val = ".".join(str(node.val) if node != None else '' for node in all_nodes)

        return ret_val

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """

        if len(data) == 0:
            return []

        nodes = data.split('.')
        ret_val = self.build_tree_breadth_first(nodes)

        return ret_val

    def build_tree_breadth_first(self, node_vals: []):

        # Create a list of trees
        forest = [TreeNode(int(val)) if val not in [None,''] else None for val in node_vals]
        count = len(node_vals)
        num_nodes = ((count - 2 - count % 2) // 2) + 1

        for i in range(num_nodes):

            left_index  = 2 * i + 1
            right_index = 2 * i + 2

            if forest[i] != None:
                if left_index <= count - 1:
                    forest[i].left = forest[left_index]
                if right_index <= count-1:
                    forest[i].right = forest[right_index]

        return forest[0]  # node


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(node)
# ans = deser.deserialize(tree)
# return ans

