# Insert Interval
# https://leetcode.com/problems/insert-interval/
# medium
#
# Tags: Google, Facebook, Amazon
#
# Time:  O(N)
# Space: O(N)
#
# Solution:
# TBD

from typing import List


def insert(intervals: List[List[int]],
           newInterval: List[int]) -> List[List[int]]:
    ans = []
    i = 0

    while i < len(intervals):
        s1, e1 = newInterval
        s2, e2 = intervals[i]

        if e1 < s2:
            ans.append(newInterval)
            ans = ans + intervals[i:]
            newInterval = None
            break

        if s1 <= e2 and s2 <= e1:
            newInterval = [min(s1, s2), max(e1, e2)]
        else:
            ans.append(intervals[i])

        i += 1

    if newInterval:
        ans.append(newInterval)

    return ans


print(insert([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])
print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
      [[1, 2], [3, 10], [12, 16]])

# 1   5
#  2 4
