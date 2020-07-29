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

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return

        self.m, self.n = len(matrix), len(matrix[0])
        self.marix = [[0] * self.n for _ in range(self.m)]
        self.bit = [[0] * (self.n+1) for _ in range(self.m+1)]

        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        diff = val - self.marix[row][col]
        i, self.marix[row][col] = row + 1, val
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.bit[i][j] += diff
                j += (j & -j)

            i += (i & -i)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sumCorner(row2, col2) + \
            self.sumCorner(row1 - 1, col1-1) - \
            self.sumCorner(row1-1, col2) - \
            self.sumCorner(row2, col1 - 1)

    def sumCorner(self, row, col):
        res, i = 0, row + 1
        while i:
            j = col + 1
            while j:
                res += self.bit[i][j]
                j -= (j & -j)
            i -= (i & -i)

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
