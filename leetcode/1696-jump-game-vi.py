# https://leetcode.com/submissions/detail/743778056/

from heapq import heappop, heappush


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        scores = [(-nums[0], 0)]

        ans = nums[0]
        for i in range(1, len(nums)):
            s_max, i_max = scores[0]

            while i_max < i - k:
                heappop(scores)
                s_max, i_max = scores[0]

            ans = -s_max + nums[i]
            heappush(scores, (-ans, i))

        return ans
