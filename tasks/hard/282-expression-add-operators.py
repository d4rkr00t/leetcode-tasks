# Expression Add Operators
# https://leetcode.com/problems/expression-add-operators/
# hard
#
# Tags: Facebook, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def addOperators(num: str, target: int) -> List[str]:
    pass


print(addOperators(num="123", target=6), ["1+2+3", "1*2*3"])
print(addOperators(num="232", target=8), ["2*3+2", "2+3*2"])
print(addOperators(num="105", target=5), ["1*0+5", "10-5"])
print(addOperators(num="00", target=0), ["0+0", "0-0", "0*0"])
print(addOperators(num="3456237490", target=9191), [])
