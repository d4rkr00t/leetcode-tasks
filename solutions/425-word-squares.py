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

def wordSquares(words: [str]) -> [[str]]:
    if not words:
        return []

    if len(words) == 1:
        return words

    table = {}

    for w in words:
        for i in range(1, len(w)):
            pref = w[:i]
            table[pref] = table.get(pref, [])
            table[pref].append(w)

    ans = []
    def backtrack(square, prefix):
        if prefix not in table:
            return

        for w in table[prefix]:
            new_square = [] + square + [w]
            if len(new_square) == len(w):
                ans.append(new_square)
            else:
                pref = "".join([n[len(new_square)] for n in new_square])
                backtrack(new_square, pref)

    for w in words:
        backtrack([w], w[1])

    return ans

print(wordSquares(["area","lead","wall","lady","ball"]), [
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
])


print(wordSquares(["abat","baba","atan","atal"]), [
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
])
