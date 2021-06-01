# Strobogrammatic Number II
# https://leetcode.com/problems/strobogrammatic-number-ii/
# medium
#
# Tags: Facebook, Google
#
# Time:  O(N!)
# Space: TBD
#
# Solution:
# TBD

from typing import List


def findStrobogrammatic(n: int, allowZeros=False) -> List[str]:
    ans = []
    if n == 0:
        return [""]

    if n == 1:
        return ["0", "1", "8"]

    table = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

    for k in table.keys():
        if not allowZeros and k == "0":
            continue

        r = table[k]
        nums = findStrobogrammatic(n - 2, True)

        for num in nums:
            ans.append(k + num + r)

    return ans


print(findStrobogrammatic(2), ["11", "69", "88", "96"])
print(findStrobogrammatic(3))
