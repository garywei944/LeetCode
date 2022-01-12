from collections import deque

from leetcode_tester import Tester
from src.binary_tree import TreeNode, null

from typing import Optional, List


# # Reverse Approach, the tree is not immutable!
# class Solution:
#     def reverse(self, root):
#         if root is None:
#             return
#         root.left, root.right = root.right, root.left
#
#         self.reverse(root.left)
#         self.reverse(root.right)
#
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         self.reverse(root.right)
#
#         return self.equals(root.left, root.right)
#
#     def equals(self, a, b):
#         if a is None and b is None:
#             return True
#         if a is None or b is None:
#             return False
#         return (
#                 a.val == b.val and
#                 self.equals(a.left, b.left) and
#                 self.equals(a.right, b.right)
#         )


# Recursive Approach
class Solution:
    def is_mirror(self, a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if a.val != b.val:
            return False
        return (
                self.is_mirror(a.left, b.right) and
                self.is_mirror(a.right, b.left)
        )

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.is_mirror(root.left, root.right)


# # Iterative Approach
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         if root is None:
#             return True
#
#         q = deque()
#         q.append(root.left)
#         q.append(root.right)
#         while len(q) > 0:
#             a = q.popleft()
#             b = q.popleft()
#
#             if a is None and b is None:
#                 continue
#             if a is None or b is None:
#                 return False
#             if a.val != b.val:
#                 return False
#
#             q.append(a.left)
#             q.append(b.right)
#             q.append(a.right)
#             q.append(b.left)
#
#         return True


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.isSymmetric)

    test.addTest(
        TreeNode.from_list([1, 2, 2, 3, 4, 4, 3]), True
    )
    test.addTest(
        TreeNode.from_list([1, 2, 2, null, 3, null, 3]), False
    )
    test.doTest()
