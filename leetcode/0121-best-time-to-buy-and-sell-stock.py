# https://leetcode.com/submissions/detail/673929853/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < prices[buy]:
                buy = i
                sell = i
            if prices[i] > prices[sell]:
                sell = i
                profit = max(profit, prices[sell] - prices[buy])

        return profit
