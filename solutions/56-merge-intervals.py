# Merge Intervals
# https://leetcode.com/problems/merge-intervals/
# medium
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  O(n * log(n))
# Space: O(n)

def merge(intervals: [[int]]) -> [[int]]:
    intervals.sort()

    merged = []
    cur = None

    for start, end in intervals:
        if not cur:
            cur = [start, end]
            continue

        if start > cur[1]:
            merged.append(cur)
            cur = [start, end]
        else:
            cur = [min(start, cur[0]), max(end, cur[1])]

    if cur:
        merged.append(cur)

    return merged

print(merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
print(merge([[1,4],[4,5]]), [[1,5]])
