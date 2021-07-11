# https://leetcode.com/problems/find-median-from-data-stream/

import bisect


class MedianFinder:

    def __init__(self):
        self.l = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.l, num)

    def findMedian(self) -> float:
        x = len(self.l)//2
        if len(self.l) % 2 == 0:
            return (self.l[x-1] + self.l[x])/2
        else:
            return self.l[x]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
