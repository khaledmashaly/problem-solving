# https://leetcode.com/submissions/detail/741380088/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str, memo = {}) -> bool:
        n = len(s1)
        m = len(s2)

        if (s1, s2, s3) in memo:
            return memo[(s1, s2, s3)]

        if len(s3) != len(s1) + len(s2):
            return False

        if s1 == "":
            return s2 == s3

        if s2 == "":
            return s1 == s3

        one = self.isInterleave(s1[1:], s2, s3[1:], memo) if s1[0] == s3[0] else False
        two = self.isInterleave(s1, s2[1:], s3[1:], memo) if s2[0] == s3[0] else False

        memo[(s1, s2, s3)] = one or two

        return memo[(s1, s2, s3)]
