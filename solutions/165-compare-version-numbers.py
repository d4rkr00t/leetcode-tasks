# Compare Version Numbers
# https://leetcode.com/problems/compare-version-numbers/
# medium
#
# Tags: Amazon, Microsoft, Google
#
# Time:  O(max(v1,v2))
# Space: O(max(v1,v2))
#
# Solution:
# TBD

def compareVersion(version1: str, version2: str) -> int:
    v1 = version1.split(".")
    v2 = version2.split(".")
    def comp(p1, p2):
        if p1 >= len(v1) and p2 >= len(v2):
            return 0

        rev1 = int(v1[p1]) if p1 < len(v1) else 0
        rev2 = int(v2[p2]) if p2 < len(v2) else 0

        if rev1 == rev2:
            return comp(p1+1, p2+1)

        return -1 if rev1 < rev2 else 1

    return comp(0, 0)

print(compareVersion(version1 = "0.1", version2 = "1.1"), -1)
print(compareVersion(version1 = "1.0.1", version2 = "1"), 1)
print(compareVersion(version1 = "7.5.2.4", version2 = "7.5.3"), -1)
print(compareVersion(version1 = "1.01", version2 = "1.001"), 0)
print(compareVersion(version1 = "1.0", version2 = "1.0.0"), 0)
