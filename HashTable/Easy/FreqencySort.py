from typing import Counter, List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dict = {}
        for c in nums:
            dict[c] = dict.get(c, 0) + 1
        return sorted(nums, key=lambda x: dict[x] * 200 - x)


print(Solution().frequencySort([1, 1, 2, 2, 2, 3]))
