from leetcode_tester import Tester
from src.binary_tree import TreeNode, null

from typing import Optional, List


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)

        if n == 0:
            return None

        mid = n // 2
        return TreeNode(
            nums[mid],
            self.sortedArrayToBST(nums[:mid]),
            self.sortedArrayToBST(nums[mid + 1:])
        )


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.sortedArrayToBST)

    test.addTest(
        [-10, -3, 0, 5, 9],
        TreeNode.from_list([0, -3, 9, -10, null, 5])
    )
    test.addTest(
        [1, 3],
        TreeNode.from_list([3, 1])
    )
    test.doTest()
