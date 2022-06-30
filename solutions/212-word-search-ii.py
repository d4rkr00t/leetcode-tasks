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


class Trie:
    def __init__(self) -> None:
        self.children = [None] * 26

    def insert(self, ch):
        pos = ord(ch) - ord("a")
        if not self.children[pos]:
            child = Trie()
            self.children[pos] = child
        return self.children[pos]

    def find(self, word, idx=0):
        if idx == len(word):
            return True

        ch = word[idx]
        pos = ord(ch) - ord("a")

        if not self.children[pos]:
            return False

        return self.children[pos].find(word, idx + 1)


def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    # 1. Build Trie
    trie = Trie()
    n = len(board)
    m = len(board[0])

    def inBounds(x, y):
        return x >= 0 and x < n and y >= 0 and y < m

    def dfs(x, y, trie):
        ch = board[x][y]
        board[x][y] = "#"
        childTrie = trie.insert(ch)

        for i, j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ix = x + i
            jy = y + j
            if inBounds(ix, jy) and board[ix][jy] != "#":
                dfs(ix, jy, childTrie)

        board[x][y] = ch

    for x in range(n):
        for y in range(m):
            dfs(x, y, trie)

    # 2. Find words
    ans = []

    for w in words:
        if trie.find(w):
            ans.append(w)

    return ans


print(
    findWords([['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'],
               ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']],
              ["oath", "pea", "eat", "rain"]), ["oath", "eat"])
