# Maximum Number of Words You Can Type
# https://leetcode.com/contest/weekly-contest-250/problems/maximum-number-of-words-you-can-type/
# easy
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from collections import Counter


def canBeTypedWords(text: str, brokenLetters: str) -> int:
    m = Counter(brokenLetters)
    ans = 0

    for w in text.split(" "):
        for ch in w:
            if ch in m:
                break
        else:
            ans += 1

    return ans


print(canBeTypedWords(text="hello world", brokenLetters="ad"))
print(canBeTypedWords(text="leet code", brokenLetters="e"))
