# First Bad Version
# https://leetcode.com/problems/first-bad-version/
# easy
#
# Tags: Facebook, Google, Microsoft
#
# Time:  O(log(N))
# Space: O(1)
#
# Solution:
# TBD

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

def firstBadVersion(n: int):
    lo = 1
    hi = n
    prev = float("inf")

    while lo <= hi:
        mid = (lo + hi) // 2

        is_bad = isBadVersion(mid)

        if is_bad:
            prev = min(prev, mid)
            hi = mid-1
        else:
            lo = mid+1

    return prev if prev < float("inf") else -1

