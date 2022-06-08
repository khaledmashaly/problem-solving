# https://leetcode.com/submissions/detail/717640064/

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def is_palindrome(s):
            n = len(s)
            for i in range(n // 2):
                if s[i] != s[n - i - 1]:
                    return False
            return True

        return 1 if is_palindrome(s) else 2
