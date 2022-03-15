# Number of Matching Subsequences
# https://leetcode.com/problems/number-of-matching-subsequences/
# medium
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# Trie

from collections import defaultdict
from email.policy import default
from typing import List


class Trie:
    def __init__(self, word) -> None:
        self.trie = defaultdict(list)
        for i, ch in enumerate(word):
            self.trie[ch].append(Trie(word[i + 1:]))

    def match(self, word, pos=0):
        if pos == len(word):
            return True

        ch = word[pos]
        if ch in self.trie:
            for child in self.trie[ch]:
                if child.match(word, pos + 1):
                    return True

        return False


def numMatchingSubseq(s: str, words: List[str]) -> int:
    trie = Trie(s)
    count = 0
    for w in words:
        if trie.match(w):
            count += 1

    return count


print(numMatchingSubseq(s="abcde", words=["a", "bb", "acd", "ace"]), 3)
print(
    numMatchingSubseq(s="dsahjpjauf",
                      words=["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]), 2)
