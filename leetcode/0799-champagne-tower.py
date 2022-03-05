# https://leetcode.com/submissions/detail/653857920/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        current_row = [poured]

        for r in range(query_row):
            next_row = [0] * (r + 2)

            for c in range(r + 1):
                if current_row[c] > 1:
                    spill = (current_row[c] - 1) / 2
                    next_row[c] += spill
                    next_row[c + 1] += spill

            current_row = next_row

        return min(current_row[query_glass], 1)
