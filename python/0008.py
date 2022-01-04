from leetcode_tester import Tester

from typing import Optional, List
import re

MAX = 1 << 31


class Solution:
    def myAtoi(self, s: str) -> int:
        g = re.match(r'^\s*([+-]?\d+).*$', s)
        if g is not None:
            s = g.group(1)
            if s != '':
                r = int(s)

                return max(min(r, MAX - 1), -MAX)
        return 0


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.myAtoi)

    test.addTest(
        '42', 42
    )
    test.addTest(
        '   -42', -42
    )
    test.addTest(
        '4193 with words', 4193
    )
    test.addTest(
        "words and 987", 0
    )
    test.addTest(
        "-91283472332", -2147483648
    )
    test.addTest(
        "+-12", 0
    )
    test.doTest()

    print(solution.myAtoi('+-12'))
