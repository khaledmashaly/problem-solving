# https://leetcode.com/submissions/detail/789079800/

class Solution:
    def max_rob(self, nums, i, memo):
        if i >= len(nums):
            return 0

        if i in memo:
            return memo[i]

        rob_i = nums[i] + self.max_rob(nums, i + 2, memo)
        not_rob_i = self.max_rob(nums, i + 1, memo)

        memo[i] = max(rob_i, not_rob_i)

        return memo[i]

    def rob(self, nums: List[int]) -> int:
        return self.max_rob(nums, 0, {})
