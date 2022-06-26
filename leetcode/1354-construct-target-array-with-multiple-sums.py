# https://leetcode.com/submissions/detail/732086636/

from heapq import heappush, heappop


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        n = len(target)

        if n == 1:
            return target[0] == 1

        heap = []
        s = 0
        for i in target:
            heappush(heap, -i)
            s += i

        while heap[0] != -1:
            cur = -heappop(heap)
            if s - cur == 1:
                return True 

            s -= cur
            x = cur % s

            if x == 0 or x == cur:
                return False

            heappush(heap, -x)
            s += x

        return True
