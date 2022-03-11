# String Transforms Into Another String
# https://leetcode.com/problems/string-transforms-into-another-string/
# hard
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from gettext import find


def canConvert(str1: str, str2: str) -> bool:
    if str1 == str2:
        return True

    cm = {}
    uniq = set()

    for ch1, ch2 in zip(str1, str2):
        if ch1 in cm and cm[ch1] != ch2:
            return False
        cm[ch1] = ch2
        uniq.add(ch2)

    return len(uniq) < 26


print(canConvert(str1="ab", str2="ba"), True)
print(canConvert(str1="aabcc", str2="ccdee"), True)
print(canConvert(str1="leetcode", str2="codeleet"), False)
print(
    canConvert(str1="abcdefghijklmnopqrstuvwxyz",
               str2="bcdefghijklmnopqrstuvwxyza"), False)

# ab
# ba
#
# ab
# ca
# ba
#
#
# a -> c
# c -> b
# b -> a
