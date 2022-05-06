# https://leetcode.com/submissions/detail/694293220/

from collections import deque


class MyStack:
    def __init__(self):
        self.q = deque()


    def push(self, x: int) -> None:
        l = len(self.q)
        self.q.append(x)
        for i in range(l):
            self.q.append(self.q.popleft())


    def pop(self) -> int:
        return self.q.popleft()


    def top(self) -> int:
        return self.q[0]


    def empty(self) -> bool:
        return len(self.q) == 0
