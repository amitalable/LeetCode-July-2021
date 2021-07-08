# https://leetcode.com/problems/maximum-length-of-repeated-subarray
from typing import List


class Solution:
    def findLengthUsingDynamicProgramming(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for i in range(len(nums1)+1)] for i in range(len(nums2)+1)]
        m = 0
        for row in range(1, len(nums2)+1):
            for col in range(1, len(nums1)+1):
                if nums2[row-1] == nums1[col-1]:
                    dp[row][col] = dp[row-1][col-1] + 1
                    m = max(m, dp[row][col])
        return m

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        num2_str = ''.join([chr(x) for x in nums2])
        subarray = ''
        max_subarray = 0

        for bit in nums1:
            subarray = subarray + chr(bit)
            if subarray in num2_str:
                max_subarray = len(subarray)
            else:
                subarray = subarray[1:]

        return max_subarray


obj = Solution()
nums1 = [1, 2, 3, 2, 1]
nums2 = [3, 2, 1, 4, 7]
print(obj.findLength(nums1, nums2))
print(obj.findLengthUsingDynamicProgramming(nums1, nums2))
