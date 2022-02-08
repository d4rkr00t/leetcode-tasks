# Race Car
# https://leetcode.com/problems/race-car/
# hard
#
# Tags: Google, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD
import collections
import math


def racecar(target: int) -> int:
    queue = collections.deque([(0, 1)])
    high = 2**math.ceil(math.log(target) / math.log(2))
    seen = {(0, 1)}
    res = 0

    while queue:
        for _ in range(len(queue)):
            pos, speed = queue.popleft()
            if pos == target:
                return res

            x, y = (pos + speed, speed * 2), (pos, -1 if speed > 0 else 1)
            if x not in seen and 0 < x[0] <= high:
                queue.append(x)
                seen.add(x)
            if y not in seen and 0 < y[0] <= high:
                queue.append(y)
                seen.add(y)

        res += 1

    return res


print(racecar(3), 2)
print(racecar(6), 5)

# target = 0 1 2 3 4 5 6
# pos =        |
# speed = -2
# commands = [AARA]
# 0 = ""
# 1 = "A"
# 2 = "ARA"
# 3 = "AA", "ARARA"
# 4 = "ARAA"
