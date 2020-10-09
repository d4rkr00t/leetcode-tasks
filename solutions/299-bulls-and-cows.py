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

from collections import Counter


def getHint(secret: str, guess: str) -> str:
    s_c = Counter()
    A = 0
    B = 0

    for i, c in enumerate(guess):
        if secret[i] == c:
            A += 1
        else:
            s_c[secret[i]] += 1

    for i, c in enumerate(guess):
        if secret[i] != c and c in s_c and s_c[c] > 0:
            B += 1
            s_c[c] -= 1

    return str(A) + "A" + str(B) + "B"


print(getHint(secret="1807", guess="7810"), "1A3B")
print(getHint(secret="1123", guess="0111"), "1A1B")
