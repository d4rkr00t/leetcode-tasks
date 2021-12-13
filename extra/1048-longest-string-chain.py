# Longest String Chain
# https://leetcode.com/problems/longest-string-chain/
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


def longestStrChain(words: List[str]) -> int:
    table = {}
    processed = set()
    ans = 0

    for w in words:
        table[w] = 0

    def process(w):
        if w in processed:
            return table[w]

        processed.add(w)
        res = 0

        for i in range(len(w)):
            tmp = w[:i] + w[i + 1:]
            if tmp not in table:
                continue

            res = max(process(tmp), res)

        table[w] = res + 1
        return table[w]

    for w in words:
        if w not in processed:
            ans = max(ans, process(w))

    return ans


print(longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]), 4)
print(longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]), 5)
print(longestStrChain(["abcd", "dbqca"]), 1)

# a b ba bca bda bdca
# a -> ""
# b -> ""
# ba -> b -> ""
# bca -> ba -> ...
#
