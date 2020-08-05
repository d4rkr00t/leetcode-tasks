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

from typing import List


def isAlienSorted(words: List[str], order: str) -> bool:
    poss = {c: p for p, c in enumerate(order)}

    if not words:
        return False

    w1 = words[0]
    for i in range(1, len(words)):
        w2 = words[i]

        end = False
        for c1, c2 in zip(w1, w2):
            if poss[c1] == poss[c2]:
                continue
            elif poss[c1] > poss[c2]:
                return False
            else:
                break
        else:
            end = True

        if len(w1) > len(w2) and end:
            return False

        w1 = w2

    return True


print(isAlienSorted(words=["hello", "leetcode"],
                    order="hlabcdefgijkmnopqrstuvwxyz"), True)
print(isAlienSorted(words=["word", "world", "row"],
                    order="worldabcefghijkmnpqstuvxyz"), False)
print(isAlienSorted(words=["apple", "app"],
                    order="abcdefghijklmnopqrstuvwxyz"), False)
