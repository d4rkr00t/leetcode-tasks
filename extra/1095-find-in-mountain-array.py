# Find in Mountain Array
# https://leetcode.com/problems/find-in-mountain-array/
# hard
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

class MountainArray:
    def get(self, index: int) -> int:
        pass

    def length(self) -> int:
        pass


class Solution:
    def findInMountainArray(self, target: int, A: MountainArray) -> int:
        n = A.length()
        # find index of peak
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if A.get(m) < A.get(m + 1):
                l = peak = m + 1
            else:
                r = m
        # find target in the left of peak
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            if A.get(m) < target:
                l = m + 1
            elif A.get(m) > target:
                r = m - 1
            else:
                return m

        # find target in the right of peak
        l, r = peak, n - 1
        while l <= r:
            m = (l + r) // 2
            if A.get(m) > target:
                l = m + 1
            elif A.get(m) < target:
                r = m - 1
            else:
                return m
        return -1


"""
[1,2,3,4,5,3,1]
[4,5,3,2,1]
[2,4,5,3,2,1]
"""
