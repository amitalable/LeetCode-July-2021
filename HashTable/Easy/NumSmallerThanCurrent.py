from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        sorted_nums = sorted(nums)
        return [sorted_nums.index(i) for i in nums]


print(Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
