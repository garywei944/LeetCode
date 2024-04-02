from itertools import pairwise, chain


class Solution:
    """
    https://leetcode.com/problems/decode-ways-ii/solutions/4461853/python-short-and-clean
    """

    def numDecodings(self, s: str) -> int:
        M = int(1e9 + 7)
        a, b = 0, 1

        for c2, c1 in pairwise(chain("0", s)):
            p = q = 0

            # consist the last 2 characters
            match c2, c1:
                case "1", "*":
                    p = 9
                case "2", "*":
                    p = 6
                case "*", "*":
                    p = 15
                case "1", _:
                    p = 1
                case "2", x:
                    p = 1 if x <= "6" else 0
                case "*", x:
                    p = 2 if x <= "6" else 1

            # consist the last 1 character
            match c1:
                case "*":
                    q = 9
                case "0":
                    q = 0
                case _:
                    q = 1

            a, b = b, (a * p + b * q) % M

        return b
