class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""                                # Store the longest palindrome found
        resLen = 0                              # Length of longest palindrome

        for i in range(len(s)):                 # Try each position as center
            # Check for odd-length palindromes (center is single character)
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:        # Found longer palindrome
                    res = s[l:r+1]              # Update result
                    resLen = r - l + 1          # Update length
                l -= 1                          # Expand left
                r += 1                          # Expand right

            # Check for even-length palindromes (center is between characters)
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:        # Found longer palindrome
                    res = s[l:r+1]              # Update result
                    resLen = r - l + 1          # Update length
                l -= 1                          # Expand left
                r += 1                          # Expand right

        return res                              # Return the longest palindrome
