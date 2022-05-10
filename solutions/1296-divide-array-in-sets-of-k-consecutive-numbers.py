# Divide Array in Sets of K Consecutive Numbers
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
# medium
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

import collections
from typing import List


def isPossibleDivide(nums: List[int], k: int) -> bool:
    if len(nums) % k == 1:
        return False

    counter = collections.Counter(nums)
    nums.sort()
    for n in nums:
        if counter[n] == 0:
            continue

        counter[n] -= 1
        for i in range(1, k):
            if counter[n + i] == 0:
                return False

            counter[n + i] -= 1

    return True


print(isPossibleDivide(nums=[1, 2, 3, 3, 4, 4, 5, 6], k=4), True)
print(isPossibleDivide(nums=[3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], k=3), True)
print(isPossibleDivide(nums=[1, 2, 3, 4], k=3), False)
