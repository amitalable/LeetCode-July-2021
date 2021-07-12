# https://leetcode.com/problems/pascals-triangle/
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTriangle = [[1]]
        x = 2
        while x <= numRows:
            pascalTriangle.append([1]+[pascalTriangle[-1][i] + pascalTriangle[-1][i+1]
                                  for i in range(len(pascalTriangle[-1])-1)]+[1])
            x += 1
        return pascalTriangle


obj = Solution()
pascal_triangle = obj.generate(5)
print(pascal_triangle)
