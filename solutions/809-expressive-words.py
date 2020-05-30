# Expressive Words
# https://leetcode.com/problems/expressive-words/
# medium
#
# Tags: Google
#
# Time:  O(QK)
# Space: O(K)
#
# Solution:
# TBD

def expressiveWords(S: str, words: [str]) -> int:
    def RLE(s):
        r = ""
        counts = []
        for c in s:
            if not r:
                r = c
                counts = [1]
                continue

            if r[-1] == c:
                counts[-1] += 1
            else:
                r += c
                counts.append(1)

        return (r, counts)

    r, count = RLE(S)

    ans = 0
    for word in words:
        r2, count2 = RLE(word)
        if r2 != r: continue

        ans += all(c1 >= max(c2, 3) or c1 == c2 for c1, c2 in zip(count, count2))

    return ans


print(expressiveWords("heeellooo", ["hello", "hi", "helo"]), 1)
