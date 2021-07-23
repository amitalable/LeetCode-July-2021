# https://leetcode.com/problems/partition-array-into-disjoint-intervals

from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        leftMax = globalMax = nums[0]
        partition = 0
        for i in range(1, len(nums)):
            globalMax = max(globalMax, nums[i])
            if nums[i] < leftMax:
                # If nums[i] < leftMax
                # then nums[i] belong to left subarray,
                # re-partition leftSubArr = nums[0..i]
                partition = i
                leftMax = globalMax
        return partition + 1


obj = Solution()
print(obj.partitionDisjoint([1, 1]))
