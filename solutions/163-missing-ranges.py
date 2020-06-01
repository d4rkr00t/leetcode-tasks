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
    if nums[-1] != upper: nums.append(upper+1)

    ans = []
    prev = lower - 1
    for n in nums:
        dist = n - prev

        if dist > 2:
            ans.append(str(prev + 1) + "->" + str(n-1))
        elif dist == 2:
            ans.append(str((n + prev) // 2))

        prev = n

    return ans

print(findMissingRanges([0, 1, 3, 50, 75], 0, 99), ["2", "4->49", "51->74", "76->99"])
