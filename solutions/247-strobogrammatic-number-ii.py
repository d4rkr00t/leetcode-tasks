# Strobogrammatic Number II
# https://leetcode.com/problems/strobogrammatic-number-ii/
# medium
#
# Tags: Facebook, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def findStrobogrammatic(n: int, first=True) -> List[str]:
    table = {"1": "1", "6": "9", "8": "8", "9": "6"}

    if n == 0: return [""] if not first else []
    if n == 1: return ["0", "1", "8"]

    res = []
    prev = findStrobogrammatic(n - 2, False)

    if not first:
        table["0"] = "0"

    for k, v in table.items():
        for s in prev:
            res.append(k + s + v)

    return res


print(findStrobogrammatic(2), ["11", "69", "88", "96"])
print(findStrobogrammatic(3))
print(findStrobogrammatic(0))
