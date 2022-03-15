# https://leetcode.com/submissions/detail/660734629/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        opening = '('
        closing = ')'
        delete = [False] * n

        opening_count = 0
        for i in range(n):
            if s[i] == opening:
                opening_count += 1
            if s[i] == closing:
                if opening_count == 0:
                    delete[i] = True
                else:
                    opening_count -= 1

        closing_count = 0
        for i in reversed(range(n)):
            if s[i] == closing:
                closing_count += 1
            if s[i] == opening:
                if closing_count == 0:
                    delete[i] = True
                else:
                    closing_count -= 1

        return ''.join(s[i] for i in range(n) if not delete[i])
