# Guess the Word
# https://leetcode.com/problems/guess-the-word/
# hard
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def findSecretWord(wordlist: List[str], master) -> None:
    matches = master.guess(wordlist[0])
    used = set([wordlist[0]])
    cur = wordlist[0]
    guess = 0
    disq = [[False] * 26 for _ in range(6)]

    def pick(cur, words, matches):
        res = []
        for w in words:
            if w in used:
                continue

            t = 0
            d = False
            for i in range(6):
                if cur[i] == w[i]:
                    t += 1

                if disq[i][ord(w[i]) - ord("a")]:
                    d = True
                    break

            if d:
                continue

            if t >= matches:
                res.append(w)

        return res

    next = pick()

    while matches < 6:
        word = next[0]
        next_matches = master.guess(word)

        if next_matches == 0:
            for i, ch in enumerate(word):
                disq[i][ord(ch) - ord("a")] = True

        if next_matches >= matches:
            matches = next_matches
            cur = word

        next = pick(cur, next, matches)


# secret = "acckzz"
# wordlist = ["ccbazz","eiowzz","abcczz", "acckzz", "ccbrty"]
#
# acckzz
# ccbazz = 3
# ccbrty = 1

# "cymplm"
# ["eykdft","gjeixr","eksbjm","mxqhpk","tjplhf","ejgdra","npkysm",
# "jsrsid","cymplm","vegdgt","jnhdvb","jdhlzb","sgrghh","jvydne","laxvnm",
# "xbcliw","emnfcw","pyzdnq"]
#  eykdft = 1
# ["ejgdra", "npkysm", "cymplm", "laxvnm", "emnfcw"]
#  eksbjm = 1
#  ejgdra = 0
#
