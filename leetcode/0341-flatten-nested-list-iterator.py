# https://leetcode.com/submissions/detail/695713723/

class NestedIterator:
    def __init__(self, nestedList):
        self.iter = self.flatten(nestedList)
        self.next_value = None

    def next(self) -> int:
        return self.next_value

    def hasNext(self) -> bool:
        self.next_value = next(self.iter, None)
        return self.next_value is not None

    def flatten(self, nested_list):
        for i in nested_list:
            if i.isInteger():
                yield i.getInteger()
            else:
                yield from self.flatten(i.getList())
