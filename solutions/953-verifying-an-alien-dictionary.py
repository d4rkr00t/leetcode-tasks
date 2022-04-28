# Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/
# easy
#
# Tags: Facebook, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from operator import eq
from typing import List


def isAlienSorted(words: List[str], order: str) -> bool:
    if not words:
        return True

    odict = {}
    for i, ch in enumerate(order):
        odict[ch] = i

    cw = words[0]
    for i in range(1, len(words)):
        nw = words[i]
        equal = False

        for c1, c2 in zip(cw, nw):
            if odict[c1] == odict[c2]:
                equal = True
                continue
            elif odict[c1] > odict[c2]:
                return False

            equal = False
            break

        if equal and len(cw) > len(nw):
            return False

        cw = nw

    return True


print(
    isAlienSorted(words=["hello", "leetcode"],
                  order="hlabcdefgijkmnopqrstuvwxyz"), True)
print(
    isAlienSorted(words=["word", "world", "row"],
                  order="worldabcefghijkmnpqstuvxyz"), False)
print(
    isAlienSorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz"),
    False)
