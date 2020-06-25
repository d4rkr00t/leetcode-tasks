# Two Sum II - Input array is sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
# easy
#
# Tags: Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def twoSum(numbers: [int], target: int) -> [int]:
    if not numbers:
        return []

    lo = 0
    hi = len(numbers) - 1

    while lo < hi:
        sum = numbers[lo] + numbers[hi]

        if sum == target:
            return [lo+1, hi+1]

        if sum > target:
            hi -= 1
        else:
            lo += 1

    return []

print(twoSum(numbers = [2,7,11,15], target = 9), [1,2])
