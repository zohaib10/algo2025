# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

import heapq
from collections import defaultdict

def topKFrequentElements(nums, k):

    myDict = defaultdict(int)

    for num in nums:
        myDict[num] += 1

    max_heap = []
    for key, val in myDict.items():
        heapq.heappush(max_heap, (-val, key))

    res = []
    while max_heap:
        key, val = heapq.heappop(max_heap)
        res.append(val)
        if len(res) == k:
            return res

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
print(topKFrequentElements([1,1,1,2,2,3,3,3,3], 2))