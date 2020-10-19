# Next Closest Time
# https://leetcode.com/problems/next-closest-time/
# medium
#
# Tags: Google, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def nextClosestTime(time: str) -> str:
    hh, mm = time.split(":")
    digits = set(hh+mm)
    hh = int(hh)
    mm = int(mm)

    while True:
        d, mm = divmod(mm+1, 60)
        hh = (hh+d) % 24

        mm_s = str(mm).zfill(2)
        hh_s = str(hh).zfill(2)

        for c in hh_s + mm_s:
            if c not in digits:
                break
        else:
            return hh_s + ":" + mm_s


print(nextClosestTime("19:34"), "19:39")
print(nextClosestTime("23:59"), "22:22")
