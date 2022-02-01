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
    nums.sort()
    counter = collections.Counter(nums)
    ans = 0

    for n in nums:
        if counter[n] == 0:
            continue

        counter[n] -= 1
        for inc in range(1, k):
            if counter[inc + n] <= 0:
                return False
            else:
                counter[inc + n] -= 1

        ans += 1

    return ans > 1


print(isPossibleDivide(nums=[1, 2, 3, 3, 4, 4, 5, 6], k=4), True)
print(isPossibleDivide(nums=[3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], k=3), True)
print(isPossibleDivide(nums=[1, 2, 3, 4], k=3), False)

# 3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11
# x  x  x  x  x  x  x  x  x  x  x   x
# 3                    4     9
#   2            4       5
#     1 2 3
#                  3          10   11
#
#
# 1 2 1 5 1 10 9 2 3
# 1 1 1 2 2 3 5 9 10
# 1
#   1
#     1
#
