from leetcode_tester import Tester

from typing import Optional, List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        m = (n - k) % n
        nums[:m] = nums[:m][::-1]
        nums[m:] = nums[m:][::-1]
        nums.reverse()

        return nums


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.rotate)

    test.addTest(
        [1, 2, 3, 4, 5, 6, 7], 3,
        [5, 6, 7, 1, 2, 3, 4]
    )
    test.doTest()
