from leetcode_tester import Tester

from typing import Optional, List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k, curr = 0, -101
        for n in nums:
            if n > curr:
                curr = n
                nums[k] = n
                k += 1
        return k


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.removeDuplicates)

    test.addTest(
        [1, 1, 2], 2
    )
    test.addTest(
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5
    )
    test.doTest()
