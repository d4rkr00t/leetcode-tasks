# Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/
# medium
#
# Tags: Amazon, Facebook, Google, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List
import heapq


def minMeetingRooms(intervals: List[List[int]]) -> int:
    hq = []
    ans = 0
    intervals.sort()

    for s, e in intervals:
        if hq and hq[0] <= s:
            heapq.heappop(hq)

        heapq.heappush(hq, e)
        ans = max(ans, len(hq))

    return ans


print(minMeetingRooms([[0, 30], [5, 10], [15, 20]]), 2)
print(minMeetingRooms([[7, 10], [2, 4]]), 1)
