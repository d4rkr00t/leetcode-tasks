# Word Search II
# https://leetcode.com/problems/word-search-ii/
# hard
#
# Tags: Amazon, Microsoft, Google, Facebook
#
# Time:  O(n*m*w)
# Space: O(n*m)

from typing import List
from collections import defaultdict


def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    table = defaultdict(list)
    ans = []
    n = len(board)
    m = len(board[1])

    for i in range(n):
        for j in range(m):
            table[board[i][j]].append((i, j))

    def dfs(i, j, w, pos):
        nonlocal ans

        if len(w) == pos:
            ans.append(w)
            return

        orig_ch = board[i][j]
        board[i][j] = "#"

        for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ix = i + x
            jy = j + y

            if ix >= 0 and jy >= 0 and ix < n and jy < m and w[pos] == board[
                    ix][jy]:
                dfs(ix, jy, w, pos + 1)

        board[i][j] = orig_ch

    for w in words:
        ch = w[0]
        if ch not in table:
            continue

        for i, j in table[ch]:
            dfs(i, j, w, 1)

    return ans


print(
    findWords([['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'],
               ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']],
              ["oath", "pea", "eat", "rain"]), ["oath", "eat"])
