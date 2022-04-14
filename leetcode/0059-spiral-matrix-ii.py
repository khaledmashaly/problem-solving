# https://leetcode.com/submissions/detail/679890595/

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        i = 0
        j = n - 1
        current = 1
        while i < j:
            # fill top row
            for x in range(i, j):
                matrix[i][x] = current
                current += 1
            # fill right column
            for x in range(i, j):
                matrix[x][j] = current
                current += 1
            # fill bottom row
            for x in reversed(range(i + 1, j + 1)):
                matrix[j][x] = current
                current += 1
            # fill left column
            for x in reversed(range(i + 1, j + 1)):
                matrix[x][i] = current
                current += 1
            i += 1
            j -= 1

        if n % 2 == 1:
            matrix[i][j] = current

        return matrix
