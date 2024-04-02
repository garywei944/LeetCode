class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            "0": 0,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        r = p = 0
        for c in s:
            e1, e2 = p, map[c]

            if e1 < e2:
                r -= e1
            else:
                r += e1
            p = e2

        return r + p
