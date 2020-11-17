# Range Sum Query 2D - Mutable
# https://leetcode.com/problems/range-sum-query-2d-mutable/
# hard
#
# Tags: Google, Microsoft
#
# Time:  O(n) – update, O(m) – sum
#          n – number of columns
#          m - number of rows
# Space: O(n*m)

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            self.matrix = [[]]
            return

        self.matrix = matrix

        for row in range(len(matrix)):
            for col in range(1, len(matrix[0])):
                self.matrix[row][col] += self.matrix[row][col-1]

    def update(self, row: int, col: int, val: int) -> None:
        orig = self.matrix[row][col]
        if col != 0:
            orig -= self.matrix[row][col-1]

        diff = orig - val
        for i in range(col, len(self.matrix[0])):
            self.matrix[row][i] -= diff

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0

        for i in range(row1, row2+1):
            s += self.matrix[i][col2]
            if col1 > 0:
                s -= self.matrix[i][col1-1]

        return s

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

#   [3,   3,  4,   8,  10],
#   [5, (11), 14,  16, 17],
#   [1,   3,  3,   4,   9],
#   [4,   5,  5,   6,  13],
#   [1,   1,  4,  (4),  9]
#   11-5 + 16-11 = 11
#   3-1  + 4-3   = 3
#   5-4  + 6-5   = 2
#   1-1 + 4-1    = 3
#  18

# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10
