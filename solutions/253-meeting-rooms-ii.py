# Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/
# medium
#
# Tags: Amazon, Facebook, Google, Microsoft
#
# Time:  O(n*log(n))
# Space: O(n)

from operator import itemgetter

def minMeetingRooms(intervals: [[int]]) -> int:
    if not intervals: return 0

    start_times = list(sorted(map(itemgetter(0), intervals)))
    end_times = list(sorted(map(itemgetter(1), intervals)))

    ep = sp = 0
    rooms = 0

    while sp < len(intervals):
        if start_times[sp] >= end_times[ep]:
            rooms -= 1
            ep += 1

        rooms += 1
        sp += 1

    return rooms


print(minMeetingRooms([[0, 30],[5, 10],[15, 20]]), 2)
print(minMeetingRooms([[7,10],[2,4]]), 1)
