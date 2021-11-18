# Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
# medium
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List
import collections


def longestSubarray(nums: List[int], limit: int) -> int:
    minq = collections.deque()
    maxq = collections.deque()

    ans = 0
    l = 0
    for r in range(len(nums)):
        while maxq and nums[maxq[-1]] < nums[r]:
            maxq.pop()

        maxq.append(r)

        while minq and nums[minq[-1]] > nums[r]:
            minq.pop()

        minq.append(r)

        minE = nums[minq[0]]
        maxE = nums[maxq[0]]

        if abs(minE - maxE) <= limit:
            ans = max(ans, r - l + 1)
        else:
            if l == maxq[0]:
                maxq.popleft()
            if l == minq[0]:
                minq.popleft()

            l += 1

    return ans


print(longestSubarray(nums=[8, 2, 4, 7], limit=4), 2)
print(longestSubarray(nums=[10, 1, 2, 4, 7, 2], limit=5), 4)
print(longestSubarray(nums=[4, 2, 2, 2, 4, 4, 2, 2], limit=0), 3)

# 8 2 4 7
#   l
#       r
# minq = [1,2]
# maxq = [2]
# diff = 4-2 = 2
# limit = 4
# ans = 2
