# Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/
# easy
#
# Tags: Facebook, Amazon
#
# Time:  O(N*M)
# Space: O(order)

from typing import List


def isAlienSorted(words: List[str], order: str) -> bool:
    if not words or len(words) == 1:
        return True

    pos = {order[i]: i for i in range(len(order))}
    prev = words[0]
    for i in range(1, len(words)):
        cur = words[i]
        allMached = True
        for c1, c2 in zip(prev, cur):
            if c1 != c2:
                allMached = False

            if pos[c1] > pos[c2]:
                return False
            elif c1 != c2:
                break

        if allMached and len(prev) > len(cur):
            return False

        prev = cur

    return True


print(isAlienSorted(words=["hello", "leetcode"],
                    order="hlabcdefgijkmnopqrstuvwxyz"), True)
print(isAlienSorted(words=["word", "world", "row"],
                    order="worldabcefghijkmnpqstuvxyz"), False)
print(isAlienSorted(words=["apple", "app"],
                    order="abcdefghijklmnopqrstuvwxyz"), False)
