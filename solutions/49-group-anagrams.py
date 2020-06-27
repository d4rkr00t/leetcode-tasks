# Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# medium
#
# Tags: Amazon, Microsoft, Facebook, Google
#
# Time:  (n * k * log(k))
# Space: O(n * k)
#
# Solution:
# TBD

def groupAnagrams(strs: [str]) -> [[str]]:
    ht = {}

    for s in strs:
      ss = str(sorted(s))
      ht[ss] = ht.get(ss, [])
      ht[ss].append(s)

    return list(ht.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]), [
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
])
