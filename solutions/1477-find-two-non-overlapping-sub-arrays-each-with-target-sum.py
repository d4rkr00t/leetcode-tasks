# Find Two Non-overlapping Sub-arrays Each With Target Sum
# https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/
# medium
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def minSumOfLengths(arr: List[int], target: int) -> int:
    def buildPrefixSuffix(arr, target):
        res = [float("inf")] * (len(arr) + 1)
        lo = s = 0
        tmp_min = float("inf")
        for hi, n in enumerate(arr):
            s += n

            while s > target:
                s -= arr[lo]
                lo += 1

            if s == target:
                tmp_min = min(tmp_min, hi - lo + 1)

            res[hi + 1] = tmp_min

        return res

    preffix = buildPrefixSuffix(arr, target)
    suffix = buildPrefixSuffix(arr[::-1], target)[::-1]

    ans = min([preffix[i] + suffix[i] for i in range(len(preffix))])

    return ans if ans != float("inf") else -1


print(minSumOfLengths(arr=[3, 3], target=3), 2)
print(minSumOfLengths(arr=[3, 2, 2, 4, 3], target=3), 2)
print(minSumOfLengths(arr=[7, 3, 4, 7], target=7), 2)
print(minSumOfLengths(arr=[4, 3, 2, 6, 2, 3, 4], target=6), -1)
print(minSumOfLengths(arr=[5, 5, 4, 4, 5], target=3), -1)
print(minSumOfLengths(arr=[3, 1, 1, 1, 5, 1, 2, 1], target=3), 3)
print(minSumOfLengths(arr=[1, 2, 2, 3, 2, 6, 7, 2, 1, 4, 8], target=5), 4)

# 3 1 1 1 5 1 2 1 _
#                 |
#                 |
# X 1 1 1 1 1 1 1 1
# 1 2 2 2 2 2 2 X X
