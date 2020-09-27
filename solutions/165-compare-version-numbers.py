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

    v1 = v1 + (['0'] * max(len(v2) - len(v1), 0))
    v2 = v2 + (['0'] * max(len(v1) - len(v2), 0))

    for n1, n2 in zip(v1, v2):
        if int(n1) > int(n2):
            return 1
        elif int(n1) < int(n2):
            return -1

    return 0


print(compareVersion(version1="0.1", version2="1.1"), -1)
print(compareVersion(version1="1.0.1", version2="1"), 1)
print(compareVersion(version1="7.5.2.4", version2="7.5.3"), -1)
print(compareVersion(version1="1.01", version2="1.001"), 0)
print(compareVersion(version1="1.0", version2="1.0.0"), 0)
