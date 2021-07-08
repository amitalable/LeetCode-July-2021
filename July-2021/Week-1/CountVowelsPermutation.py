# https://leetcode.com/problems/count-vowels-permutation/

from typing import List


class Solution:
    def __init__(self) -> None:
        self.m = [[0, 1, 0, 0, 0],
                  [1, 0, 1, 0, 0],
                  [1, 1, 0, 1, 1],
                  [0, 0, 1, 0, 1],
                  [1, 0, 0, 0, 0]]
        self.len = len(self.m)
        self.MOD = 10**9+7

    def identity(self, n: int) -> List[List[int]]:
        return [[int(i == j) for j in range(n)]for i in range(n)]

    # Multiplication of two matrices
    def mul(self, a: List[int], b: List[int]) -> List[int]:
        n, m, l = len(a), len(b), len(b[0])
        res = [[0] * l for _ in range(n)]
        for i in range(n):
            for j in range(l):
                for k in range(m):
                    res[i][j] += a[i][k] * b[k][j] % self.MOD
                    res[i][j] %= self.MOD
        return res

    # matrix a to the power b
    def power(self, a: List[int], b: int) -> List[int]:
        res = self.identity(len(a))
        while b > 0:
            if b % 2 == 1:
                res = self.mul(res, a)
            a = self.mul(a, a)
            b //= 2
        return res

    def countVowelPermutation(self, n: int) -> int:
        a = self.power(self.m, n - 1)
        res = 0
        for i in range(5):
            for j in range(5):
                res += a[i][j]
                res %= self.MOD
        return res


if __name__ == "__main__":
    obj = Solution()
    print(obj.countVowelPermutation(obj.len-1))
