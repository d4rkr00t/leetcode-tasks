# Word Squares
# https://leetcode.com/problems/word-squares/
# hard
#
# Tags: Google
#
# Time:  O(n^2 + 26^L)
# Space: O(n*l)

from typing import List


def wordSquares(words: List[str]) -> List[List[str]]:
    prefixes = {}
    ans = []

    def backtrack(w, col, cur):
        if len(cur) == len(w):
            ans.append([] + cur)
            return

        prefix = "".join([s[col] for s in cur])

        for nei in prefixes.get(prefix, []):
            cur.append(nei)
            backtrack(w, col + 1, cur)
            cur.pop()

    for w in words:
        for i in range(1, len(w) + 1):
            prefixes[w[:i]] = prefixes.get(w[:i], [])
            prefixes[w[:i]].append(w)

    for w in words:
        backtrack(w, 1, [w])

    return ans


# w a l l
# a r e a
# l e a d
# l a d y

# { a: ["area"], "ar": ["area"], "are": ["area"],  }

print(wordSquares(["area", "lead", "wall", "lady", "ball"]),
      [["wall", "area", "lead", "lady"], ["ball", "area", "lead", "lady"]])

print(wordSquares(["abat", "baba", "atan", "atal"]),
      [["baba", "abat", "baba", "atan"], ["baba", "abat", "baba", "atal"]])
