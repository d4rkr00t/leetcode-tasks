# Reverse Only Letters
# https://leetcode.com/problems/reverse-only-letters/
# easy
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def reverseOnlyLetters(s: str) -> str:
    start = 0
    end = len(s) - 1
    s = list(s)

    while start < end:
        s_ch = s[start]
        e_ch = s[end]

        if not s_ch.isalpha():
            start += 1
            continue
        elif not e_ch.isalpha():
            end -= 1
            continue

        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

    return "".join(s)


print(reverseOnlyLetters("ab-cd"), "dc-ba")
print(reverseOnlyLetters("a-bC-dEf-ghIj"), "j-Ih-gfE-dCba")
print(reverseOnlyLetters("Test1ng-Leet=code-Q!"), "Qedo1ct-eeLg=ntse-T!")
