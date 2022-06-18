# https://leetcode.com/submissions/detail/725403786/

from collections import defaultdict
from itertools import zip_longest


class Trie:
    def __init__(self):
        self.index = None
        self.children = defaultdict(lambda: Trie())


class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = Trie()

        for i, word in enumerate(words):
            cur = self.trie

            n = len(word)
            for j in range(n):
                tmp = cur
                for c in word[j:]:
                    tmp = tmp.children[c, None]
                    tmp.index = i

                tmp = cur
                for c in reversed(word[:-j or n]):
                    tmp = tmp.children[None, c]
                    tmp.index = i

                cur = cur.children[word[j], word[-j - 1]]
                cur.index = i


    def f(self, prefix: str, suffix: str) -> int:
        search = zip_longest(prefix, reversed(suffix))
        cur = self.trie
        for p, s in search:
            if (p, s) not in cur.children:
                return -1

            cur = cur.children[p, s]

        return cur.index
