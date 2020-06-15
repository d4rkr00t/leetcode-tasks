# Insert Interval
# https://leetcode.com/problems/insert-interval/
# hard
#
# Tags: Google, Facebook, Amazon
#
# Time:  O(n)
# Space: O(n)

def insert(intervals: [[int]], newInterval: [int]) -> [[int]]:
    ans = []

    joined = newInterval
    inserted = False
    for i,n in enumerate(intervals):
        if n[0] <= joined[1] and n[1] >= joined[0]:
            joined[0] = min(n[0], joined[0])
            joined[1] = max(n[1], joined[1])
        elif n[0] > joined[1]:
            inserted = True
            ans.append(joined)
            ans.extend(intervals[i:])
            break
        else:
            ans.append(n)

    if not inserted:
        ans.append(newInterval)

    return ans


print(insert([[1,3], [6,9]], [2,5]), [[1,5], [6,9]])
print(insert([[1,2], [3,5], [6,7], [8,10], [12,16]], [4,8]), [[1,2], [3,10], [12,16]])

# [4,8]
# [[1,2], | [3,5], [6,7], [8,10], | [12,16]]

