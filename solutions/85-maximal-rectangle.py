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
    def maxhistarea(heights):
        stack = [-1]
        maxarea = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                maxarea = max(maxarea,
                              heights[stack.pop()] * (i - stack[-1] - 1))

            stack.append(i)

        while stack[-1] != -1:
            maxarea = max(
                maxarea, heights[stack.pop()] * (len(heights) - stack[-1] - 1))

        return maxarea

    if not matrix:
        return 0

    maxarea = 0
    dp = [0] * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0

        maxarea = max(maxarea, maxhistarea(dp))

    return maxarea


print(
    maximalRectangle([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
                      ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]),
    6)
print(maximalRectangle([["0"]]), 0)
print(maximalRectangle([["1"]]), 1)

# ["1", "0", "1", "0, "0"],
# ["1", "0", "1", "1", "1"],
# ["1", "1", "1", "1", "1"],
# ["1", "0", "0", "1", "0"]
#
# [1, 0, 1, 0, 0],
# [1, 0, 1, 2, 3],
# [1, 2, 3, 4, 5],
# [1, 0, 0, 1, 0],
