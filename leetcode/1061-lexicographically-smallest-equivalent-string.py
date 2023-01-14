# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/submissions/878147831/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def get_root(i, parent):
            while parent[i] != i:
                i = parent[i]
            return i

        parent = list(range(26))

        for c1, c2 in zip(s1, s2):
            c1i = ord(c1) - ord('a')
            c2i = ord(c2) - ord('a')

            c1r = get_root(c1i, parent)
            c2r = get_root(c2i, parent)

            p = min(c1r, c2r)
            c = max(c1r, c2r)

            parent[c] = p

        ans = []
        for c in baseStr:
            ci = ord(c) - ord('a')
            cr = get_root(ci, parent)
            ans.append(chr(ord('a') + cr))

        return ''.join(ans)
