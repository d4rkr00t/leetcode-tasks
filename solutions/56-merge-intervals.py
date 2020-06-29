# Merge Intervals
# https://leetcode.com/problems/merge-intervals/
# medium
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def merge(intervals: [[int]]) -> [[int]]:
    if not intervals: return []
    intervals = list(sorted(intervals))
    ans = [intervals[0]]

    for i in range(1, len(intervals)):
        intr = intervals[i]
        cur = ans[-1]

        if cur[0] <= intr[1] and cur[1] >= intr[0]:
            ans[-1] = [min(cur[0], intr[0]), max(cur[1], intr[1])]
        else:
            ans.append(intr)

    return ans


print(merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
print(merge([[1,4],[4,5]]), [[1,5]])
