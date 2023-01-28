# https://leetcode.com/problems/data-stream-as-disjoint-intervals/submissions/886978927/

from sortedcontainers import SortedList

class SummaryRanges:
    def __init__(self):
        self.intervals = SortedList(key=lambda interval: interval[0])

    def addNum(self, value: int) -> None:
        if len(self.intervals) == 0:
            self.intervals.add([value, value])
            return

        i = self.intervals.bisect_left([value])
        if i == len(self.intervals):
            if self.intervals[-1][1] == value - 1:
                self.intervals[-1][1] = value
            elif self.intervals[-1][1] < value - 1:
                self.intervals.add([value, value])
        elif i == 0:
            if self.intervals[0][0] == value + 1:
                self.intervals[0][0] = value
            elif self.intervals[0][0] > value + 1:
                self.intervals.add([value, value])
        elif self.intervals[i - 1][1] == value - 1 and self.intervals[i][0] == value + 1:
            high = self.intervals.pop(i)[1]
            self.intervals[i - 1][1] = high
        elif self.intervals[i][0] == value + 1:
            high = self.intervals.pop(i)[1]
            self.intervals.add([value, high])
        elif self.intervals[i - 1][1] == value - 1:
            self.intervals[i - 1][1] = value
        elif self.intervals[i - 1][1] < value - 1 and self.intervals[i][0] > value + 1:
            self.intervals.add([value, value])

    def getIntervals(self) -> List[List[int]]:
        return self.intervals
