# Number of Good Ways to Split a String
# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/
# medium
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def numSplits(s: str) -> int:
    n = len(s)
    prefix = [0] * n
    suffix = [0] * n
    ans = 0

    freq = set()
    for i, ch in enumerate(s):
        freq.add(ch)
        prefix[i] = len(freq)

    freq = set()
    for i, ch in reversed(list(enumerate(s))):
        freq.add(ch)
        suffix[i] = len(freq)

    for i in range(1, n):
        if prefix[i - 1] == suffix[i]:
            ans += 1

    return ans


print(numSplits("aacaba"), 2)
print(numSplits("abcd"), 1)

# aacaba
# --
# { a:4,c:1,b:1 }
# { }
# --
# { a:3,c:1,b:1 }
# { a:1 }
# --
# { a:2,c:1,b:1 }
# { a:2 }
# --
# { a:2, b:1 }
# { a:2, c:1 }
