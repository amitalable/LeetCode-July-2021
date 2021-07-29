# https://leetcode.com/problems/01-matrix/
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        h, w = len(matrix), len(matrix[0])

        distance = [[float('inf') for _ in range(w)] for _ in range(h)]

        # first propagation

        for y in range(h):
            for x in range(w):

                if matrix[y][x] == 0:
                    # current matrix[y][x] is 0 already
                    distance[y][x] = 0

                else:
                    # current matrix[y][x] is 1, propagate distance from top and left

                    if y > 0:
                        # propagate shorter distance from top
                        distance[y][x] = min(
                            distance[y][x], distance[y-1][x] + 1)

                    if x > 0:
                        # progagate shorter distance from left
                        distance[y][x] = min(
                            distance[y][x], distance[y][x-1] + 1)

        # second propagation

        for y in reversed(range(h)):
            for x in reversed(range(w)):

                if distance[y][x] not in (0, 1):
                    # skip those grids with distance 0 or 1, because they are optimal already

                    # current matrix[y][x] is 1, propagate distance from bottom and right

                    if y < h-1:
                        # propagate shorter distance from bottom
                        distance[y][x] = min(
                            distance[y][x], distance[y+1][x] + 1)

                    if x < w-1:
                        # progagate shorter distance from right
                        distance[y][x] = min(
                            distance[y][x], distance[y][x+1] + 1)

        return distance
