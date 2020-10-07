
import unittest

from tree_binary_insert.solution import Solution, TreeNode


class BinaryTreeInsertTest(unittest.TestCase):

    def test_solution(self):

        s = Solution()

        tests = [
            ([4, 2, 7, 1, 3], 5, [4, 2, 7, 1, 3, 5]),
            ([40, 20, 60, 10, 30, 50, 70], 25, [40, 20, 60, 10, 30, 50, 70, None, None, 25]),
            ( [4, 2, 7, 1, 3, None, None, None, None, None, None], 5, [4, 2, 7, 1, 3, 5])
        ]

        for test in tests:
            vals   = test[0]
            insert_val = test[1]
            expected = test[2]

            print("vals = " + str(vals) + " expected_list = " + str(expected))

            tree = s.build_binary_tree(vals)
            expected_tree = s.build_binary_tree(expected)

            actual = s.insertIntoBST(tree, insert_val)
            # s.print_tree(tree)
            # s.print_tree(expected_tree)
            actual_as_list = s.tree_to_list(actual)
            print("vals = " + str(vals) + " expected_list = " + str(expected) + " actual = " + str(actual_as_list))

            # self.assertEqual(expected_list, actual)
