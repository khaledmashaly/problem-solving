# https://leetcode.com/problems/permutation-in-string/submissions/891237649/
from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        chars = defaultdict(int)

        for c in s1:
            chars[c] += 1

        for i in range(len(s1)):
            chars[s2[i]] -= 1

        for i in range(len(s1), len(s2)):
            if not any(chars.values()):
                return True

            c_out = s2[i - len(s1)]
            chars[c_out] += 1

            c_in = s2[i]
            chars[c_in] -=1

        return not any(chars.values())
