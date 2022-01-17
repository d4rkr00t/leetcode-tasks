# Word Squares
# https://leetcode.com/problems/word-squares/
# hard
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List
from collections import defaultdict


def wordSquares(words: List[str]) -> List[List[str]]:
    prefixes = defaultdict(list)
    ans = []

    for w in words:
        for i in range(len(w)):
            prefixes[w[:i + 1]].append(w)

    def backtrack(wlist, pos):
        if pos == len(wlist[0]):
            ans.append([] + wlist)
            return

        pref = ""
        for w in wlist:
            pref += w[pos]

        for w in prefixes[pref]:
            wlist.append(w)
            backtrack(wlist, pos + 1)
            wlist.pop()

    for w in words:
        wlist = [w]
        backtrack(wlist, 1)

    return ans


print(wordSquares(["area", "lead", "wall", "lady", "ball"]),
      [["wall", "area", "lead", "lady"], ["ball", "area", "lead", "lady"]])

print(wordSquares(["abat", "baba", "atan", "atal"]),
      [["baba", "abat", "baba", "atan"], ["baba", "abat", "baba", "atal"]])
