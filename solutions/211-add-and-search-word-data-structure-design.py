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
# Trie

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
        trie = self.trie
        for c in word:
            if not c in trie:
                trie[c] = {}

            trie = trie[c]

        trie["$"] = True


    def __search__(self, word, trie) -> bool:

        if not word:
            if "$" in trie:
                return True

            return False

        c = word[0]

        if c == ".":
            word = word[1:]
            for k in trie.keys():
                if k != "$" and self.__search__(word, trie[k]):
                    return True

            return False

        elif c not in trie:
            return False

        return self.__search__(word[1:], trie[c])

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        return self.__search__(word, self.trie)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
