# Maximal Rectangle
# https://leetcode.com/problems/maximal-rectangle/
# hard
#
# Tags: Google, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def maximalRectangle(matrix: List[List[str]]) -> int:
    pass


print(
    maximalRectangle([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
                      ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]),
    6)
print(maximalRectangle([["0"]]), 0)
print(maximalRectangle([["1"]]), 1)
