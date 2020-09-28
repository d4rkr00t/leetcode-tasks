# Jump Game
# https://leetcode.com/problems/jump-game/
# medium
#
# Tags: Amazon, Facebook, Google
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# TBD

from typing import List


def canJump(nums: List[int]) -> bool:
    can_reach = 0

    for i, n in enumerate(nums):
        can_reach = max(can_reach, i + n)
        if can_reach == i and i != len(nums) - 1:
            return False

    return True


print(canJump([2, 3, 1, 1, 4]))
print(canJump([3, 2, 1, 0, 4]))
print(canJump([2, 3, 1, 1, 0]))
