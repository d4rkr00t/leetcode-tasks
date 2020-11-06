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


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = {}
        self.query = ""

        for s, t in zip(sentences, times):
            self.__add__(s, t)

    def __add__(self, sentence, times):
        cur = self.trie
        for c in sentence:
            cur[c] = cur.get(c, {})
            cur = cur[c]

        (count, _) = cur.get('#', (0, ""))
        cur['#'] = (count + times, sentence)

    def __get_sentences__(self, trie):
        res = []

        for c in trie.keys():
            if c == "#":
                res.append(trie[c])
            else:
                res.extend(self.__get_sentences__(trie[c]))

        return res

    def __find__(self, query):
        cur = self.trie

        for c in query:
            if c not in cur:
                return []
            cur = cur[c]

        return self.__get_sentences__(cur)

    def __sort__(self, sentences):
        return list(sorted([(-t, s) for t, s in sentences]))

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.__add__(self.query, 1)
            self.query = ""
            return []

        self.query += c
        sentences = self.__sort__(self.__find__(self.query))
        return [s for t, s in sentences[:3]]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
