# https://leetcode.com/submissions/detail/719837627/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        s = sum(nums)
        target = s - x

        if target < 0:
            return -1

        if target == 0:
            return n

        for i in range(1, n):
            nums[i] += nums[i - 1]

        sums = {0: -1}
        ans = -1
        for i in range(n):
            if nums[i] - target in sums:
                ans = max(ans, i - sums[nums[i] - target])
            if nums[i] not in sums:
                sums[nums[i]] = i

        return n - ans if ans != -1 else -1
