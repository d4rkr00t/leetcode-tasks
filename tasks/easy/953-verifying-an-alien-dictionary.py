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
    pass


print(isAlienSorted(words=["hello", "leetcode"],
                    order="hlabcdefgijkmnopqrstuvwxyz"), True)
print(isAlienSorted(words=["word", "world", "row"],
                    order="worldabcefghijkmnpqstuvxyz"), False)
print(isAlienSorted(words=["apple", "app"],
                    order="abcdefghijklmnopqrstuvwxyz"), False)
