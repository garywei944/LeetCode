from leetcode_tester import Tester

from typing import Optional, List


class Solution:
    # # sorted takes O(n log n) time, we need O(n) time and O(1) space
    # def singleNumber(self, nums: List[int]) -> int:
    #     s = sorted(nums)
    #     for i in range(len(s) // 2):
    #         if s[i * 2] != s[i * 2 + 1]:
    #             return s[i * 2]
    #     return s[-1]

    # XOR solution
    def singleNumber(self, nums: List[int]) -> int:
        r = 0
        for n in nums:
            r ^= n
        return r


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.singleNumber)

    test.addTest(
        [4, 1, 2, 1, 2], 4
    )
    test.doTest()
