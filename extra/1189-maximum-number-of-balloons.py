# Maximum Number of Balloons
# https://leetcode.com/problems/maximum-number-of-balloons/
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


def maxNumberOfBalloons(text: str) -> int:
    counter = collections.Counter(text)
    ans = float("inf")
    table = set(["l", "o"])

    for ch in "balon":
        if ch not in counter:
            return 0

        div = 1 if ch not in table else 2
        ans = min(counter[ch] // div, ans)

    return ans


print(maxNumberOfBalloons("nlaebolko"), 1)
print(maxNumberOfBalloons("loonbalxballpoon"), 2)
print(maxNumberOfBalloons("leetcode"), 0)
