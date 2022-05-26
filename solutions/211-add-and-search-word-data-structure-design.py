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


class TrieNode:
    def __init__(self):
        self.word = False
        self.children = [None] * 26


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def __getIdx__(self, ch):
        return ord(ch) - ord("a")

    def add(self, word):
        node = self.root
        for ch in word:
            idx = self.__getIdx__(ch)
            if not node.children[idx]:
                node.children[idx] = TrieNode()

            node = node.children[idx]

        node.word = True

    def __find__(self, word, pos, node):
        if pos == len(word):
            return node.word

        ch = word[pos]
        idx = self.__getIdx__(ch)

        if ch == ".":
            for child in node.children:
                if child and self.__find__(word, pos + 1, child):
                    return True

            return False

        return node.children[idx] and self.__find__(word, pos + 1,
                                                    node.children[idx])

    def find(self, word):
        return self.__find__(word, 0, self.root)


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


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
