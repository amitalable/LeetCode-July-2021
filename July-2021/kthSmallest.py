# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = [matrix[row][col]
             for row in range(len(matrix))
             for col in range(len(matrix[0]))]
        l.sort()
        return l[k-1]


obj = Solution()
matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
print(obj.kthSmallest(matrix, k))
