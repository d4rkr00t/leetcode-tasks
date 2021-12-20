# Number of Matching Subsequences
# https://leetcode.com/problems/number-of-matching-subsequences/
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
from collections import defaultdict


def numMatchingSubseq(s: str, words: List[str]) -> int:
    buckets = defaultdict(list)
    ans = 0

    for w in words:
        buckets[w[0]].append(w)

    for ch in s:
        nb = []
        while buckets[ch]:
            w = buckets[ch].pop(0)
            if w == ch:
                ans += 1
            elif len(w) > 1 and w[0] == ch:
                nw = w[1:]
                if nw[0] == ch:
                    nb.append(nw)
                else:
                    buckets[nw[0]].append(nw)
        buckets[ch].extend(nb)

    return ans


print(numMatchingSubseq(s="abcde", words=["a", "bb", "acd", "ace"]), 3)
print(
    numMatchingSubseq(s="dsahjpjauf",
                      words=["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]), 2)

# abcde
#       a
#    b c d e
# c d e
