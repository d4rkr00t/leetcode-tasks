# Longest Turbulent Subarray
# https://leetcode.com/problems/longest-turbulent-subarray/
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


def maxTurbulenceSize(arr: List[int]) -> int:
    up = down = 0
    ans = min(1, len(arr))

    for i in range(1, len(arr)):
        prev = arr[i - 1]
        n = arr[i]

        if n > prev:
            up = down + 1
            down = 0
            ans = max(ans, up + 1)
        elif n < prev:
            down = up + 1
            up = 0
            ans = max(ans, down + 1)
        else:
            down = 0
            up = 0

    return ans


print(maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]), 5)
print(maxTurbulenceSize([4, 8, 12, 16]), 2)
print(maxTurbulenceSize([100]), 1)

#   9 4 2 10 7 8 8 1 9
# ↑ 0 0 0 2  0 4 0 0 2
# ↓ 0 1 1 0  3 0 0 1 0
