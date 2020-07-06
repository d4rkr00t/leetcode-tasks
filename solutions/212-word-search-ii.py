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


def findWords(board: [[str]], words: [str]) -> [str]:
    trie = {}

    for w in words:
        cur = trie
        for c in w:
            cur[c] = cur.get(c, {})
            cur = cur[c]

        cur['$'] = w

    ans = set()

    def dfs(i, j, trie):
        if '$' in trie:
            ans.add(trie['$'])

        ch = board[i][j]
        board[i][j] = "#"

        for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ix = i + x
            jy = j + y

            if ix >= 0 and ix < len(board) and jy >= 0 and jy < len(board[0]):
                if board[ix][jy] in trie:
                    dfs(ix, jy, trie[board[ix][jy]])

        board[i][j] = ch

    for i in range(len(board)):
        for j in range(len(board[0])):
            c = board[i][j]
            if c in trie:
                dfs(i, j, trie[c])

    return list(ans)


print(findWords([
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
], ["oath", "pea", "eat", "rain"]), ["oath", "eat"])
