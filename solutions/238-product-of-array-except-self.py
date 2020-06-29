# Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# medium
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def productExceptSelf(nums: [int]) -> [int]:
    s = 1
    lr = []
    for n in nums:
        s = s * n
        lr.append(s)

    s = 1
    rl = []
    for n in nums[::-1]:
        s = s * n
        rl.append(s)

    rl = rl[::-1]

    ans = []

    for i in range(len(nums)):
        l = 1 if i-1 < 0 else lr[i-1]
        r = 1 if i+1 >= len(rl) else rl[i+1]

        ans.append(l*r)

    return ans

print(productExceptSelf([1,2,3,4]), [24,12,8,6])

# 24 12 8  6
#
# 1  2  6  24
# 24 24 12  4
#
