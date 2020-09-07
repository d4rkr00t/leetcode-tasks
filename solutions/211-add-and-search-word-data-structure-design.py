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

class Trie:
    def __init__(self):
        self.trie = {}
        self.is_word = False

    def add(self, word: str) -> None:
        c = word[0]
        trie = self.trie.get(c, Trie())
        self.trie[c] = trie
        if len(word) > 1:
            trie.add(word[1:])
        else:
            trie.is_word = True

    def find(self, word: str) -> bool:
        if not word and self.is_word:
            return True

        if not word:
            return False

        c = word[0]

        if c not in self.trie and c != ".":
            return False

        if c == ".":
            for k in self.trie.keys():
                if self.trie[k].find(word[1:]):
                    return True

            return False

        return self.trie[c].find(word[1:])


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.trie.add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.trie.find(word)
