# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# link: https://leetcode.com/problems/group-anagrams/description/

from collections import defaultdict
from validAnagram import validAnagram

def groupAnagrams_On2K(strs):
    grouped = {}
    for s in strs:
        found = False
        for key in grouped.keys():
            if validAnagram(key, s):
                grouped[key].append(s)
                found = True
        if not found:
            grouped[s] = [s]

    print("On^2 * K", list(grouped.values()))

def groupAnagrams_On(strs):
    myDict = defaultdict(list)
    for s in strs:
        letters = [0] * 26
        for i in s:
            idx = ord(i) - ord('a')
            letters[idx] += 1
        myDict[tuple(letters)].append(s)
    print("On * K", list(myDict.values()))


def groupAnagrams(strs):
    groupAnagrams_On(strs)
    groupAnagrams_On2K(strs)

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
groupAnagrams(["eat","tea","tan","ate","nat","bat"])

# Example 2: 
# Input: strs = [""]
# Output: [[""]]
groupAnagrams([""]) 

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
groupAnagrams(["a"])