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
    table = {}
    for i, ch in enumerate(order):
        table[ch] = i

    prev = words[0]

    for i in range(1, len(words)):
        cur = words[i]

        for ch1, ch2 in zip(prev, cur):
            if table[ch1] > table[ch2]:
                return False
            if table[ch1] < table[ch2]:
                break
        else:
            if len(prev) > len(cur):
                return False

        prev = cur

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
