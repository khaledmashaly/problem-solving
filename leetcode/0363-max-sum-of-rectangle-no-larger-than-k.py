# https://leetcode.com/submissions/detail/794190979/


from bisect import bisect_left, insort_left


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            for j in range(1, c):
                matrix[i][j] += matrix[i][j - 1]

        s_max = float('-inf')

        for c_start in range(c):
            for c_end in range(c_start, c):
                temp = [0]
                s_cur = 0

                for i in range(r):
                    start = 0 if c_start == 0 else matrix[i][c_start - 1]
                    end = matrix[i][c_end]
                    s_cur += end - start

                    d = s_cur - k
                    j = bisect_left(temp, d)
                    if j != len(temp):
                        if temp[j] == d:
                            return k
                        s_max = max(s_max, s_cur - temp[j])

                    insort_left(temp, s_cur)

        return s_max
