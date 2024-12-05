# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.



def validAnagram(s1, s2):
    if len(s1) != len(s2):
        return False

    letters = [0] * 26
    
    for i in s1:
        idx = ord(i) -  ord('a')
        letters[idx] += 1
    
    for j in s2:
        idx = ord(j) - ord('a')
        letters[idx] -= 1

    for k in letters:
        if k != 0:
            return False
        
    return True


# Example 1 -> Input: s = "anagram", t = "nagaram" -> Output: true
assert validAnagram("anagram", "nagaram") == True

# Example 2 -> Input: s = "rat", t = "car" -> Output: false
assert validAnagram("rat", "car") == False