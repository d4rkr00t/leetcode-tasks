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
# def isBadVersion(version):

def firstBadVersion(n: int):
    lo = 0
    hi = n
    bad = n

    while lo <= hi:
        mid = (lo + hi) // 2

        if isBadVersion(mid):
            hi = mid - 1
            bad = min(mid, bad)
        else:
            lo = mid + 1

    return bad
