# Add and Search Word - Data structure design
# https://leetcode.com/problems/add-and-search-word-data-structure-design/
# medium
#
# Tags: Facebook, Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """

        cur = self.trie

        for c in word:
            cur[c] = cur.get(c, {})
            cur = cur[c]

        cur['$'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        return self.dfs(word, 0, self.trie)

    def dfs(self, word, pos, trie):
        if pos == len(word):
            if '$' in trie:
                return True

            return False

        c = word[pos]

        if c == ".":
            return any([self.dfs(word, pos + 1, trie[key] for key in trie.keys())])
        elif c in trie:
            return self.dfs(word, pos+1, trie[c])

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
