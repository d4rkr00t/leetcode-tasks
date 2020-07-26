# Insert Interval
# https://leetcode.com/problems/insert-interval/
# hard
#
# Tags: Google, Facebook, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def insert(intervals: [[int]], newInterval: [int]) -> [[int]]:
    copy = []
    cur = newInterval
    i = 0
    for intr in intervals:
        if intr[0] > cur[1]:
            copy.append(cur)
            break

        if intr[0] <= cur[1] and intr[1] >= cur[0]:
            cur = [min(intr[0], cur[0]), max(cur[1], intr[1])]
        else:
            copy.append(intr)

        i += 1

    copy += intervals[i:]

    return copy


print(insert([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])
print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
             [4, 8]), [[1, 2], [3, 10], [12, 16]])
