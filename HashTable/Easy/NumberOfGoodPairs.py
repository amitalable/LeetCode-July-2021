from typing import List
from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        res = 0
        for val in d.values():
            res += (val - 1) * val // 2
        return res


obj = Solution()
print(obj.numIdenticalPairs([1, 1, 1, 1]))
