# Expressive Words
# https://leetcode.com/problems/expressive-words/
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


def expressiveWords(S: str, words: List[str]) -> int:
    ans = 0

    def check(s, w):
        i, j, n, m = 0, 0, len(s), len(w)

        for i in range(n):
            if j < m and s[i] == w[j]:
                j += 1
            elif s[i - 1:i + 2] != s[i] * 3 != s[i - 2:i + 1]:
                return False

        return j == m

    for w in words:
        if check(S, w):
            ans += 1

    return ans


print(expressiveWords("heeellooo", ["hello", "hi", "helo"]), 1)
