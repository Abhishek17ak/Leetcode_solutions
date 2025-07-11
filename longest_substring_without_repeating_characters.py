'''
Brute Force Method
Check every possible substring and determine if it contains all unique characters. Track the maximum length found.

Time Complexity: O(n³) (O(n²) substrings, O(n) to check uniqueness for each)

Space Complexity: O(n) (for checking uniqueness in a substring)

def lengthOfLongestSubstring(s):
    n = len(s)
    max_len = 0
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)
    return max_len

'''
'''
Optimal Method (Sliding Window + HashSet)
Use a sliding window with two pointers and a set to track unique characters 
in the current window. When a duplicate is found, move the left pointer until 
the duplicate is removed.

Time Complexity: O(n) (each character is added and removed from the set at most once)

Space Complexity: O(min(n, m)), where m is the charset size (for the set)
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()                     # Track characters in current window
        l = 0                               # Left pointer (start of window)
        res = 0                             # Maximum length found
        
        for r in range(len(s)):             # Right pointer (end of window)
            while s[r] in charSet:          # If duplicate found
                charSet.remove(s[l])        # Remove leftmost character
                l += 1                      # Shrink window from left
            charSet.add(s[r])               # Add current character
            res = max(res, r - l + 1)       # Update maximum length
        
        return res
