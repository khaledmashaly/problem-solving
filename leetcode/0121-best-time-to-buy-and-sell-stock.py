# https://leetcode.com/submissions/detail/673929853/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p_min = prices[0]
        profit = 0
        for p in prices:
            if p < p_min:
                p_min = p
                continue

            profit = max(p - p_min, profit)

        return max(profit, 0)
