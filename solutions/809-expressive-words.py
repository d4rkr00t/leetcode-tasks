# Expressive Words
# https://leetcode.com/problems/expressive-words/
# medium
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def expressiveWords(S: str, words: List[str]) -> int:
    def group(word):
        res = []
        prev = ""

        for ch in word:
            if prev and ch != prev[0]:
                res.append(prev)
                prev = ch
            else:
                prev += ch

        res.append(prev)
        return res

    ans = 0
    sGroups = group(S)
    for word in words:
        wGroup = group(word)
        if len(sGroups) != len(wGroup):
            continue

        for g1, g2 in zip(sGroups, wGroup):
            if g1 == g2: continue
            if len(g1) < len(g2): break
            if not g1.startswith(g2): break
            if len(g1) < 3: break
        else:
            ans += 1

    return ans


print(expressiveWords("heeellooo", ["hello", "hi", "helo"]), 1)
print(expressiveWords("zzzzzyyyyy", ["zzyy", "zy", "zyy"]), 3)
