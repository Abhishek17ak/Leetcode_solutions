'''brute force
Check every possible pair of buy and sell days. For each pair (i, j) where i < j, calculate the profit as prices[j] - prices[i], and keep track of the maximum profit found.

Time Complexity: O(n²) (since you check all pairs)

Space Complexity: O(1) (only a variable to store the max profit)

def maxProfit(prices):
    n = len(prices)
    max_profit = 0
    for i in range(n):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit

'''
'''
Optimal Method (Single Pass, Two Pointers)
Use two pointers: one to track the best day to buy (left), 
and the other to scan possible sell days (right). If selling on the right day is profitable,
update the maximum profit. If not, move the buy pointer to the current day.

Time Complexity: O(n) (each price is checked once)

Space Complexity: O(1) (constant extra space)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1                         # Two pointers: buy day (l), sell day (r)
        P = 0                               # Maximum profit found so far
        
        while r < len(prices):              # Check all possible sell days
            if prices[l] < prices[r]:       # Can make profit?
                profit = prices[r] - prices[l]  # Calculate current profit
                P = max(P, profit)          # Update maximum profit
            else:                           # Can't make profit
                l = r                       # Move buy day to current sell day
            r += 1                          # Move to next sell day
        
        return P
