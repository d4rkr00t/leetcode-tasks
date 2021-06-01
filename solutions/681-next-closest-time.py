# Next Closest Time
# https://leetcode.com/problems/next-closest-time/
# medium
#
# Tags: Google, Microsoft
#
# Time:  O(1)
# Space: O(1)
#
# Solution:
# Simulation


def nextClosestTime(time: str) -> str:
    hour, minute = time.split(":")
    nums = set(hour + minute)
    mm = int(minute)
    hh = int(hour)

    while True:
        d, mm = divmod(mm + 1, 60)
        hh = (hh + d) % 24

        mm_s = str(mm).zfill(2)
        hh_s = str(hh).zfill(2)

        for n in hh_s + mm_s:
            if n not in nums:
                break
        else:
            return hh_s + ":" + mm_s


print(nextClosestTime("19:34"), "19:39")
print(nextClosestTime("23:59"), "22:22")
