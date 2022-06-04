# https://leetcode.com/submissions/detail/714418084/

class Solution:
    def __init__(self):
        self.solutions = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        def can_extend(sol, n):
            l = len(sol)
            for i in range(l):
                if n == sol[i]:
                    return False
                if abs(n - sol[i]) == l - i:
                    return False
            return True

        def solve_n_queens(sol, n):
            if len(sol) == n:
                self.solutions.append(sol[:])
                return

            for i in range(n):
                if can_extend(sol, i):
                    sol.append(i)
                    solve_n_queens(sol, n)
                    sol.pop()

            return

        def format_sol(sol, n):
            out = []
            for i in range(n):
                out.append(''.join('Q' if sol[i] == j else '.' for j in range(n)))
            return out

        solve_n_queens([], n)

        return [format_sol(s, n) for s in self.solutions]
