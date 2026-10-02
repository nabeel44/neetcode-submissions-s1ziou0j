class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) < 2:
            return profit
        l, r = 0, 1
        while l < len(prices) - 1 and r < len(prices):
            if prices[l] >= prices[r]:
                if r - l == 1:
                    r += 1
                l += 1
            else:
                profit = max(profit, prices[r] - prices[l])
                r += 1
        return profit


        