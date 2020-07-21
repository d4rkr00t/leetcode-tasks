# Bulls and Cows
# https://leetcode.com/problems/bulls-and-cows/
# easy
#
# Tags: Google, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

import collections


def getHint(secret: str, guess: str) -> str:
    A = 0
    B = 0
    secret_set = collections.Counter()
    for c1, c2 in zip(secret, guess):
        if c1 != c2:
            secret_set[c1] += 1

    for c1, c2 in zip(secret, guess):
        if c1 == c2:
            A += 1
        elif c2 in secret_set and secret_set[c2] > 0:
            secret_set[c2] -= 1
            B += 1

    return str(A) + "A" + str(B) + "B"


print(getHint(secret="1807", guess="7810"), "1A3B")
print(getHint(secret="1123", guess="0111"), "1A1B")
