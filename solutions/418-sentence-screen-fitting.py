# Sentence Screen Fitting
# https://leetcode.com/problems/sentence-screen-fitting/
# medium
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def wordsTyping(sentence: List[str], rows: int, cols: int) -> int:
    curRow = curCol = curWord = times = 0

    while curRow < rows:
        w = sentence[curWord]
        if len(w) + curCol >= cols:
            curCol = 0
            curRow += 1
        curCol += len(w) + 1
        curWord += 1
        if curWord == len(sentence):
            times += 1
            curWord = 0

    return times


print(wordsTyping(sentence=["hello", "world"], rows=2, cols=8), 1)
print(wordsTyping(sentence=["a", "bcd", "e"], rows=3, cols=6), 2)
print(wordsTyping(sentence=["i", "had", "apple", "pie"], rows=4, cols=5), 1)
