# https://leetcode.com/submissions/detail/748061411/

from collections import deque


class Solution:
    def can_extend(self, i, j):
        if not (0 <= i < self.r) or not (0 <= j < self.c):
            return False

        if self.grid[i][j] == 1:
            return True

        return False

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.r = len(grid)
        self.c = len(grid[0])

        max_area = 0

        for i in range(self.r):
            for j in range(self.c):
                if self.grid[i][j] == 1:
                    self.grid[i][j] = -1
                    q = deque([(i, j)])
                    current_area = 1
                    while len(q) > 0:
                        ci, cj = q.popleft()

                        if self.can_extend(ci, cj - 1):
                            q.append((ci, cj - 1))
                            self.grid[ci][cj - 1] = -1
                            current_area += 1

                        if self.can_extend(ci, cj + 1):
                            q.append((ci, cj + 1))
                            self.grid[ci][cj + 1] = -1
                            current_area += 1

                        if self.can_extend(ci + 1, cj):
                            q.append((ci + 1, cj))
                            self.grid[ci + 1][cj] = -1
                            current_area += 1

                        if self.can_extend(ci - 1, cj):
                            q.append((ci - 1, cj))
                            self.grid[ci - 1][cj] = -1
                            current_area += 1
                    max_area = max(max_area, current_area)

        return max_area
