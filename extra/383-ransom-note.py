# Ransom Note
# https://leetcode.com/problems/ransom-note/
# easy
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

import collections


def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    rc = collections.Counter(ransomNote)
    mc = collections.Counter(magazine)

    for k in rc.keys():
        if rc[k] > mc[k]:
            return False

    return True
