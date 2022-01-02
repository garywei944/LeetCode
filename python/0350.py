from collections import Counter

from leetcode_tester import Tester

from typing import Optional, List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)

        r = []
        for n in nums2:
            if count1[n] > 0:
                r.append(n)
                count1[n] -= 1
        # return r
        return sorted(r)  # Sort r for test locally, not necessary


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.intersect)

    test.addTest(
        [1, 2, 2, 1], [2, 2],
        [2, 2]
    )
    test.addTest(
        [4, 9, 5], [9, 4, 9, 8, 4],
        [4, 9]
    )
    test.doTest()
