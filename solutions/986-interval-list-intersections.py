# Interval  Intersections
# https://leetcode.com/problems/interval-list-intersections/
# medium
#
# Tags: Facebook, Google, Amazon
#
# Time:  O(min(A,B))
# Space: O(1)
#
# Solution:
# Two Pointers

from typing import List


def intervalIntersection(A: List[List[int]],
                         B: List[List[int]]) -> List[List[int]]:
    pa = pb = 0
    ans = []

    while pa < len(A) or pb < len(B):
        ia = A[pa] if pa < len(A) else None
        ib = B[pb] if pb < len(B) else None

        if not ia or not ib:
            break

        if ia[0] <= ib[1] and ib[0] <= ia[1]:
            ans.append([max(ia[0], ib[0]), min(ia[1], ib[1])])

        if ia[1] > ib[1]:
            pb += 1
        else:
            pa += 1

    return ans


print(
    intervalIntersection(A=[[0, 2], [5, 10], [13, 23], [24, 25]],
                         B=[[1, 5], [8, 12], [15, 24], [25, 26]]),
    [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]])

# 0    2
#   1      5

#   1     5
# 0    2

# 0      5
#   1  3

#   1  3
# 0      5
