
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        if not root:
            return TreeNode(val=val)

        cur_node = root
        end_node = None

        while(cur_node):
            end_node = cur_node
            if val < cur_node.val:
                cur_node = cur_node.left
            elif val > cur_node.val:
                cur_node = cur_node.right

        # at terminal node. SHould it go right or left side?
        if val < end_node.val:
            end_node.left = TreeNode(val=val)
        else:
            end_node.right = TreeNode(val=val)

        return root

    def build_binary_tree(self, values: []) -> TreeNode:
        root = TreeNode(values[0])

        for i in range(1, len(values)):
            if values[i]:
                self.insertIntoBST(root, values[i])

        return root

    def print_tree(self, node : TreeNode):

        if node :
            self.print_tree(node.left)
            print("val = " + str(node.val))
            self.print_tree(node.right)

    def tree_to_list(self, node : TreeNode):

        if not node :
            return []

        ret_val = [node.val]
        ret_val = ret_val + self.tree_to_list(node.left)
        ret_val = ret_val + self.tree_to_list(node.right)

        return ret_val
