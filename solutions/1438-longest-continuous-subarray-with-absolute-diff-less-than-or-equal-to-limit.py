# Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
# medium
#
# Tags: Google, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from collections import deque
from typing import List


def longestSubarray(nums: List[int], limit: int) -> int:
    maxq = deque()
    minq = deque()

    lo = 0
    ans = 0

    for i in range(len(nums)):
        while maxq and nums[maxq[-1]] < nums[i]:
            maxq.pop()

        maxq.append(i)

        while minq and nums[minq[-1]] > nums[i]:
            minq.pop()

        minq.append(i)

        minE = nums[minq[0]]
        maxE = nums[maxq[0]]

        if maxE - minE <= limit:
            ans = max(ans, i - lo + 1)
        else:
            if minq[0] == lo:
                minq.popleft()

            if maxq[0] == lo:
                maxq.popleft()

            lo += 1

    return ans


print(longestSubarray(nums=[8, 2, 4, 7], limit=4), 2)
print(longestSubarray(nums=[10, 1, 2, 4, 7, 2], limit=5), 4)
print(longestSubarray(nums=[4, 2, 2, 2, 4, 4, 2, 2], limit=0), 3)

# 10, 1, 5, 2, 4, 7, 2, 9
#           l           i
#                 mx
#           mn
# max: 9
# min: 9
