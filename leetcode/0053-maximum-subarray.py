# https://leetcode.com/submissions/detail/788447394/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(1, n):
            nums[i] += nums[i - 1]

        s_min = 0
        ans = float('-inf')

        for s in nums:
            ans = max(s - s_min, ans)
            s_min = min(s, s_min)

        return ans
