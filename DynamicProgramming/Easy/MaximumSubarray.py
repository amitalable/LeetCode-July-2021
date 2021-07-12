# https://leetcode.com/problems/maximum-subarray/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ps = cs = nums[0]
        for i in range(1, len(nums)):
            cs = max(nums[i], cs+nums[i])
            if(ps < cs):
                ps = cs
        return ps


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
