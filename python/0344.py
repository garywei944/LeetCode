from leetcode_tester import Tester

from typing import Optional, List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n // 2):
            s[i], s[-i - 1] = s[-i - 1], s[i]

        return s


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.reverseString)

    test.addTest(
        ["h", "e", "l", "l", "o"],
        ["o", "l", "l", "e", "h"]
    )
    test.addTest(
        ["H", "a", "n", "n", "a", "h"],
        ["h", "a", "n", "n", "a", "H"]
    )
    test.doTest()
