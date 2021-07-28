# https://leetcode.com/problems/beautiful-array
from typing import List


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        dp = [None]*(n+1)
        dp[1] = [1]
        for i in range(2, n+1):
            # considering odd cases and even cases
            dp[i] = [(2*j)-1 for j in dp[(i+1)//2]] + [(2*j) for j in dp[i//2]]
        return dp[n]


obj = Solution()
print(obj.beautifulArray(5))
