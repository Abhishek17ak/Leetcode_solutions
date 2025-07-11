class Solution:
    def numDecodings(self, s: str) -> int:
        dp = dp2 = 0                            # dp = current, dp2 = two positions ahead
        dp1 = 1                                 # dp1 = one position ahead (base case)
        
        for i in range(len(s) - 1, -1, -1):    # Process from right to left
            if s[i] == "0":                     # Can't decode single '0'
                dp = 0
            else:                               # Can decode single digit
                dp = dp1
            
            # Check if we can decode two digits
            if i + 1 < len(s) and (s[i] == "1" or
               s[i] == "2" and s[i + 1] in "0123456"):
                dp += dp2                       # Add ways from two positions ahead
                
            dp, dp1, dp2 = 0, dp, dp1          # Shift variables for next iteration
            
        return dp1                              # Return result
