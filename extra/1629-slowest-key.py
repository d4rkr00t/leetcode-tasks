# Slowest Key
# https://leetcode.com/problems/slowest-key/
# easy
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def slowestKey(releaseTimes: List[int], keysPressed: str) -> str:
    key = ""
    dur = prev = 0

    for rt, k in zip(releaseTimes, list(keysPressed)):
        new_dur = rt - prev
        if new_dur > dur:
            dur = new_dur
            key = k
        elif new_dur == dur:
            if k > key:
                key = k
        prev = rt

    return key


print(slowestKey(releaseTimes=[9, 29, 49, 50], keysPressed="cbcd"), "c")
print(slowestKey(releaseTimes=[12, 23, 36, 46, 62], keysPressed="spuda"), "a")
