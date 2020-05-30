# Next Closest Time
# https://leetcode.com/problems/next-closest-time/
# medium
#
# Tags: Google, Microsoft
#
# Time:  O(1) 4*4*4*4
# Space: O(1)
#
# Solution:
# exaust all posibilities

import itertools

def nextClosestTime(time: str) -> str:
    ans = start = 60 * int(time[:2]) + int(time[3:])
    elapsed = 24 * 60
    allowed = [int(x) for x in time if x != ":"]

    for h1,h2,m1,m2 in itertools.product(allowed, repeat = 4):
        hours, minutes = 10 * h1 + h2, 10 * m1 + m2

        if hours < 24 and minutes < 60:
            cur = hours * 60 + minutes
            cand_elapsed = (cur - start) % (24 * 60)

            if 0 < cand_elapsed < elapsed:
                elapsed = cand_elapsed
                ans = cur

    return "{:02d}:{:02d}".format(*divmod(ans, 60))


print(nextClosestTime("19:34"), "19:39")
print(nextClosestTime("23:59"), "22:22")
