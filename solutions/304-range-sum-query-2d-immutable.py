# Range Sum Query 2D - Immutable
# https://leetcode.com/problems/range-sum-query-2d-immutable/
# medium
#
# Tags: Facebook, Google, Amazon
#
# Time:  O(1) for query, O(n*m) for construction
# Space: O(n*m)
#
# Solution:
# TBD

class NumMatrix:

    def __init__(self, matrix: [[int]]):
        if not matrix or not matrix[0]:
            return
        self.cache = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        self.matrix = matrix

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.cache[i+1][j+1] = self.cache[i+1][j] + self.cache[i][j+1] + matrix[i][j] - self.cache[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.cache[row2+1][col2+1] - self.cache[row1][col2+1] - self.cache[row2+1][col1] + self.cache[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
