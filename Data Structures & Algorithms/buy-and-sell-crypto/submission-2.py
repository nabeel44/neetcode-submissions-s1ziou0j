class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) < 2:
            return profit
        minPrice = prices[0]
        for price in prices:
            profit = max(profit, price - minPrice)
            minPrice = min(minPrice, price)
        return profit

        