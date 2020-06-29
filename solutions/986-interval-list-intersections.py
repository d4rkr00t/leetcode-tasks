# Interval  Intersections
# https://leetcode.com/problems/interval-list-intersections/
# medium
#
# Tags: Facebook, Google, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def intervalIntersection(A: [[int]], B: [[int]]) -> [[int]]:
    ans = []

    a = 0
    b = 0

    while a < len(A) and b < len(B):
        ai = A[a] if a < len(A) else None
        bi = B[b] if b < len(B) else None

        if not ai:
            ans.append(bi)
            b += 1
            continue

        if not bi:
            ans.append(ai)
            a += 1
            continue

        if ai and bi and ai[0] <= bi[1] and ai[1] >= bi[0]:
            ans.append([max(ai[0], bi[0]), min(ai[1], bi[1])])

        if ai[1] >= bi[1]:
            b += 1

        if ai[1] <= bi[1]:
            a += 1

    return ans

print(intervalIntersection(A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]), [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]])
