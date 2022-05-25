# 3Sum
# https://leetcode.com/problems/3sum/
# medium
#
# Tags: Amazon, Facebook, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    ans = []
    numsLen = len(nums)
    nums.sort()

    for i in range(numsLen):
        if i == 0 or nums[i - 1] != nums[i]:
            prevNums = set()
            ni = nums[i]

            j = i + 1
            while j < numsLen:
                nj = nums[j]
                tmp = -ni - nj
                if tmp in prevNums:
                    ans.append([ni, nj, tmp])

                    while j + 1 < numsLen and nums[j] == nums[j + 1]:
                        j += 1

                prevNums.add(nj)
                j += 1

    return ans


print(threeSum([-1, 0, 1, 2, -1, -4]), [[-1, 0, 1], [-1, -1, 2]])
