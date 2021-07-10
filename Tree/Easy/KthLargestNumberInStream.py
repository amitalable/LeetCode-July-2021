# https://leetcode.com/problems/kth-largest-element-in-a-stream/

import heapq
from typing import List
import bisect


class KthLargestUsingBisect:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        bisect.insort(self.nums, val)
        return self.nums[len(self.nums)-k]


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums[:k]
        heapq.heapify(self.heap)
        for num in nums[k:]:
            print(heapq.heappushpop(self.heap, num))

    def add(self, val: int) -> int:
        fn = heapq.heappush
        if len(self.heap) == self.k:
            fn = heapq.heappushpop
        print(fn(self.heap, val), self.heap)

        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
k = 3
nums = [4, 5, 8, 2]
val = [3, 5, 10, 9, 4]
obj = KthLargest(k, nums)
for i in val:
    param_1 = obj.add(i)
    print(param_1)
