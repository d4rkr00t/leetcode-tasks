# Split Array Largest Sum
# https://leetcode.com/problems/split-array-largest-sum/
# hard
#
# Tags: Google, Amazon, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def splitArray(nums: List[int], m: int) -> int:
    l = max(nums)
    r = sum(nums)
    n = len(nums)
    ans = r

    while l < r:
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


# l = 16
# r = 20
# ans = 21
# mid = 18
# s = 18
# cnt = 2
print(splitArray([7, 2, 5, 10, 8], 2), 18)
