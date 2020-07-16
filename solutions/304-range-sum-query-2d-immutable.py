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
# Cumulative row sum

class NumMatrix:

    def __init__(self, matrix: [[int]]):
        self.cache = [[0] * (len(matrix) + 1) for _ in range(len(matrix) + 1)]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.cache[r+1][c+1] = self.cache[r+1][c] + \
                    self.cache[r][c+1] + matrix[r][c] - self.cache[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.cache[row2+1][col2+1] - self.cache[row1][col2+1] - self.cache[row2+1][col1] + self.cache[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
