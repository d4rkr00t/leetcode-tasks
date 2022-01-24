# Minimum Number of Increments on Subarrays to Form a Target Array
# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/
# hard
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def minNumberOperations(target: List[int]) -> int:
    res = pre = 0

    for n in target:
        res += max(n - pre, 0)
        pre = n

    return res


print(minNumberOperations([1, 2, 3, 2, 1]), 3)
print(minNumberOperations([3, 1, 1, 2]), 4)
print(minNumberOperations([3, 1, 5, 4, 2]), 7)
