# https://leetcode.com/submissions/detail/695066761/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)

        if n < 3:
            return False

        s = []
        three = float('-inf')
        for i in reversed(range(n)):
            if nums[i] < three:
                return True

            while len(s) > 0 and nums[i] > s[-1]:
                three = s.pop()

            s.append(nums[i])

        return False
