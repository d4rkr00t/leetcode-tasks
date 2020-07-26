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
    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]

    return matrix


print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))

# [1, 2, 3, 4],
# [5, 6, 7, 8],
# [9, 10, 11, 12],
# [13, 14, 15, 16]

# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]
