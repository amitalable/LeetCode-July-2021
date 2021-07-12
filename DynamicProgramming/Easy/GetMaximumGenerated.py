# https://leetcode.com/problems/get-maximum-in-generated-array/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0, 1]+[0] * (n - 1)
        x = n//2 + 1 if n % 2 == 1 else n//2
        for i in range(1, x):
            nums[2*i] = nums[i]
            nums[2*i + 1] = nums[i] + nums[i+1]
        return max(nums)


obj = Solution()
print(obj.getMaximumGenerated(5))
