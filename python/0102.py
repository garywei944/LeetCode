from leetcode_tester import Tester
from src.binary_tree import TreeNode, null
from collections import deque

from typing import Optional, List


# Iterative Approach
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        r = []
        q = deque()
        q.append(root)

        while len(q) > 0:
            l_ = len(q)
            level = []
            for _ in range(l_):
                t = q.popleft()
                if t is not None:
                    level.append(t.val)
                    if t.left is not None:
                        q.append(t.left)
                    if t.right is not None:
                        q.append(t.right)
            r.append(level)
        return r


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.levelOrder)

    test.addTest(
        TreeNode.from_list([3, 9, 20, null, null, 15, 7]),
        [[3], [9, 20], [15, 7]]
    )
    test.addTest(
        TreeNode.from_list([1]),
        [[1]]
    )
    test.addTest(
        TreeNode.from_list([]),
        []
    )
    test.doTest()
