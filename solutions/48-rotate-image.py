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
# Transpose a matrix

def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    for i in range(len(matrix)):
        matrix[i].reverse()

    return matrix


print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
