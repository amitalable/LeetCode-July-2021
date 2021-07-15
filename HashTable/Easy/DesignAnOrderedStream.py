# https://leetcode.com/problems/design-an-ordered-stream

from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.d = [None]*(n+1)
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.d[idKey-1] = value
        ind = self.d.index(None)
        l = self.d[self.ptr:ind]
        self.ptr = ind
        return l


# Your OrderedStream object will be instantiated and called as such:
obj = OrderedStream(5)
n = [[3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
for idKey, value in n:
    param_1 = obj.insert(idKey, value)
    print(param_1)
