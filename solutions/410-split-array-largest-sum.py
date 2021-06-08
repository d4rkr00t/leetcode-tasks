# Split Array Largest Sum
# https://leetcode.com/problems/split-array-largest-sum/
# hard
#
# Tags: Google, Amazon, Facebook
#
# Time:  O(n * log(sumofarr))
# Space: O(1)
#
# Solution:
# TBD

from typing import List


def splitArray(nums: List[int], m: int) -> int:
    l = r = 0
    n = len(nums)

    for i in range(n):
        r += nums[i]

        if l < nums[i]:
            l = nums[i]

    ans = r

    while l <= r:
        mid = (l + r) // 2
        s = 0
        cnt = 1

        for i in range(n):
            if s + nums[i] > mid:
                cnt += 1
                s = nums[i]
            else:
                s += nums[i]

        if cnt <= m:
            ans = min(ans, mid)
            r = mid - 1
        else:
            l = mid + 1

    return ans


print(splitArray([7, 2, 5, 10, 8], 2), 18)
