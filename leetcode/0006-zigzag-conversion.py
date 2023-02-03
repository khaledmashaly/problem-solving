# https://leetcode.com/problems/zigzag-conversion/submissions/890749916/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ans = []
        d1 = (numRows - 1) * 2
        d2 = 0
        for i in range(numRows):
            if len(ans) == len(s):
                break
            c = i
            turn = True
            while c < len(s):
                if len(ans) == 0 or (len(ans) > 0 and ans[-1] != c):
                    ans.append(c)
                c += d1 if turn else d2
                turn = not turn
            d1 -= 2
            d2 += 2
        
        return ''.join(s[c] for c in ans)
