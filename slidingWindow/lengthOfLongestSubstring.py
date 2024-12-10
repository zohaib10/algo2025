
def lengthOfLongestSubstring(s: str) -> int:
    i = 0
    j = 0
    maxLength = 0
    mySet = set()

    while j < len(s):
        if s[j] not in mySet:
            maxLength = max(maxLength, (j + 1) - i)
        else:
            while s[j] in mySet:
                mySet.remove(s[i])
                i += 1
        mySet.add(s[j])
        j += 1
    return maxLength
        

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
print(lengthOfLongestSubstring("abcabcbb"))

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
print(lengthOfLongestSubstring("bbbbb"))


# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
print(lengthOfLongestSubstring("pwwkew"))
