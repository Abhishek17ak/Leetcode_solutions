'''
Brute Force Method (Recursion)
Try all possible paths recursively: at each step, you can move to i+1 or i+2, and take the minimum cost among all possible paths.

Time Complexity: O(2ⁿ) (exponential, as each step branches into two choices)

Space Complexity: O(n) (recursion stack)

def minCostClimbingStairs(cost):
    def dfs(i):
        if i >= len(cost):
            return 0
        return cost[i] + min(dfs(i+1), dfs(i+2))
    return min(dfs(0), dfs(1))

'''
'''
Optimal Method (Bottom-Up Dynamic Programming, In-Place)
Work backwards from the end, updating each step with the minimum cost to reach the top. At each step, the minimum cost to reach the top is the cost at that step plus the minimum cost of the next one or two steps.

Time Complexity: O(n) (one pass through the array)

Space Complexity: O(1) (in-place modification)
'''


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Work backwards from the end, updating each step with minimum cost to reach top
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        
        # Choose the cheaper starting point (step 0 or step 1)
        return min(cost[0], cost[1])
