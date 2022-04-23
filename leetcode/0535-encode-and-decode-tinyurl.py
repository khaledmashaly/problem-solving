# https://leetcode.com/submissions/detail/686215092/

from random import randint

SYMBOLS = [chr(x) for x in range(ord('a'), ord('z') + 1)]
SYMBOLS += [chr(y) for y in range(ord('A'), ord('Z') + 1)]
SYMBOLS += [str(z) for z in range(10)]

SYMBOL_COUNT = len(SYMBOLS)
URL_SIZE = 8
URL_COUNT = SYMBOL_COUNT ** URL_SIZE


class Codec:
    def __init__(self):
        self.store = dict()

    def key_to_short_url(self, key: int) -> str:
        short_url = list()

        for i in range(URL_SIZE):
            symbol_index = int(key % SYMBOL_COUNT)
            symbol = SYMBOLS[symbol_index]
            short_url.append(symbol)
            key /= SYMBOL_COUNT

        return ''.join(short_url)

    def encode(self, long_url: str) -> str:
        key = randint(0, URL_COUNT - 1)
        short_url = self.key_to_short_url(key)
        self.store[short_url] = long_url
        return short_url

    def decode(self, short_url: str) -> str:
        return self.store[short_url]
