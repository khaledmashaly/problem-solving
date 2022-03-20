# https://leetcode.com/submissions/detail/662418534/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        last = dict()

        for i in reversed(range(n)):
            if s[i] not in last:
                last[s[i]] = i

        out = list()
        visited = set()

        for i in range(n):
            if s[i] not in visited:
                while len(out) > 0 and out[-1] > s[i] and last[out[-1]] > i:
                    visited.remove(out.pop())

                out.append(s[i])
                visited.add(s[i])

        return ''.join(out)
