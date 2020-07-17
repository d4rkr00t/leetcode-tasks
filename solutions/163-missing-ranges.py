# Missing Ranges
# https://leetcode.com/problems/missing-ranges/
# medium
#
# Tags: Amazon, Facebook, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def findMissingRanges(nums: [int], lower: int, upper: int) -> [str]:
    missing = []
    nums = nums or []

    lo = lower - 1

    for n in nums + [upper+1]:
        if n - lo == 2:
            missing.append(str(n-1))
        elif n - lo > 2:
            missing.append(str(lo+1) + "->" + str(n-1))

        lo = n

    return missing


print(findMissingRanges([0, 1, 3, 50, 75], 0, 99),
      ["2", "4->49", "51->74", "76->99"])

print(findMissingRanges([], 1, 1))
