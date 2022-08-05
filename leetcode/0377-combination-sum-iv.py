# https://leetcode.com/submissions/detail/765890404/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        tab = [0] * (target + 1)
        tab[0] = 1

        for i in range(0, target + 1):
            for num in nums:
                if i + num < target + 1:
                    tab[i + num] += tab[i]

        return tab[target]
