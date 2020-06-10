# Swap Adjacent in LR String
# https://leetcode.com/problems/swap-adjacent-in-lr-string/
# medium
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def canTransform(start: str, end: str) -> bool:
    if start.replace("X", "") != end.replace("X", ""):
        return False

    p1 = p2 = 0
    l1 = len(start)
    l2 = len(end)

    while p1 < l1 and p2 < l2:
        while p1 < l1 and start[p1] == "X":
                p1 += 1

        while p2 < l2 and end[p2] == "X":
                p2 += 1

        if p1 == l1 and p2 == l2:
            return True

        if p1 == l1 or p2 == l2:
            return False

        if start[p1] != end[p2]:
            return False

        if start[p1] == "L" and p2 > p1:
            return False

        if start[p1] == "R" and p1 > p2:
            return False

        p1 += 1
        p2 += 1

    return True

print(canTransform(start = "RXXLRXRXL", end = "XRLXXRRLX"), True)
