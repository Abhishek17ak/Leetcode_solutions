class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)         # DP array: can we break string from position i?
        dp[len(s)] = True                   # Base case: empty string can always be "broken"

        for i in range(len(s) - 1, -1, -1): # Work backwards from end to start
            for w in wordDict:              # Try each word in dictionary
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]  # Can break if rest can be broken
                if dp[i]:                   # Found a valid break, stop trying more words
                    break

        return dp[0]                        # Can we break the entire string?
