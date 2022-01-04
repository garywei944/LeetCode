from leetcode_tester import Tester

from typing import Optional, List
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)

        for i, c in enumerate(s):
            if counter[c] == 1:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.firstUniqChar)

    test.addTest(
        "leetcode", 0
    )
    test.addTest(
        "loveleetcode", 2
    )
    test.addTest(
        "aabb", -1
    )
    test.doTest()
