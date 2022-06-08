# First Bad Version
# https://leetcode.com/problems/first-bad-version/
# easy
#
# Tags: Facebook, Google, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    pass


def firstBadVersion(n: int):
    lo = 0
    hi = n
    while lo < hi:
        mid = (hi + lo) // 2
        if isBadVersion(mid):
            hi = mid
        else:
            lo = mid + 1

    return hi
