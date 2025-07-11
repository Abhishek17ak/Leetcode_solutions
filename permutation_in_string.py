
'''
Brute Force Method
For every possible substring, check if it can be made into a substring of a single character with at most k replacements. Track the maximum length.

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
Optimal Method (Sliding Window + Hash Map)
Use a sliding window. Track the frequency of characters in the window and the count of the most frequent character. If the window size minus the max frequency exceeds k, shrink the window from the left.

Time Complexity: O(n) (each character is visited at most twice)

Space Complexity: O(1) (since there are at most 26 uppercase letters)
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):                    # Impossible case
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26   # Character frequency arrays
        
        # Count characters in s1 and first window of s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        # Count how many character frequencies match
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        # Sliding window through rest of s2
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:                    # All frequencies match!
                return True
            
            # Add new character (expand window)
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # Remove old character (shrink window)
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
            
        return matches == 26                     # Check final window
