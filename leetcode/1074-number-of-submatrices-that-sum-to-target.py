# https://leetcode.com/submissions/detail/719164157/

from collections import defaultdict


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            for j in range(1, c):
                matrix[i][j] += matrix[i][j - 1]

        ans = 0
        for start in range(c):
            for end in range(start, c):
                d = defaultdict(int)
                d[0] = 1
                s = 0
                for i in range(r):
                    cur = matrix[i][end] if start == 0 else matrix[i][end] - matrix[i][start - 1]
                    s += cur
                    ans += d[s - target]
                    d[s] += 1

        return ans
