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

import heapq


def minMeetingRooms(intervals: [[int]]) -> int:
    if not intervals:
        return 0

    intervals.sort()
    pq = [intervals.pop(0)[1]]
    rooms = 1

    for intr in intervals:
        if pq[0] < intr[0]:
            heapq.heappop(pq)
        else:
            rooms += 1

        heapq.heappush(pq, intr[1])

    return rooms


print(minMeetingRooms([[0, 30], [5, 10], [15, 20]]), 2)
print(minMeetingRooms([[7, 10], [2, 4]]), 1)
