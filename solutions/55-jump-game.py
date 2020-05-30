# Jump Game
# https://leetcode.com/problems/jump-game/
# medium
#
# Tags: Amazon, Facebook, Google
#
# Time:  O(n)
# Space: O(1)

def canJump(nums: [int]) -> bool:
    last = len(nums) - 1
    for i in range(len(nums))[::-1]:
        if i + nums[i] >= last: last = i

    return last == 0

print(canJump([2,3,1,1,4]), True)
print(canJump([3,2,1,0,4]), False)

#   |         |
# 3,5,2,0,4,0,1
