# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        l = [1, 1]

        for i in range(2, n+1):
            l.append(l[i-1]+l[i-2])

        return l[n]


obj = Solution()
print(obj.climbStairs(3))
