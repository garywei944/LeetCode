from leetcode_tester import Tester
import itertools

from typing import Optional, List


# Recursive Approach, most intuitive
class Solution:
    def countAndSay(self, n):
        if n == 1:
            return '1'

        s = self.countAndSay(n - 1)
        r = ''
        c = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                c += 1
            else:
                r += str(c) + s[i - 1]
                c = 1

        return r + str(c) + s[-1]


# # itertools groupby Approach, takes advantage of python builtin packages
# class Solution:
#     def countAndSay(self, n: int) -> str:
#         s = '1'
#         for _ in range(n - 1):
#             s = ''.join(f'{len(list(g))}{k}' for k, g in itertools.groupby(s))
#         return s


# # Loop Approach, theoretically same with the recursive approach, except we do
# # it in a for loop.
# class Solution:
#     def countAndSay(self, n: int) -> str:
#         if n == 1:
#             return '1'
#         elif n == 2:
#             return '11'
#
#         s = '11'
#         for _ in range(n - 2):
#             s += '$'
#
#             t = ''
#             c = 1
#             for i in range(1, len(s)):
#                 if s[i] != s[i - 1]:
#                     t += f'{c}{s[i - 1]}'
#                     c = 1
#                 else:
#                     c += 1
#             s = t
#         return s


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.countAndSay)

    test.addTest(
        1, '1'
    )
    test.addTest(
        4, '1211'
    )
    test.addTest(
        6, '312211'
    )
    test.doTest()

    # print(solution.countAndSay(6))
