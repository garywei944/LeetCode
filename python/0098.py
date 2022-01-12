from leetcode_tester import Tester
from src.binary_tree import TreeNode, null

from typing import Optional, List

MAX = float('inf')


class Solution:
    def check_bound(self, node, max_=MAX, min_=-MAX):
        if node is None:
            return True

        if node.val >= max_ or node.val <= min_:
            return False

        return (
                self.check_bound(node.left, node.val, min_) and
                self.check_bound(node.right, max_, node.val)
        )

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check_bound(root)


# # In-order approach
# # A BST is valid iff it's in-order traversal is ascending.
# class Solution:
#     def __init__(self):
#         self.upper = None
#
#     def inorder(self, node):
#         if node is None:
#             return True
#
#         if not self.inorder(node.left):
#             return False
#         if node.val <= self.upper:
#             return False
#         self.upper = node.val
#         return self.inorder(node.right)
#
#     def isValidBST(self, node: Optional[TreeNode]) -> bool:
#         self.upper = -MAX
#         return self.inorder(node)


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.isValidBST)

    test.addTest(
        TreeNode.from_list([2, 1, 3]), True
    )
    test.addTest(
        TreeNode.from_list([5, 1, 4, null, null, 3, 6]), False
    )
    test.doTest()
