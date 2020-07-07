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


def threeSum(nums: [int]) -> [[int]]:
    res = []
    found = set()
    for i, n1 in enumerate(nums):
        seen = set()
        for n2 in nums[i+1:]:
            c = -n1 - n2
            if c in seen:
                min_val = min([n1, n2, c])
                max_val = max([n1, n2, c])

                if (min_val, max_val) not in found:
                    found.add((min_val, max_val))
                    res.append([n1, n2, c])

            seen.add(n2)

    return res


print(threeSum([-1, 0, 1, 2, -1, -4]), [
    [-1, 0, 1],
    [-1, -1, 2]
])
