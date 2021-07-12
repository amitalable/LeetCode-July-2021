# https://leetcode.com/problems/pascals-triangle-ii

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascalTriangle = [[1]]
        for i in range(1, rowIndex+1):
            pascalTriangle.append([1] + [pascalTriangle[-1][j] + pascalTriangle[-1][j+1]
                                  for j in range(len(pascalTriangle[-1])-1)] + [1])
        return pascalTriangle[rowIndex]


obj = Solution()
print(obj.getRow(10))
