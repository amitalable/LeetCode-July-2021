# https://leetcode.com/problems/longest-increasing-subsequence/

from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLISUsingDP(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)

    def lengthOfLISUsingBisect(self, nums: List[int]) -> int:
        LIS = []
        for num in nums:
            idx = bisect_left(LIS, num)
            if idx == len(LIS):
                LIS.append(num)
            else:
                LIS[idx] = num
        return len(LIS)


arr = [10, 9, 2, 5, 3, 7, 101, 18]
obj = Solution()
print(obj.lengthOfLIS(arr))
