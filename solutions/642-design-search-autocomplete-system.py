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
    def __init__(self):
        self.trie = {}

    def insert(self, sentence, times):
        cur = self.trie
        for c in sentence:
            cur[c] = cur.get(c, {})
            cur = cur[c]

        cur['$'] = cur.get('$', {"times": 0, "sentence": sentence})
        cur['$']["times"] += times

    def __find__(self, input):
        cur = self.trie
        pos = 0

        while cur and pos < len(input):
            if input[pos] in cur:
                cur = cur[input[pos]]
                pos += 1
            else:
                return None

        return cur

    def get_sentence(self, node, sentences):
        if '$' in node:
            sentences.append((-node['$']["times"], node['$']["sentence"]))

        for k in node.keys():
            if k != "$":
                self.get_sentence(node[k], sentences)

        return sentences

    def get_sentences(self, input):
        node = self.__find__(input)
        if not node:
            return []

        return self.get_sentence(node, [])


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.query = ""
        self.trie = Trie()

        for s, t in zip(sentences, times):
            self.trie.insert(s, t)

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.trie.insert(self.query, 1)
            self.query = ""
            return []

        self.query += c
        sentences = self.trie.get_sentences(self.query)

        if sentences:
            return [s for t, s in sorted(sentences)[:3]]

        return []


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
