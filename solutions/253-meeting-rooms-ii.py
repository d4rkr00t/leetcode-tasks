# Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/
# medium
#
# Tags: Amazon, Facebook, Google, Microsoft
#
# Time:  O(n*log(n))
# Space: O(n)
#
# Solution:
# TBD

from typing import List
import heapq


def minMeetingRooms(intervals: List[List[int]]) -> int:
    intervals.sort()
    hq = []
    ans = 0

    for start, end in intervals:
        heapq.heappush(hq, end)
        while hq and hq[0] <= start:
            heapq.heappop(hq)

        ans = max(ans, len(hq))

    return ans


print(minMeetingRooms([[0, 30], [5, 10], [15, 20]]), 2)
print(minMeetingRooms([[7, 10], [2, 4]]), 1)
print(minMeetingRooms([[6, 15], [13, 20], [6, 17]]), 3)
print(minMeetingRooms([[2, 7]]), 1)

# [[6,15],[13,20],[6,17]]
# [[6,15], [6,17], [13,20]]
