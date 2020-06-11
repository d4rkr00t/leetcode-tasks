# 3Sum
# https://leetcode.com/problems/3sum/
# medium
#
# Tags: Amazon, Facebook, Google
#
# Time: O(n^2)
# Space: O(n^2)
#
# Solution:
# TBD

def threeSum(nums: [int]) -> [[int]]:
    res = []
    found, dups = set(), set()

    for i, val1 in enumerate(nums):
        seen = set()

        if val1 not in dups:
            dups.add(val1)

            for j, val2 in enumerate(nums[i+1:]):
                complement = -val1 - val2
                if complement in seen:
                    min_val = min(val1, val2, complement)
                    max_val = max(val1, val2, complement)

                    if (min_val, max_val) not in found:
                        found.add((min_val, max_val))
                        res.append([val1, val2, complement])

                seen.add(val2)

    return res

print(threeSum([-1, 0, 1, 2, -1, -4]), [
    [-1, 0, 1],
    [-1, -1, 2]
])
