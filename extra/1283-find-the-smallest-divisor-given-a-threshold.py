# Find the Smallest Divisor Given a Threshold
# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
# medium
#
# Tags: Amazon
#
# Time:  O(N*log(max(N)))
# Space: O(1)
#
# Solution:
# Binary Search

from typing import List
from math import ceil


def smallestDivisor(nums: List[int], threshold: int) -> int:
    nums.sort()

    def compute_sum(x):
        return sum([ceil(n/x) for n in nums])

    left, right = 1, nums[-1]

    while left <= right:
        pivot = (right + left) >> 1
        num = compute_sum(pivot)

        if num > threshold:
            left = pivot + 1
        else:
            right = pivot - 1

    return left


print(smallestDivisor(nums=[2, 3, 5, 7, 11], threshold=11), 3)
print(smallestDivisor(nums=[1, 2, 5, 9], threshold=6), 5)
print(smallestDivisor(nums=[19], threshold=5), 4)

"""
1
1 + 2 + 5 + 9 = 17

2
1 + 1 + 3 + 5 = 10

3
1 + 1 + 2 + 3 = 7

4
1 + 1 + 2 + 2 = 6
"""
