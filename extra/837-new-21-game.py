# New 21 Game
# https://leetcode.com/problems/new-21-game/
# medium
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def new21Game(n: int, k: int, maxPts: int) -> float:
    if k == 0 or n >= k + maxPts:
        return 1.0

    dp = [1.0] + [0.0] * n
    wSum = 1

    for i in range(1, n + 1):
        dp[i] = wSum / maxPts
        if i < k:
            wSum += dp[i]

        if i - maxPts >= 0:
            wSum -= dp[i - maxPts]

    return sum(dp[k:])


print(new21Game(n=11, k=6, maxPts=10), 0.86631)
# print(new21Game(n=10, k=6, maxPts=10), 0.80525)
# print(new21Game(n=10, k=1, maxPts=10), 1.0)
# print(new21Game(n=6, k=1, maxPts=10), 0.6)
# print(new21Game(n=21, k=17, maxPts=10), 0.73278)

#
#   1 2 3 4 5 6 7 8 9 10 11
# 0.1
