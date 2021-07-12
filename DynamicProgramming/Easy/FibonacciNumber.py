# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        l = [0, 1]
        for i in range(2, n+1):
            l.append(l[i-1]+l[i-2])
        return l[n]


print(Solution().fib(1))
