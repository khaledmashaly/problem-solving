# https://leetcode.com/submissions/detail/659199314/

class Solution:
    def isValid(self, s: str) -> bool:
        opening = '({['
        closing = ')}]'

        match = {closing[i]: opening[i] for i in range(len(opening))}

        stack = []

        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
            elif len(stack) < 1 or stack.pop() != match[s[i]]:
                return False

        return len(stack) == 0
