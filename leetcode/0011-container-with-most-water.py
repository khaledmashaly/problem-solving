# https://leetcode.com/submissions/detail/795611244/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        a_max = 0
        while j > i:
            w = j - i
            h = min(height[j], height[i])
            a_max = max(a_max, w * h)

            if height[j] <= height[i]:
                j -= 1
            else:
                i += 1

        return a_max
