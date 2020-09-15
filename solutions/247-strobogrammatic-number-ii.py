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


def findStrobogrammatic(n: int) -> List[str]:
    def backtrack(n, consecutive=True):
        if n == 0:
            return [""]
        if n == 1:
            return ["0", "1", "8"]

        twins = [("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")] + \
            ([("0", "0")] * consecutive)

        return [a + s + b for s in backtrack(n-2) for a, b in twins]

    return backtrack(n, False)


print(findStrobogrammatic(2), ["11", "69", "88", "96"])
