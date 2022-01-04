from leetcode_tester import Tester

from typing import Optional, List

from collections import Counter


class Solution:
    # Sorted Approach, should be faster when s and t are not very long
    # O(n log n) time, O(1) space
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    # # Counter Approach, hash function is O(1) but actually do some computation
    # # O(n) time, O(1) space, b/c there are only 26 letters
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return Counter(s) == Counter(t)


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.isAnagram)

    test.addTest(
        "anagram", "nagaram", True
    )
    test.addTest(
        "rat", "car", False
    )
    test.doTest()
