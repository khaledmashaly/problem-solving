# https://leetcode.com/submissions/detail/784015722/

from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n_count = Counter(str(n))

        for i in range(31):
            if n_count == Counter(str(1 << i)):
                return True

        return False
