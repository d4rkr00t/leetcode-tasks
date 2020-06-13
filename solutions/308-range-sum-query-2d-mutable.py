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

    def __init__(self, matrix: [[int]]):
        if not matrix or not matrix[0]:
            return

        self.m = len(matrix)
        self.n = len(matrix[0])

        self.tree = [[0] * (self.n+1) for _ in range(self.m+1)]
        self.nums = [[0] * (self.n) for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])


    def update(self, row: int, col: int, val: int) -> None:
        if self.m == 0 or self.n == 0:
            return

        delta = val - self.nums[row][col]
        self.nums[row][col] = val

        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.tree[i][j] += delta
                j += (j & -j)

            i += (i & -i)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.m == 0 or self.n == 0:
            return

        return self.sum(row2+1, col2+1) + self.sum(row1, col1) - self.sum(row1, col2+1) - self.sum(row2+1, col1)

    def sum(self, row, col):
        s = 0

        i = row
        while i > 0:
            j = col
            while j > 0:
                s += self.tree[i][j]
                j -= (j & -j)

            i -= (i & -i)

        return s



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

obj = NumMatrix(matrix)

print(obj.sumRegion(2, 1, 4, 3), 8)
obj.update(3, 2, 2)
print(obj.sumRegion(2, 1, 4, 3), 10)
