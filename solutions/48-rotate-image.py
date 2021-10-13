# Rotate Image
# https://leetcode.com/problems/rotate-image/
# medium
#
# Tags: Microsoft, Amazon, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]

    return matrix


# print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
print(rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))

# [5,  2,13,15],
# [1,  4, 3,14],
# [9,  8, 6, 12],
# [11,10,7,16]
