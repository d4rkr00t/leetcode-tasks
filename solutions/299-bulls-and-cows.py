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
    table = collections.defaultdict(int)

    bulls = 0
    for i,c in enumerate(secret):
        if c == guess[i]:
            bulls += 1
        else:
            table[c] += 1

    cows = 0

    for i,c in enumerate(guess):
        if c == secret[i]:
            continue

        if c in table and table[c] > 0:
            cows += 1
            table[c] -= 1

    return str(bulls) + "A" + str(cows) + "B"

print(getHint(secret = "1807", guess = "7810"), "1A3B")
print(getHint(secret = "1123", guess = "0111"), "1A1B")
print(getHint(secret = "1122", guess = "1222"), "3A0B")
