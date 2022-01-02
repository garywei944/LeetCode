from leetcode_tester import Tester

from typing import Optional, List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                r += prices[i] - prices[i - 1]
        return r


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.maxProfit)

    test.addTest(
        [7, 1, 5, 3, 6, 4], 7
    )
    test.addTest(
        [1, 2, 3, 4, 5], 4
    )
    test.addTest(
        [7, 6, 4, 3, 1], 0
    )
    test.doTest()
