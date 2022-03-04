# https://leetcode.com/submissions/detail/652739314/gs

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 3:
            return 0

        count = 2
        diff = nums[1] - nums[0]
        ans = 0

        for i in range(2, n):
            if nums[i] - nums[i - 1] == diff:
                count += 1
                if count > 2:
                    ans += count - 2
            else:
                count = 2
                diff = nums[i] - nums[i - 1]

        return ans
