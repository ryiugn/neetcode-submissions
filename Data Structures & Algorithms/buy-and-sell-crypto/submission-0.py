class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyprice = 9999
        profit = 0
        for n in range(len(prices)):
            buyprice = min(buyprice, prices[n])
            current = prices[n] - buyprice
            profit = max(current, profit)
        return profit