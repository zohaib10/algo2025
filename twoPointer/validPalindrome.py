# 125. Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all 
# non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

def validPalindrome(s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and not s[i].isalpha() and not s[i].isnumeric():
                i += 1
            while i < j and not s[j].isalpha() and not s[j].isnumeric():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
assert validPalindrome("A man, a plan, a canal: Panama") == True

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
assert validPalindrome("race a car") == False


# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
assert validPalindrome(" ") == True

# Example 4:
# Input: s = "0P"
# Output: false
assert validPalindrome("0P") == False

