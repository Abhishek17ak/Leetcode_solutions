'''
Brute Force Method
For every possible substring, check if it can be made into a substring 
of a single character with at most k replacements. Track the maximum length.

Time Complexity: O(n³) (O(n²) substrings, O(n) to count frequencies for each)

Space Complexity: O(n) (for character frequency count in a substring)

def characterReplacement(s, k):
    n = len(s)
    res = 0
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j+1]
            maxf = max(sub.count(c) for c in set(sub))
            if (j - i + 1) - maxf <= k:
                res = max(res, j - i + 1)
    return res

'''
'''
Use a sliding window. Track the frequency of characters in the window and the count 
of the most frequent character. If the window size minus the max frequency exceeds k,
shrink the window from the left.

Time Complexity: O(n) (each character is visited at most twice)

Space Complexity: O(1) (since there are at most 26 uppercase letters)
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}                          # Count characters in current window
        res = 0                             # Maximum length found
        l = 0                               # Left pointer (start of window)
        maxf = 0                            # Maximum frequency of any character
        
        for r in range(len(s)):             # Right pointer (end of window)
            count[s[r]] = 1 + count.get(s[r], 0)  # Add current character to count
            maxf = max(maxf, count[s[r]])   # Update maximum frequency
            
            while (r - l + 1) - maxf > k:   # If window needs too many changes
                count[s[l]] -= 1            # Remove leftmost character
                l += 1                      # Shrink window from left
                
            res = max(res, r - l + 1)       # Update maximum length
        
        return res
