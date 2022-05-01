# Compare Version Numbers
# https://leetcode.com/problems/compare-version-numbers/
# medium
#
# Tags: Amazon, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def compareVersion(version1: str, version2: str) -> int:
    v1 = version1.split(".")
    v2 = version2.split(".")

    for i in range(max(len(v1), len(v2))):
        n1 = int(v1[i]) if i < len(v1) else 0
        n2 = int(v2[i]) if i < len(v2) else 0

        if n1 > n2:
            return 1
        elif n1 < n2:
            return -1

    return 0


print(compareVersion(version1="0.1", version2="1.1"), -1)
print(compareVersion(version1="1.0.1", version2="1"), 1)
print(compareVersion(version1="7.5.2.4", version2="7.5.3"), -1)
print(compareVersion(version1="1.01", version2="1.001"), 0)
print(compareVersion(version1="1.0", version2="1.0.0"), 0)
