# Add and Search Word - Data structure design
# https://leetcode.com/problems/add-and-search-word-data-structure-design/
# medium
#
# Tags: Facebook, Amazon, Google
#
# Time:  insert = O(m), m = len(word),
#        search = O(m) best case, O(m*n) where n is len(word) and n number of keys in m first layers
# Space: O(K) – K = length of unique prefixes
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
        cur = self.trie
        for ch in word:
            cur[ch] = cur.get(ch, {})
            cur = cur[ch]

        cur['$'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        queue = [(self.trie, 0)]

        while queue:
            cur, pos = queue.pop(0)
            ch = word[pos] if pos < len(word) else ""

            if pos == len(word) and '$' in cur:
                return True

            if ch not in cur and ch != ".":
                continue

            if ch == ".":
                for k in cur.keys():
                    if k != "$":
                        queue.append((cur[k], pos + 1))
            else:
                queue.append((cur[ch], pos + 1))

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
