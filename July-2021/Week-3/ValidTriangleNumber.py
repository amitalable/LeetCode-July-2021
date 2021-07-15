from typing import List
from itertools import combinations


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums)):
            current = nums[i]
            left, right = 0, i-1
            while left < right:
                if nums[left] + nums[right] > current:
                    result += right - left
                    right -= 1
                else:
                    left += 1
        return result


obj = Solution()
print(obj.triangleNumber([24, 3, 82, 22, 35, 84, 19, 10, 15, 20,
      34, 23, 45, 53, 24, 4, 55, 42, 4, 5, 45, 32, 121, 22, 12]))
