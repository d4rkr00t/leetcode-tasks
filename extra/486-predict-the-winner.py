# Predict the Winner
# https://leetcode.com/problems/predict-the-winner/
# medium
#
# Tags: Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def PredictTheWinner(nums: List[int]) -> bool:
    dp = [num for num in nums]
    for length in range(2, len(nums) + 1):
        for j in range(len(nums) - length + 1):
            dp[j] = max(nums[j] - dp[j + 1], nums[j + length - 1] - dp[j])
    return dp[0] >= 0


print(PredictTheWinner([1, 5, 2]), False)
print(PredictTheWinner([1, 5, 233, 7]), True)

"""
[1, 5, 233, 2, 3, 7]
[5, 233, 7]
[5, 233]
[5]
[]
"""
