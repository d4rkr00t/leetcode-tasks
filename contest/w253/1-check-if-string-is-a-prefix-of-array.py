# Check If String Is a Prefix of Array
#
# easy
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def isPrefixString(s: str, words: List[str]) -> bool:
    pos = 0

    for w in words:
        if not s.startswith(w, pos):
            return False

        pos += len(w)

        if pos >= len(s):
            return True

    return True if pos >= len(s) else False


print(
    isPrefixString(s="iloveleetcode",
                   words=["i", "love", "leetcode", "apples"]), True)
print(
    isPrefixString(s="iloveleetcode",
                   words=["i", "apples", "leetcode", "apples"]), False)

print(isPrefixString(s="ccccccccccc", words=["c", "cc"]), False)
