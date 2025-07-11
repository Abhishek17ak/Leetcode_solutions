class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0                                 # Count of palindromic substrings
        
        for i in range(len(s)):                 # Try each position as center
            # Check for odd-length palindromes (center is single character)
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1                        # Found a palindrome, count it
                l -= 1                          # Expand left
                r += 1                          # Expand right

            # Check for even-length palindromes (center is between characters)
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1                        # Found a palindrome, count it
                l -= 1                          # Expand left
                r += 1                          # Expand right
        
        return res                              # Total count of palindromes
