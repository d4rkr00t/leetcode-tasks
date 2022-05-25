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

from collections import defaultdict
from typing import List


def wordSquares(words: List[str]) -> List[List[str]]:
    if not words or len(words[0]) == 1:
        return words

    prefix = defaultdict(list)
    for word in words:
        for i in range(1, len(word)):
            prefix[word[:i]].append(word)

    ans = []

    def backtrack(square, pref):
        if len(square[0]) == len(square):
            ans.append([] + square)
            return

        for nei in prefix[pref]:
            next_pref = ""
            square.append(nei)

            if len(square) < len(square[0]):
                for line in square:
                    next_pref += line[len(square)]

            backtrack(square, next_pref)
            square.pop()

    for word in words:
        backtrack([word], word[1])

    return ans


print(wordSquares(["area", "lead", "wall", "lady", "ball"]),
      [["wall", "area", "lead", "lady"], ["ball", "area", "lead", "lady"]])

print(wordSquares(["abat", "baba", "atan", "atal"]),
      [["baba", "abat", "baba", "atan"], ["baba", "abat", "baba", "atal"]])

# b a l l
# a r e a
# l e a d
# l a d y
