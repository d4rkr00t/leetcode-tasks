# Merge Intervals
# https://leetcode.com/problems/merge-intervals/
# medium
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  O(N*log(N))
# Space: O(N)
#
# Solution:
# TBD

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    ans = []

    if not intervals:
        return ans

    intervals.sort()
    cur = None

    for s1, e1 in intervals:
        if not cur:
            cur = [s1, e1]
            continue

        s2, e2 = cur

        if s1 <= e2 and s2 <= e1:
            cur = [min(s1, s2), max(e1, e2)]
        else:
            ans.append(cur)
            cur = [s1, e1]

    ans.append(cur)
    return ans


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])
print(merge([[1, 4], [4, 5]]), [[1, 5]])
