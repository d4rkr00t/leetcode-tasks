# Word Search II
# https://leetcode.com/problems/word-search-ii/
# hard
#
# Tags: Amazon, Microsoft, Google, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    prefix = set()
    words = set(words)
    ans = set()

    for w in words:
        for i in range(len(w)):
            key = w[:i + 1]
            prefix.add(key)

    def dfs(i, j, cur):
        val = board[i][j]
        board[i][j] = "#"
        cur += val

        if cur in words:
            ans.add(cur)

        for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ix = i + x
            jy = j + y

            if ix >= 0 and ix < len(board) and jy >= 0 and jy < len(board[1]):
                if board[ix][jy] != "#":
                    dfs(ix, jy, cur)

        board[i][j] = val

    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(i, j, "")

    return list(ans)


print(
    findWords([['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'],
               ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']],
              ["oath", "pea", "eat", "rain"]), ["oath", "eat"])
