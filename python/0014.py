from leetcode_tester import Tester

from typing import Optional, List


# Vertical compare approach: compare each character from the first one and
# return immediate when
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)

        for i, ch in enumerate(shortest):
            if not all([s[i] == ch for s in strs]):
                return shortest[:i]
        return shortest


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.longestCommonPrefix)

    test.addTest(
        ["flower", "flow", "flight"], 'fl'
    )
    test.addTest(
        ["dog", "racecar", "car"], ''
    )
    test.addTest(
        [""], ''
    )
    test.addTest(
        ["a"], 'a'
    )
    test.doTest()
