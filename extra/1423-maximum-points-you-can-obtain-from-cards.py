# Maximum Points You Can Obtain from Cards
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
# medium
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def maxScore(cardPoints: List[int], k: int) -> int:
    total = sum(cardPoints)
    hi = len(cardPoints) - k
    subtotal = sum([cardPoints[x] for x in range(hi)])
    ans = total - subtotal
    lo = 0

    while hi < len(cardPoints):
        subtotal -= cardPoints[lo]
        subtotal += cardPoints[hi]
        lo += 1
        hi += 1
        ans = max(ans, total - subtotal)

    return ans


print(maxScore(cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3), 12)
print(maxScore(cardPoints=[2, 2, 2], k=2), 4)
print(maxScore(cardPoints=[9, 7, 7, 9, 7, 7, 9], k=7), 55)
print(maxScore(cardPoints=[1, 1000, 1], k=1), 1)
print(maxScore(cardPoints=[1, 79, 80, 1, 1, 1, 200, 1], k=3), 202)

# 1, 2, 3, 4, 5, 6, 1
# |        |
