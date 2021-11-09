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
from collections import defaultdict


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)

    for w in strs:
        key = "".join(sorted(w))
        groups[key].append(w)

    return list(groups.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
      [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]])
