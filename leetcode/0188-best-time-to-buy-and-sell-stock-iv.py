# https://leetcode.com/submissions/detail/796417766/


class Solution:
    def max_profit(self, i, to_sell, k, prices, memo):
        if k == 0 or i == len(prices):
            return 0

        if (i, k, to_sell) in memo:
            return memo[(i, k, to_sell)]

        diff = prices[i] if to_sell else -prices[i]
        do_trans = diff + self.max_profit(i + 1, not to_sell, k - 1 if to_sell else k, prices, memo)
        no_trans = self.max_profit(i + 1, to_sell, k, prices, memo)

        memo[(i, k, to_sell)] = max(do_trans, no_trans)
        return memo[(i, k, to_sell)]

    def maxProfit(self, k: int, prices: List[int]) -> int:
        return self.max_profit(0, False, k, prices, {})
