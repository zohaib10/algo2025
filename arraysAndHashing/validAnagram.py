"""
 Valid Anagram

 Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

 An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.

"""

from tests.valid_anagram_test_cases import TEST_CASES


class Solution:
    def isAnagram(self, s1: str, s2: str) -> bool:
        tracker = {}
        for s in s1:
            if s in tracker:
                tracker[s] = tracker[s] + 1
            else:
                tracker[s] = 1

        for s in s2:
            if s not in tracker:
                return False
            elif tracker[s] > 1:
                tracker[s] -= 1
            else:
                del tracker[s]

        return len(tracker) == 0


runner = Solution()

for s, t, expected in TEST_CASES:
    actual = runner.isAnagram(s, t)
    assert (
        actual == expected
    ), f"Failed on s={s}, t={t}: expected {expected}, got {actual}"

print("All tests passed!")
