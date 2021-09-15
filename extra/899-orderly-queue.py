# Orderly Queue
# https://leetcode.com/problems/orderly-queue/
# hard
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def orderlyQueue(s: str, k: int) -> str:
    if k == 1:
        return min(s[i:] + s[:i] for i in range(len(s)))
    else:
        return ''.join(sorted(s))


print(orderlyQueue(s="dedba", k=1), "adedb")
print(orderlyQueue(s="cba", k=1), "acb")
print(orderlyQueue(s="baaca", k=3), "aaabc")
print(orderlyQueue(s="xmvzi", k=2), "imvxz")

# xmvzi
# mvzix
# vzixm
# zixmv
# ixmvz
# imvzx
