# Find Two Non-overlapping Sub-arrays Each With Target Sum
# https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/
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


def minSumOfLengths(arr: List[int], target: int) -> int:
    if len(arr) < 2:
        return -1

    inf = float("inf")
    prefix = [inf] * (len(arr))
    suffix = [inf] * (len(arr))

    lo = 0
    sum = 0
    for hi in range(0, len(arr)):
        prev = prefix[hi - 1] if hi - 1 >= 0 else inf
        if sum == target:
            prefix[hi] = min((hi - lo), prev)
        else:
            prefix[hi] = prev

        sum += arr[hi]

        while sum > target:
            sum -= arr[lo]
            lo += 1

    hi = len(arr) - 1
    sum = 0
    for lo in range(len(arr) - 1, -1, -1):
        sum += arr[lo]

        prev = suffix[lo + 1] if lo + 1 < len(arr) else inf
        if sum == target:
            suffix[lo] = min((hi - lo + 1), prev)
        else:
            suffix[lo] = prev

        while sum > target:
            sum -= arr[hi]
            hi -= 1

    res = min([x + y for x, y in zip(prefix, suffix)])
    # print(prefix)
    # print(suffix)

    return res if res != inf else -1


print(minSumOfLengths(arr=[3, 3], target=3), 2)
print(minSumOfLengths(arr=[3, 2, 2, 4, 3], target=3), 2)
print(minSumOfLengths(arr=[7, 3, 4, 7], target=7), 2)
print(minSumOfLengths(arr=[4, 3, 2, 6, 2, 3, 4], target=6), -1)
print(minSumOfLengths(arr=[5, 5, 4, 4, 5], target=3), -1)
print(minSumOfLengths(arr=[3, 1, 1, 1, 5, 1, 2, 1], target=3), 3)

# 3, 1, 1, 1, 5, 1, 2, 1
# X  1  1  1  1  1  1  1
# 1  2  2  2  2  2  2  X
