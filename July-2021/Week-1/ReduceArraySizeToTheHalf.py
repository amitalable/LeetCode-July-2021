# https://leetcode.com/problems/reduce-array-size-to-the-half/

from typing import List
from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        freq = sorted(list(Counter(arr).values()), reverse=True)
        removed, res = 0, 0
        while removed < n//2:
            removed += freq[res]
            res += 1
        return res


arr = [9, 77, 63, 22, 92, 9, 14, 54, 8, 38, 18, 19, 38, 68, 58, 19]
obj = Solution()
print(obj.minSetSize(arr))
