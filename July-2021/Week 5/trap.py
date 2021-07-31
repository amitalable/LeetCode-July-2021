# https://leetcode.com/problems/trapping-rain-water
from typing import List
from itertools import accumulate


class Solution:
    def trap(self, H: List[int]) -> int:
        left = list(accumulate(H, max))
        right = list(accumulate(H[::-1], max))[::-1]
        return sum(min(i, j) - k for i, j, k in zip(left, right, H))
