from typing import List
from numpy import reshape


class Solution:
    def matrixReshapeUsingBruteForce(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row, col = len(mat), len(mat[0])

        l = []
        if r * c == row * col:
            new_mat = [[0 for i in range(c)] for j in range(r)]
            for i in range(row):
                for j in range(col):
                    l.append(mat[i][j])

            for i in range(r):
                for j in range(c):
                    new_mat[i][j] = l.pop(0)

            return new_mat
        return mat

    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ans = [element for row in mat for element in row]
        if len(ans) == r*c:
            return [ans[i*c:(i+1)*c] for i in range(r)]
        return mat

    def matrixReshapeUsingNumpy(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        return reshape(mat, (r, c)).tolist()


def main():
    mat = [[1, 2], [3, 4]]
    r = 4
    c = 1
    obj = Solution().matrixReshapeUsingBruteForce(mat, r, c)
    print(obj)


if __name__ == "__main__":
    main()
