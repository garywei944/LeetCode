from leetcode_tester import Tester

from typing import Optional, List

MAX = 2 ** 31


class Solution:
    def reverse(self, x: int) -> int:
        if x > MAX - 1 or x < -MAX:
            return 0

        sign = x < 0
        x = abs(x)
        r = 0
        while x > 0:
            t = x % 10
            x //= 10
            r *= 10
            r += t

        if sign:
            r = -r

        # May not work for language like C++ that behave a different way when
        # int overflow the maximum.
        if r > MAX - 1 or r < -MAX:
            return 0
        return r


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.reverse)

    test.addTest(
        123, 321
    )
    test.addTest(
        -123, -321
    )
    test.addTest(
        1534236469,
        0
    )
    test.doTest()
