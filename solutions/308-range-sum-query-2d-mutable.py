# Range Sum Query 2D - Mutable
# https://leetcode.com/problems/range-sum-query-2d-mutable/
# hard
#
# Tags: Google, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.rows = []
            return
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.matrix = matrix
        self.rows = [[0] * self.m for _ in range(self.n)]

        for i in range(self.n):
            for j in range(self.m):
                if j == 0:
                    self.rows[i][j] = matrix[i][j]
                else:
                    self.rows[i][j] = matrix[i][j] + self.rows[i][j - 1]

    def update(self, row: int, col: int, val: int) -> None:
        self.matrix[row][col] = val
        for j in range(col, self.m):
            if j == 0:
                self.rows[row][j] = self.matrix[row][j]
            else:
                self.rows[row][j] = self.matrix[row][j] + self.rows[row][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0

        for i in range(row1, row2 + 1):
            right = self.rows[i][col2]
            left = 0 if col1 - 1 < 0 else self.rows[i][col1 - 1]
            res += right - left

        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)

# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]

# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10

# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]

# row sum= [
#   [3,  3   4,  8, 10],
#   [5, 11, 14, 16, 17],
#   [1,  3,  3,  4,  9],
#   [4,  5,  5,  6, 13],
#   [1,  1,  4,  4,  9]
# ]

# col sum= [
#   [ 3,  3,  4,  8, 10],
#   [ 8, 14, 18, 24, 27],
#   [ 9, 17, 21, 28, 36],
#   [13, 22, 26, 34, 49],
#   [14, 23, 30, 38, 58]
# ]
