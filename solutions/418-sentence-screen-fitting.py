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
    s = ' '.join(sentence) + ' '
    start = 0
    for i in range(rows):
        start += cols - 1
        if s[start % len(s)] == ' ':
            start += 1
        elif s[(start + 1) % len(s)] == ' ':
            start += 2
        else:
            while start > 0 and s[(start - 1) % len(s)] != ' ':
                start -= 1

    return start // len(s)


print(wordsTyping(sentence=["hello", "world"], rows=2, cols=8), 1)
print(wordsTyping(sentence=["a", "bcd", "e"], rows=3, cols=6), 2)
print(wordsTyping(sentence=["i", "had", "apple", "pie"], rows=4, cols=5), 1)
print(wordsTyping(sentence=["i"], rows=10, cols=10), 50)
print(wordsTyping(sentence=["f", "p", "a"], rows=8, cols=7), 10)

# f _ p _ a _ f
# p _ a _ f _ p
# a _ f _ p _ a
# - _ _ _ _ _ _
# _ _ _ _ _ _ _
# _ _ _ _ _ _ _
# _ _ _ _ _ _ _
# _ _ _ _ _ _ _
