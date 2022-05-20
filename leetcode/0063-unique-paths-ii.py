# https://leetcode.com/submissions/detail/703621115/

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0

        n = len(grid)
        m = len(grid[0])

        grid[0][0] = -1
        for i in range(n):
            for j in range(m):
                if grid[i][j] < 0:
                    if i + 1 < n and grid[i + 1][j] < 1:
                        grid[i + 1][j] += grid[i][j]
                    if j + 1 < m and grid[i][j + 1] < 1:
                        grid[i][j + 1] += grid[i][j]

        return -grid[-1][-1]
