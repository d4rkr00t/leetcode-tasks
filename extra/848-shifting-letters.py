# Shifting Letters
# https://leetcode.com/problems/shifting-letters/
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


def shiftingLetters(s: str, shifts: List[int]) -> str:
    def calc_shift(ch, shifts):
        a = ord("a")
        och = ord(ch)
        return chr((((och - a) + shifts) % 26) + a)

    prev = 0
    s = list(s)
    for i in range(len(s) - 1, -1, -1):
        shifts[i] += prev
        s[i] = calc_shift(s[i], shifts[i])
        prev = shifts[i]

    return "".join(s)


print(shiftingLetters(s="abc", shifts=[3, 5, 9]), "rpl")
print(shiftingLetters(s="aaa", shifts=[1, 2, 3]), "gfd")
print(shiftingLetters(s="bad", shifts=[10, 20, 30]), "jyh")
print(shiftingLetters(s="z", shifts=[1]), "a")
