# https://leetcode.com/submissions/detail/787501829/

class Solution:
    def climbStairs(self, n: int) -> int:
        x = 0
        y = 1

        for i in range(n):
            z = y + x
            x = y
            y = z

        return y
