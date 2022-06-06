# Range Sum Query 2D - Immutable
# https://leetcode.com/problems/range-sum-query-2d-immutable/
# medium
#
# Tags: Facebook, Google, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        n = len(matrix) + 1
        m = len(matrix[0]) + 1
        self.sums = [[0] * m for _ in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                self.sums[i][j] = self.sums[i][j - 1] + matrix[i - 1][j - 1]

        for j in range(1, m):
            for i in range(1, n):
                self.sums[i][j] += self.sums[i - 1][j]

        print(self.sums)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2 + 1][col2 + 1] - self.sums[row1][
            col2 + 1] - self.sums[row2 + 1][col1] + self.sums[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# 3 0 1
# 5 6 3
# 1 2 0

# 3  3  4
# 8 14 18
# 9 17 21

# 21 - 9 - 0 + 0 = 12
