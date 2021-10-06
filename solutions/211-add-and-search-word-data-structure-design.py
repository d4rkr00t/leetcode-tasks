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
        self.word = False

    def add(self, word):
        if not word:
            self.word = True
            return

        if word[0] not in self.trie:
            self.trie[word[0]] = Trie()

        self.trie[word[0]].add(word[1:])

    def search(self, word):
        if not word:
            return self.word

        if word[0] == ".":
            subword = word[1:]
            for _, trie in self.trie.items():
                if trie.search(subword):
                    return True
            return False

        if word[0] in self.trie:
            return self.trie[word[0]].search(word[1:])

        return False


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.root.add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.root.search(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
