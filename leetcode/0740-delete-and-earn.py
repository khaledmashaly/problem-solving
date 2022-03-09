# https://leetcode.com/submissions/detail/656794796/

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        scores = {}

        for num in nums:
            scores[num] = scores[num] + num if num in scores else num

        n = max(nums)
        tab = [0] * (n + 1)

        for i in range(1, n + 1):
            take = scores[i] if i in scores else 0
            if i - 2 > 0:
                take += tab[i - 2]
            not_take = tab[i - 1]
            tab[i] = max(take, not_take)

        return tab[n]
