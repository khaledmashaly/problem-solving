# https://leetcode.com/submissions/detail/690980359/

class Solution:
    def type_string(self, s: str):
        out = []

        for c in s:
            if c == '#':
                if len(out) > 0:
                    out.pop()
                continue

            out.append(c)

        return ''.join(out)


    def backspaceCompare(self, s: str, t: str) -> bool:
        s_out = self.type_string(s)
        t_out = self.type_string(t)
        return s_out == t_out
