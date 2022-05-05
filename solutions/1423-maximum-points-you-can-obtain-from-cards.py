# Maximum Points You Can Obtain from Cards
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
# medium
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def maxScore(cardPoints: List[int], k: int) -> int:
    if not list or k == 0:
        return 0

    if k == len(cardPoints):
        return sum(cardPoints)

    lo = 0
    hi = k - 1
    tmp = sum(cardPoints[lo:hi + 1])
    ans = tmp

    for _ in range(1, k + 1):
        tmp -= cardPoints[hi]
        lo = lo - 1
        hi = hi - 1
        tmp += cardPoints[lo]

        ans = max(ans, tmp)

    return ans


#                          hi             lo
print(maxScore(cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3), 12)
print(maxScore(cardPoints=[2, 2, 2], k=2), 4)
print(maxScore(cardPoints=[9, 7, 7, 9, 7, 7, 9], k=7), 55)
print(maxScore(cardPoints=[1, 1000, 1], k=1), 1)
print(maxScore(cardPoints=[1, 79, 80, 1, 1, 1, 200, 1], k=3), 202)
