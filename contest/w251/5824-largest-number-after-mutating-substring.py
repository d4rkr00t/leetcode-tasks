# Largest Number After Mutating Substring
# https://leetcode.com/contest/weekly-contest-251/problems/largest-number-after-mutating-substring/
# medium
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def maximumNumber(num: str, change: List[int]) -> str:
    for i, n in enumerate(num):
        ni = int(n)
        r = change[ni]

        if r > ni:
            j = i
            replace = ""
            while j < len(num) and int(num[j]) <= change[int(num[j])]:
                replace += str(change[int(num[j])])
                j += 1

            num = num[:i] + replace + num[j:]
            break

    return num


print(maximumNumber(num="132", change=[9, 8, 5, 0, 3, 6, 4, 2, 6, 8]), "832")
print(maximumNumber(num="021", change=[9, 4, 3, 5, 7, 2, 1, 9, 0, 6]), "934")
print(maximumNumber(num="5", change=[1, 4, 7, 5, 3, 2, 5, 6, 9, 4]), "5")
print(maximumNumber(num="012", change=[1, 4, 7, 5, 3, 2, 5, 6, 9, 4]), "147")
