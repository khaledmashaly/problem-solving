# https://leetcode.com/submissions/detail/748791911/


class Solution:
    def count_paths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int, memo) -> int:
        if not (0 <= startRow < m) or not (0 <= startColumn < n):
            return 1

        if maxMove < 1:
            return 0

        if (startRow, startColumn, maxMove) in memo:
            return memo[(startRow, startColumn, maxMove)]

        paths = 0
        for i, j in ((startRow, startColumn - 1), (startRow, startColumn + 1), (startRow - 1, startColumn), (startRow + 1, startColumn)):
            paths += self.count_paths(m, n, maxMove - 1, i, j, memo) % (1e9 + 7)

        memo[(startRow, startColumn, maxMove)] = paths % (1e9 + 7)

        return memo[(startRow, startColumn, maxMove)]


    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        return self.count_paths(m, n, maxMove, startRow, startColumn, {})
