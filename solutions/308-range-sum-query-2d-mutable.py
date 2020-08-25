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
        pass

    def update(self, row: int, col: int, val: int) -> None:
        pass

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pass


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
