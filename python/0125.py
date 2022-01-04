from leetcode_tester import Tester
import re

from typing import Optional, List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[\W_]+', '', s).lower()

        return s == s[::-1]


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.isPalindrome)

    test.addTest(
        "A man, a plan, a canal: Panama", True
    )
    test.addTest(
        "race a car", False
    )
    test.addTest(
        " ", True
    )
    test.addTest(
        "ab_a", True
    )
    test.doTest()
