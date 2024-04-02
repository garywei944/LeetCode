import numpy as np


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = np.zeros(128, dtype=int)
        best = 0
        start = 0

        for end, c in enumerate(s):
            e = ord(c)
            start = max(start, pos[e])
            best = max(best, end - start + 1)
            pos[e] = end + 1

        return best
