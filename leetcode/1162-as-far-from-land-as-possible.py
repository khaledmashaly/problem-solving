# https://leetcode.com/problems/as-far-from-land-as-possible/submissions/895978423/

class Solution:
    def maxDistance(self, grid):
        r = len(grid)
        c = len(grid[0])

        tab = [[201] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    d_left = 201
                    if j > 0:
                        if grid[i][j - 1] == 1:
                            d_left = 0
                        else:
                            d_left = tab[i][j - 1]

                    d_top = 201
                    if i > 0:
                        if grid[i - 1][j] == 1:
                            d_top = 0
                        else:
                            d_top = tab[i - 1][j]

                    tab[i][j] = min(tab[i][j], d_left + 1, d_top + 1)

        ans = -1
        for i in reversed(range(r)):
            for j in reversed(range(c)):
                if grid[i][j] == 0:
                    d_right = 201
                    if j < c - 1:
                        if grid[i][j + 1] == 1:
                            d_right = 0
                        else:
                            d_right = tab[i][j + 1]

                    d_bottom = 201
                    if i < r - 1:
                        if grid[i + 1][j] == 1:
                            d_bottom = 0
                        else:
                            d_bottom = tab[i + 1][j]

                    tab[i][j] = min(tab[i][j], d_right + 1, d_bottom + 1)
                    ans = max(ans, tab[i][j])

        return -1 if ans == 201 else ans
