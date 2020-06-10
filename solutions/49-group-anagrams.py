# Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# medium
#
# Tags: Amazon, Microsoft, Facebook, Google
#
# Time:  O(n*w log w) where w is a length of a word
# Space: O(n)
#
# Solution:
# TBD

def groupAnagrams(strs: [str]) -> [[str]]:
    ht = {}

    for w in strs:
      sw = "".join(sorted(w))

      if sw in ht:
        ht[sw].append(w)
      else:
        ht[sw] = [w]

    return list(ht.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]), [
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
])
