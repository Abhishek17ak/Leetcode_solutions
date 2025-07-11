#dp(n)=1+dp(n-1)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)        # DP array, initialized to "impossible"
        dp[0] = 0                               # Base case: 0 coins needed for amount 0

        for a in range(1, amount + 1):          # For each amount from 1 to target
            for c in coins:                     # Try each coin
                if a - c >= 0:                  # Can we use this coin?
                    dp[a] = min(dp[a], 1 + dp[a - c])  # Take minimum coins
                    
        return dp[amount] if dp[amount] != amount + 1 else -1  # Return result or -1
