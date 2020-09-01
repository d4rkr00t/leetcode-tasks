# Sparse Matrix Multiplication
# https://leetcode.com/problems/sparse-matrix-multiplication/
# medium
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def multiply(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    m = len(A)
    n = len(B)
    k = len(B[0])
    res = [[0] * k for _ in range(m)]
    ns_a = [[(j, A[i][j]) for j in range(len(A[0])) if A[i][j] != 0]
            for i in range(m)]
    ns_b = [[(i, B[i][j]) for i in range(n) if B[i][j] != 0]
            for j in range(k)]

    for i in range(m):
        row_a = ns_a[i]
        for col_a, val_a in row_a:
            for j in range(k):
                col_b = ns_b[j]
                for row_b, val_b in col_b:
                    if row_b == col_a:
                        res[i][j] += val_a * val_b

    return res


print(multiply(A=[[1, 0, 0], [-1, 0, 3]], B=[[7, 0, 0],
                                             [0, 0, 0], [0, 0, 1]]), [[7, 0, 0], [-7, 0, 3]])

print(multiply(A=[[1, -5]], B=[[12], [-1]]), [[17]])
