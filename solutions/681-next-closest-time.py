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
    hh_s, mm_s = time.split(":")
    digits = set(hh_s + mm_s)

    def check(time):
        for ch in time:
            if ch not in digits:
                return False

        return True

    hh = int(hh_s)
    mm = int(mm_s)
    while True:
        carry, mm = divmod(mm + 1, 60)
        hh = (hh + carry) % 24
        hh_s = str(hh).zfill(2)
        mm_s = str(mm).zfill(2)
        time = hh_s + ":" + mm_s
        if check(hh_s + mm_s):
            return time


print(nextClosestTime("19:34"), "19:39")
print(nextClosestTime("23:59"), "22:22")
