# Rotate Image
# https://leetcode.com/problems/rotate-image/
# medium
#
# Tags: Microsoft, Amazon, Facebook
#
# Time:  O(n^2)
# Space: O(1)
#
# Solution:
# Transpose a matrix and reverse rows


def rotate(matrix):
    if not matrix or not matrix[0]:
        return

    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(i, m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()

    return matrix


print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
