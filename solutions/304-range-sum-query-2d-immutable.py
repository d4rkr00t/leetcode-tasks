# Range Sum Query 2D - Immutable
# https://leetcode.com/problems/range-sum-query-2d-immutable/
# medium
#
# Tags: Facebook, Google, Amazon
#
# Time:  O(n*m) – O(1)
# Space: O(n*m)
#
# Solution:
# TBD

from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        n = len(matrix) + 1
        m = len(matrix[0]) + 1
        self.sum = [[0] * m for _ in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                self.sum[i][j] += matrix[i - 1][j - 1]

        for j in range(1, m):
            for i in range(1, n):
                self.sum[i][j] += self.sum[i - 1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2 + 1][col2 + 1] - self.sums[row1][
            col2 + 1] - self.sums[row2 + 1][col1] + self.sums[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# query = [2, 1, 4, 3]

# 38 - 24 - 14 + 17
#    0   1   2   3   4   5
# 0 [0,  0,  0,  0,  0,  0],
# 1 [0,  3,  3,  4,  8, 10],
# 2 [0,  8, 14, 18, 24, 27],
# 3 [0,  9, 17, 21, 28, 36],
# 4 [0, 13, 22, 26, 34, 49],
# 5 [0, 14, 23, 30, 38, 58]

# 38 - 24 - 14 + 8 = 8
