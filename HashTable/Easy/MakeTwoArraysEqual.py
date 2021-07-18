# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/

from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)


print(Solution().canBeEqual([1, 2, 3, 4], [1, 2, 4, 3]))
