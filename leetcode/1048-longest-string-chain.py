# https://leetcode.com/submissions/detail/724724251/

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)

        tab = {}

        ans = 0
        for cur in words:
            tab[cur] = 1

            for i in range(len(cur)):
                prev = cur[:i] + cur[i + 1:]
                if prev in tab:
                    tab[cur] = max(tab[cur], tab[prev] + 1)

            ans = max(ans, tab[cur])

        return ans
