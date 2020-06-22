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
# Trie

class Node:
    def __init__(self):
        self.is_word = False
        self.children = [None] * 26


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def get_char_pos(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        pos = 0
        node = self.root

        while pos < len(word):
            ch = word[pos]
            ch_pos = self.get_char_pos(ch)

            if node.children[ch_pos]:
                node = node.children[ch_pos]
            else:
                node.children[ch_pos] = Node()
                node = node.children[ch_pos]

            pos += 1

        node.is_word = True


def findWords(board: [[str]], words: [str]) -> [str]:
    ans = []
    trie = Trie()

    for w in words:
        trie.insert(w)

    def dfs(i, j, node, s):
        if node.is_word:
            ans.append(s)
            node.is_word = False

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == '#':
            return

        node = node.children[trie.get_char_pos(board[i][j])]

        if not node:
            return

        ch = board[i][j]
        board[i][j] = '#'

        for dh, dv in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dfs(i+dv, j+dh, node, s + ch)

        board[i][j] = ch

    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(i, j, trie.root, "")

    return list(sorted(ans))

print(findWords([
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
], ["oath","pea","eat","rain"]), ["oath", "eat"])

print(findWords([["a","b"],["c","d"]], ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]))

print(findWords([["b","a","a","b","a","b"],["a","b","a","a","a","a"],["a","b","a","a","a","b"],["a","b","a","b","b","a"],["a","a","b","b","a","b"],["a","a","b","b","b","a"],["a","a","b","a","a","b"]], ["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]))
