# 128. Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

def longestConsecutive(nums) -> int:
    longest = 0
    mySet = set()

    for n in nums:
        mySet.add(n)

    for n in nums:
        if (n - 1) not in mySet:
            length = 0
            while n + length in mySet:
                length += 1
            longest = max(longest, length)
    return longest
    
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
print(longestConsecutive([100,4,200,1,3,2]))

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))