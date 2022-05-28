# https://leetcode.com/submissions/detail/709160257/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = n * (n + 1) // 2
        return s - sum(nums)
