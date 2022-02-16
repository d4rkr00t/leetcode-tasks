# Design Search Autocomplete System
# https://leetcode.com/problems/design-search-autocomplete-system/
# hard
#
# Tags: Amazon, Google, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


class Trie:
    def __init__(self) -> None:
        self.trie = {}
        self.count = 0
        self.sentence = ""

    def add(self, query, count=1, pos=0):
        if pos >= len(query):
            self.count += count
            self.sentence = query
            return

        ch = query[pos]
        if not ch in self.trie:
            self.trie[ch] = Trie()

        self.trie[ch].add(query, count, pos + 1)

    def find(self, query, pos=0):
        if pos >= len(query):
            return self.__get_sentences__([])

        ch = query[pos]
        if ch in self.trie:
            return self.trie[ch].find(query, pos + 1)

        return []

    def __get_sentences__(self, res):
        if self.sentence:
            res.append((-self.count, self.sentence))

        for _, trie in self.trie.items():
            trie.__get_sentences__(res)

        return res


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.query = ""
        self.trie = Trie()
        for s, t in zip(sentences, times):
            self.trie.add(s, t)

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.trie.add(self.query)
            self.query = ""
            return []

        self.query += c
        results = self.trie.find(self.query)

        return [s for _, s in sorted(results)]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
