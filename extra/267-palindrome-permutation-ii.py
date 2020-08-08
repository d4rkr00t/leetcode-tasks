# Palindrome Permutation II
# https://leetcode.com/problems/palindrome-permutation-ii/
# medium
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List
import collections


def generatePalindromes(s: str) -> List[str]:
    hl = len(s) // 2
    cs = [0] * 26
    csu = [0] * 26
    odd = ""
    counts = collections.Counter(s)
    ans = []

    for k in counts.keys():
        if counts[k] % 2 == 0:
            cs[ord(k) - ord("a")] += counts[k]
        else:
            odd = k

    def backtrack(cur):
        if len(cur) == hl:
            if len(s) % 2 == 1:
                ans.append("".join(cur + [odd] + cur[::-1]))
            else:
                ans.append("".join(cur + cur[::-1]))
            return

        for ch in counts.keys():
            k = ord(ch) - ord("a")
            if cs[k] <= 0:
                continue

            cs[k] -= 1
            csu[k] += 1
            cur.append(ch)
            if cs[k] >= csu[k]:
                backtrack(cur)

            cs[k] += 1
            csu[k] -= 1
            cur.pop()

    backtrack([])

    return ans


print(generatePalindromes("aabb"), ["abba", "baab"])
print(generatePalindromes("aacbb"), ["abcba", "bacab"])
print(generatePalindromes("abc"), [])

# ab
# ba
