from leetcode_tester import Tester

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            if n in d:
                return [d[n], i]
            d[target - n] = i


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.twoSum)

    test.addTest(
        [2, 7, 11, 15], 9,
        [0, 1]
    )
    test.addTest(
        [3, 2, 4], 6,
        [1, 2]
    )
    test.addTest(
        [3, 3], 6,
        [0, 1]
    )
    test.doTest()
