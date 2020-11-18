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

from collections import Counter


def getHint(secret: str, guess: str) -> str:
    A = 0
    B = 0
    cc = Counter(secret)
    maybe_cows = []

    for s_c, g_c in zip(secret, guess):
        if s_c == g_c:
            A += 1
            cc[s_c] -= 1
        elif cc[g_c] > 0:
            maybe_cows.append(g_c)

    for c in maybe_cows:
        if cc[c] > 0:
            B += 1
            cc[c] -= 1

    return str(A) + "A" + str(B) + "B"


print(getHint(secret="1807", guess="7810"), "1A3B")
print(getHint(secret="1123", guess="0111"), "1A1B")
