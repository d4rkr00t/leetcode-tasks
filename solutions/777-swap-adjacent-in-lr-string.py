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

import operator


def canTransform(start: str, end: str) -> bool:
    if start.replace('X', '') != end.replace('X', ''):
        return False

    for (symbol, op) in (('L', operator.ge), ('R', operator.le)):
        B = (i for i, c in enumerate(end) if c == symbol)
        for i, c in enumerate(start):
            if c == symbol and not op(i, next(B)):
                return False

    return True


print(canTransform(start="RXXLRXRXL", end="XRLXXRRLX"), True)
