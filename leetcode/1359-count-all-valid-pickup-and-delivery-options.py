# https://leetcode.com/submissions/detail/655434009/

class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10 ** 9 + 7

        def count_orders(p, d, memo={}):
            if (p, d) in memo:
                return memo[(p, d)]

            if p < 2 and d < 2:
                return 1

            choose_p = p * count_orders(p - 1, d, memo) if p > 0 else 0
            choose_d = (d - p) * count_orders(p, d - 1, memo) if d > p else 0

            memo[(p, d)] = (choose_p + choose_d) % mod
            return memo[(p, d)]

        return count_orders(n, n)
