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
    trie = {}
    ans = set()

    for w in words:
        cur = trie
        for c in w:
            cur[c] = cur.get(c, {})
            cur = cur[c]

        cur['$'] = w

    def dfs(word, i, j, trie):
        nonlocal board, ans

        if '$' in trie:
            ans.add(trie['$'])

        ch = board[i][j]
        word += ch
        board[i][j] = "#"

        for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ix = x + i
            jy = y + j

            if ix >= 0 and ix < len(board) and jy >= 0 and jy < len(board[0]):
                if board[ix][jy] in trie:
                    dfs(word, ix, jy, trie[board[ix][jy]])

        board[i][j] = ch

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] in trie:
                dfs("", i, j, trie[board[i][j]])

    return list(ans)


print(findWords([
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
], ["oath", "pea", "eat", "rain"]), ["oath", "eat"])
