# https://leetcode.com/submissions/detail/678670898/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r = len(board)
        c = len(board[0])

        def get_neighbours(x, y):
            neighbours = list()

            for i in (x - 1, x, x + 1):
                for j in (y - 1, y, y + 1):
                    if 0 <= i <= r - 1 and 0 <= j <= c - 1 and (i != x or j != y):
                        neighbours.append(board[i][j])

            return neighbours

        cells_to_toggle = list()

        for i in range(r):
            for j in range(c):
                neighbours = get_neighbours(i, j)
                live_neighbours = sum(neighbours)
                if board[i][j]:
                    if live_neighbours < 2 or live_neighbours > 3:
                        cells_to_toggle.append((i, j))
                elif live_neighbours == 3:
                    cells_to_toggle.append((i, j))

        for i, j in cells_to_toggle:
            board[i][j] = 1 - board[i][j]
