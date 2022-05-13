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
    chars = set(time)

    def isValid(hh, mm):
        for ch in hh + mm:
            if ch not in chars:
                return False

        return True

    hh_s, mm_s = time.split(":")
    hh = int(hh_s)
    mm = int(mm_s)

    while True:
        carry, mm = divmod(mm + 1, 60)
        hh = (hh + carry) % 24
        hh_s = str(hh).zfill(2)
        mm_s = str(mm).zfill(2)

        if isValid(hh_s, mm_s):
            return hh_s + ":" + mm_s


print(nextClosestTime("19:34"), "19:39")
print(nextClosestTime("23:59"), "22:22")
