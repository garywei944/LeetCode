from leetcode_tester import Tester

from typing import Optional, List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0

        for i, n in enumerate(nums):
            if n != 0:
                nums[idx] = n
                idx += 1

        for i in range(idx, len(nums)):
            nums[i] = 0

        return nums


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.moveZeroes)

    test.addTest(
        [0, 1, 0, 3, 12],
        [1, 3, 12, 0, 0]
    )
    test.addTest(
        [0],
        [0]
    )

    test.doTest()
