# Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# medium
#
# Tags: Amazon, Microsoft, Facebook, Google
#
# Time:  O(N * M*log(M))
# Space: O(N)
#
# Solution:
# Sort + Group

from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    ans = {}

    for s in strs:
        s_sorted = "".join(sorted(s))
        ans[s_sorted] = ans.get(s_sorted, [])
        ans[s_sorted].append(s)

    return list(ans.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]), [
    ["ate", "eat", "tea"],
    ["nat", "tan"],
    ["bat"]
])
