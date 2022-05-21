# https://leetcode.com/submissions/detail/704186821/

from math import inf


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        tab = [inf for _ in range(amount + 1)]

        for c in coins:
            if c < amount + 1:
                tab[c] = 1

        for i in range(amount + 1):
            if tab[i] != -1:
                for c in coins:
                    if i + c < amount + 1:
                        tab[i + c] = min(tab[i + c], tab[i] + 1)

        return tab[-1] if tab[-1] is not inf else -1
