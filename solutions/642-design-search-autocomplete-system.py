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

class TrieNode:
    def __init__(self):
        self.trie = {}

    def insert(self, sentence, times):
        trie = self.trie

        for c in sentence:
            trie[c] = trie.get(c, {})
            trie = trie[c]

        trie['$'] = trie.get('$', (0, sentence))
        trie['$'] = (trie['$'][0] - times, sentence)


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = TrieNode()
        self.current_trie = self.trie.trie
        self.query = ""

        for s, t in zip(sentences, times):
            self.trie.insert(s, t)

    def get_sentences(self, trie, res=[]):
        if '$' in trie:
            res.append(trie['$'])

        for c in trie.keys():
            if c == '$':
                continue

            self.get_sentences(trie[c], res)

        return res

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.trie.insert(self.query, 1)
            self.current_trie = self.trie.trie
            self.query = ""
            return []

        if c in self.current_trie.keys():
            self.current_trie = self.current_trie[c]

        sentences = sorted(self.get_sentences(self.current_trie))

        return [s for t, s in sentences]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
