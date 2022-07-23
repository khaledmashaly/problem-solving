# https://leetcode.com/submissions/detail/754579479/

from sortedcontainers import SortedList


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        right = SortedList()

        for i in reversed(range(n)):
            counts[i] = right.bisect_left(nums[i])
            right.add(nums[i])

        return counts
