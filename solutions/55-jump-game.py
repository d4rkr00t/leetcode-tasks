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
        if i > can_reach:
            return False

        can_reach = max(can_reach, i + n)

    return True


print(canJump([2, 3, 1, 1, 4]))
print(canJump([3, 2, 1, 0, 4]))
print(canJump([0]))
