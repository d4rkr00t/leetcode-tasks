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


def isAlienSorted(words: [str], order: str) -> bool:
    ordr = {key: value for value, key in enumerate(order)}

    for i in range(1, len(words)):
        w1 = words[i-1]
        w2 = words[i]

        j = 0
        while j < min(len(w1), len(w2)):
            if ordr[w1[j]] > ordr[w2[j]]:
                return False
            if ordr[w1[j]] != ordr[w2[j]]:
                break

            j += 1

        if j == len(w2) and len(w1) > len(w2):
            return False

    return True


print(isAlienSorted(words=["hello", "leetcode"],
                    order="hlabcdefgijkmnopqrstuvwxyz"), True)
print(isAlienSorted(words=["word", "world", "row"],
                    order="worldabcefghijkmnpqstuvxyz"), False)
print(isAlienSorted(words=["apple", "app"],
                    order="abcdefghijklmnopqrstuvwxyz"), False)
