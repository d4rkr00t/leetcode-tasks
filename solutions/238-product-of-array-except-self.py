# Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# medium
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  O(n)
# Space: O(1)

def productExceptSelf(nums: [int]) -> [int]:
    l = len(nums)
    answer = [0] * l
    answer[0] = 1

    for i in range(1, l):
        answer[i] = nums[i-1] * answer[i-1]

    r = 1
    for i in range(l)[::-1]:
        answer[i] = answer[i] * r
        r *= nums[i]

    return answer

print(productExceptSelf([1,2,3,4]), [24,12,8,6])
