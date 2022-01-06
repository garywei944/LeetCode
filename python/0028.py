from leetcode_tester import Tester

from typing import Optional, List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0

        n = len(needle)

        for i in range(len(haystack) - n + 1):
            s = haystack[i:i + n]
            if s == needle:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.strStr)

    test.addTest(
        "hello", "ll", 2
    )
    test.addTest(
        "aaaaa", "bba", -1
    )
    test.addTest(
        "", "", 0
    )
    test.doTest()
