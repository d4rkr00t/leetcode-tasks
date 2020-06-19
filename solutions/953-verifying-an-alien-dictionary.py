# Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/
# easy
#
# Tags: Facebook, Amazon
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# TBD

def isAlienSorted(words: [str], order: str) -> bool:
    priority = [0] * 26
    for i,c in enumerate(order):
        priority[ord(c) - ord("a")] = i

    for i in range(1, len(words)):
        w1 = words[i-1]
        w2 = words[i]

        for i in range(min(len(w1), len(w2))):
            p1 = priority[ord(w1[i]) - ord("a")]
            p2 = priority[ord(w2[i]) - ord("a")]
            if p1 < p2:
                break
            if p1 > p2:
                return False

            if i+1 == min(len(w1), len(w2)) and len(w1) > len(w2):
                return False

    return True

print(isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"), True)
print(isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"), False)
print(isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"), False)
