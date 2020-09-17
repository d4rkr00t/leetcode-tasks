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
import collections


def wordSquares(words: List[str]) -> List[List[str]]:
    prefix_groups = collections.defaultdict(list)

    for w in words:
        for i in range(1, len(w)):
            prefix_groups[w[:i]].append(w)

    ans = []

    def build_sqaure(square, col):
        if len(square[0]) == len(square):
            ans.append([] + square)
            return

        prefix = "".join([w[col] for w in square])

        for w in prefix_groups[prefix]:
            square.append(w)
            build_sqaure(square, col + 1)
            square.pop()

    for w in words:
        build_sqaure([w], 1)

    return ans


print(wordSquares(["area", "lead", "wall", "lady", "ball"]), [
    ["wall",
     "area",
     "lead",
     "lady"],
    ["ball",
     "area",
     "lead",
     "lady"]
])


print(wordSquares(["abat", "baba", "atan", "atal"]), [
    ["baba",
     "abat",
     "baba",
     "atan"],
    ["baba",
     "abat",
     "baba",
     "atal"]
])
