# https://leetcode.com/submissions/detail/662986042/

class FreqStack:

    def __init__(self):
        self.max_freq = 0
        self.freqs = dict()
        self.elements = dict()


    def push(self, val: int) -> None:
        self.freqs[val] = self.freqs[val] + 1 if val in self.freqs else 1
        if self.freqs[val] not in self.elements:
            self.elements[self.freqs[val]] = list()
        self.elements[self.freqs[val]].append(val)
        self.max_freq = max(self.max_freq, self.freqs[val])


    def pop(self) -> int:
        top = self.elements[self.max_freq].pop()
        self.freqs[top] -= 1
        if len(self.elements[self.max_freq]) == 0:
            self.max_freq -= 1
        return top