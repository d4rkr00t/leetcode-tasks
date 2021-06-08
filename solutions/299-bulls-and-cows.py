# Bulls and Cows
# https://leetcode.com/problems/bulls-and-cows/
# medium
#
# Tags: Google, Microsoft
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# TBD

import collections


def getHint(secret: str, guess: str) -> str:
    A = 0
    B = 0
    cc = collections.Counter()
    for sc, gc in zip(secret, guess):
        if sc == gc:
            A += 1
        else:
            cc[sc] += 1

    for gc in guess:
        if cc[gc] > 0:
            B += 1
        cc[gc] -= 1

    return str(A) + "A" + str(B) + "B"


print(getHint(secret="1807", guess="7810"), "1A3B")
print(getHint(secret="1123", guess="0111"), "1A1B")
