from leetcode_tester import Tester
from src.binary_tree import TreeNode, null

from typing import Optional, List


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(map(self.maxDepth, (root.left, root.right))) + 1


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.maxDepth)

    test.addTest(
        TreeNode.from_list([3, 9, 20, null, null, 15, 7]), 3
    )
    test.addTest(
        TreeNode.from_list([1, null, 2]), 2
    )
    test.doTest()
