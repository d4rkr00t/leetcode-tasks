# Stone Game III
# https://leetcode.com/problems/stone-game-iii/
# hard
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def stoneGameIII(stoneValue: List[int]) -> str:
    n = len(stoneValue)
    dp = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        dp[i] = float("-inf")
        s = 0
        for j in range(i, min(n, i + 3)):
            s += stoneValue[j]
            dp[i] = max(dp[i], s - dp[j + 1])

    diff = dp[0]

    if diff == 0:
        return "Tie"

    return "Alice" if diff > 0 else "Bob"


print(stoneGameIII([1, 2, 3, 7]), "Bob")
print(stoneGameIII([1, 2, 3, -9]), "Alice")
print(stoneGameIII([1, 2, 3, 6]), "Tie")

#  1  2   3   7
# -1 12  10  7
#
