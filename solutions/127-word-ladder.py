# Word Ladder
# https://leetcode.com/problems/word-ladder/
# medium
#
# Tags: Amazon, Google, Facebook, Microsoft
#
# Time:  O(M^2 * N)
# Space: O(M^2 * N)
#
# Solution:
# BFS

def ladderLength(beginWord: str, endWord: str, wordList: [str]) -> int:
    stack = [(beginWord, 1)]
    ans = 0
    transforms = {}
    wordList = [beginWord] + wordList
    processed = set()

    for w in wordList:
        for i in range(len(w)):
            k = w[:i] + "*" + w[i+1:]
            if not k in transforms:
                transforms[k] = []

            transforms[k].append(w)


    while stack:
        cur, level = stack.pop(0)

        for i in range(len(cur)):
            k = cur[:i] + "*" + cur[i+1:]

            for w in transforms[k]:
                if w == endWord:
                    return level + 1

                if w not in processed:
                    processed.add(w)
                    stack.append((w, level + 1))

    return ans

print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]), 5)
print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]), 0)
