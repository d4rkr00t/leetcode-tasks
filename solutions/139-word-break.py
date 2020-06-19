# Word Break
# https://leetcode.com/problems/word-break/
# medium
#
# Tags: Amazon, Facebook, Google, Microsoft
#
# Time:  O(n^2)
# Space: O(n)
#
# Solution:
# TBD

def wordBreak(s: str, wordDict: [str]) -> bool:
    cache = {}
    def backtrack(p):
        nonlocal s, cache, wordDict

        if p in cache:
            return cache[p]

        if p == len(s):
            return True

        for w in wordDict:
            if s.startswith(w, p):
                if backtrack(p + len(w)):
                    cache[p] = True
                    return True

        cache[p] = False
        return False

    return backtrack(0)

print(wordBreak(s = "leetcode", wordDict = ["leet", "code"]), True)
print(wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]), True)
print(wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]), False)
