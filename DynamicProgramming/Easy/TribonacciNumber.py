# https://leetcode.com/problems/n-th-tribonacci-number

class Solution:
    def tribonacci(self, n: int) -> int:
        tribonacci = [0, 1, 1] + [0]*(n-2)
        for i in range(3, n+1):
            tribonacci[i] = tribonacci[i-1] + tribonacci[i-2] + tribonacci[i-3]
        return tribonacci[n]


obj = Solution()
print(obj.tribonacci(5))
