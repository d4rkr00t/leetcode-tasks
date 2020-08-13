# Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# medium
#
# Tags: Amazon, Microsoft, Facebook, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = {}

    for s in strs:
        ss = str(sorted(s))
        groups[ss] = groups.get(ss, [])
        groups[ss].append(s)

    return groups.values()


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]), [
    ["ate", "eat", "tea"],
    ["nat", "tan"],
    ["bat"]
])
