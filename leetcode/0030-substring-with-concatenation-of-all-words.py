# https://leetcode.com/submissions/detail/777754457/

from copy import copy


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        d = {}

        for word in words:
            d[word] = 1 if word not in d else d[word] + 1

        n = len(s)
        l = len(words[0])
        m = len(words) * l

        sol = []
        for i in range(n - m + 1):
            di = copy(d)
            for j in range(i, i + m, l):
                cur = s[j:j + l]
                if cur in di:
                    if di[cur] > 1:
                        di[cur] -= 1
                    else:
                        di.pop(cur)
                else:
                    break
            else:
                sol.append(i)

        return sol
