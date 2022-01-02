class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        r = 0
        for i in range(n - 1):
            if prices[i] < prices[i + 1]:
                r += prices[i + 1] - prices[i]
        return r
