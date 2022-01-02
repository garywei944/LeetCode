from leetcode_tester import Tester

from typing import Optional, List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = True
        for i in range(len(digits)):
            if digits[-i - 1] == 9:
                digits[-i - 1] = 0
            else:
                flag = False
                digits[-i - 1] += 1
                break
        if flag:
            digits.insert(0, 1)

        return digits


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.plusOne)

    test.addTest(
        [1, 2, 3], [1, 2, 4]
    )
    test.addTest(
        [4, 3, 2, 1], [4, 3, 2, 2]
    )
    test.addTest(
        [9], [1, 0]
    )
    test.doTest()
