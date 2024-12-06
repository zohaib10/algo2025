# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

def topKFrequentElements(nums, k):
    myDict = {}
    myList = [[] for i in range(len(nums) + 1)]

    for num in nums:
        if num in myDict:
           myDict[num] += 1
        else:
            myDict[num] = 1

    for key, v in myDict.items():
        myList[key].append(v)

    res = []
    for i in range(len(myList) - 1, 0, -1):
        for j in myList[i]:
            res.append(j)
            if len(res) == k:
                return res

    

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
print(topKFrequentElements([1,1,1,2,2,3], 2))

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
print(topKFrequentElements([1], 1))