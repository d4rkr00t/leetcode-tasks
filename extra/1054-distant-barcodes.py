# Distant Barcodes
# https://leetcode.com/problems/distant-barcodes/
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
import heapq
import collections


def rearrangeBarcodes(barcodes: List[int]) -> List[int]:
    if len(barcodes) <= 2:
        return barcodes

    counts = collections.Counter(barcodes)
    hq = []
    ans = []
    for k in counts.keys():
        heapq.heappush(hq, (-counts[k], k))

    while len(hq) >= 2:
        cc, cur = heapq.heappop(hq)
        nc, next = heapq.heappop(hq)
        ans.append(cur)
        ans.append(next)
        cc += 1
        nc += 1

        if cc < 0:
            heapq.heappush(hq, (cc, cur))

        if nc < 0:
            heapq.heappush(hq, (nc, next))

    if hq:
        cc, cur = heapq.heappop(hq)
        ans.append(cur)

    return ans


print(rearrangeBarcodes([1, 1, 1, 2, 2, 2]), [2, 1, 2, 1, 2, 1])
print(rearrangeBarcodes([1, 1, 1, 1, 2, 2, 3, 3]), [1, 3, 1, 3, 2, 1, 2, 1])
