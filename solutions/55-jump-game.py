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

def canJump(nums: [int]) -> bool:
    last = len(nums) - 1

    for i in range(len(nums))[::-1]:
        n = nums[i]
        if i + n >= last:
            last = i

    return last == 0

print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))
