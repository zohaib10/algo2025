
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation: The element 1 occurs at the indices 0 and 3.



def containsDuplicates(nums):
    mySet = set()

    for n in nums:
        if n in mySet:
            return True
        mySet.add(n)

    return False


assert containsDuplicates([1,2,3,1]) == True
assert containsDuplicates([1,2,3,4]) == False
assert containsDuplicates([1,1,1,3,3,4,3,2,4,2]) == True

# Tested with Leetcode https://leetcode.com/problems/contains-duplicate/description/