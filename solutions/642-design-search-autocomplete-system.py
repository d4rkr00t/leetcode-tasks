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
# Trie

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

class TrieNode:
    def __init__(self, sentence = False, full = "", times = 0):
        self.letters = {}
        self.sentence = sentence
        self.full = full
        self.times = 0

    def add(self, sentence, times):
        cur = self

        for i,c in enumerate(sentence):
            if c in cur.letters:
                cur = cur.letters[c]
                if i == len(sentence) - 1:
                    cur.times += times
            else:
                cur.letters[c] = TrieNode()
                cur = cur.letters[c]

        cur.sentence = True
        cur.full = sentence
        cur.times = max(cur.times, times)

    def find(self, query):
        cur = self

        for c in query:
            if c in cur.letters:
                cur = cur.letters[c]
            else:
                cur = None
                break

        if not cur:
            return []

        return self.get_sentences(cur)

    def get_sentences(self, trie):
        results = []
        if trie.sentence:
            results = [(trie.times, trie.full)]

        for t in trie.letters.values():
            results.extend(self.get_sentences(t))

        return results


class AutocompleteSystem:

    def __init__(self, sentences: [str], times: [int]):
        self.trie = TrieNode()
        self.query = ""
        for s,t in zip(sentences, times):
            self.trie.add(s, t)

    def input(self, c: str) -> [str]:
        if c == "#":
            self.trie.add(self.query, 1)
            self.query = ""
            return []

        self.query += c
        results = self.trie.find(self.query)

        def cmp(x,y):
            if x[0] == y[0]:
                for i in range(min(len(x[1]), len(y[1]))):
                    if ord(x[1][i]) > ord(y[1][i]):
                        return -1
                    elif ord(x[1][i]) < ord(y[1][i]):
                        return 1

                return 0
            return x[0] - y[0]

        return [sentence for times, sentence in sorted(results, key=cmp_to_key(cmp), reverse=True)[:3]]


auto = AutocompleteSystem(["abc","abbc","a"],[3,3,3])

print(auto.input("b"), [])
print(auto.input("c"), [])
print(auto.input("#"), [])
print(auto.input("b"), ["bc"])
print(auto.input("c"), ["bc"])
print(auto.input("#"), [])
print(auto.input("a"), ["a","abbc","abc"])
print(auto.input("b"), ["abbc","abc"])
print(auto.input("c"), ["abc"])
print(auto.input("#"), [])
print(auto.input("a"), ["abc","a","abbc"])
print(auto.input("b"), ["abc", "abbc"])
print(auto.input("c"), ["abc"])
print(auto.input("#"), [])

# [null,["i love you","island","i love leetcode"],["i love you","i love leetcode"],[],[],["i love you","island","i love leetcode"],["i love you","i love leetcode"],[],[],["i love you","island","i love leetcode"],["i love you","i love leetcode"],[],[]]
# [null,["i love you","island","i love leetcode"],["i love you","i love leetcode"],[],[],["i love you","island","i love leetcode"],["i love you","i love leetcode","i a"],["i a"],[],["i love you","island","i a"],["i love you","i a","i love leetcode"],["i a"],[]]

# ["AutocompleteSystem","input","input","input","input","input","input","input","input","input","input","input","input","input","input"]
# [[["abc","abbc","a"],[3,3,3]],["b"],["c"],["#"],["b"],["c"],["#"],["a"],["b"],["c"],["#"],["a"],["b"],["c"],["#"]]

# [null,[],[],[],["bc"],["bc"],[],["a","abbc","abc"],["abbc","abc"],["abc"],[],["abc","a","abbc"],["abc","abbc"],["abc"],[]]
