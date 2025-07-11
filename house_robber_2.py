'''
Brute Force Method
Try all possible combinations recursively, but with the extra constraint that you cannot rob both the first and last house. This is not practical for large inputs.

Time Complexity: O(2ⁿ) (exponential, as each house can be robbed or skipped)

Space Complexity: O(n) (recursion stack)
def rob(nums):
    def dfs(i, first_robbed):
        if i >= len(nums):
            return 0
        if i == len(nums) - 1 and first_robbed:
            return 0  # Can't rob the last if first was robbed
        return max(nums[i] + dfs(i+2, first_robbed or i==0), dfs(i+1, first_robbed))
    return dfs(0, False)

'''
'''
Optimal Method (Dynamic Programming, O(1) Space)
Since the first and last houses are adjacent, you can't rob both.
Key Insight:

Rob from house 0 to n-2 (skip last)

Rob from house 1 to n-1 (skip first)

Take the maximum of the two

For each case, use the standard House Robber I DP.

Time Complexity: O(n) (two passes through the list)

Space Complexity: O(1) (constant space, just two variables per pass)
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], 
                   self.helper(nums[1:]),      # Skip first house, rob from house 1 to end
                   self.helper(nums[:-1]))     # Skip last house, rob from house 0 to second-last

    def helper(self, nums):                    # Same logic as House Robber I
        rob1, rob2 = 0, 0
        for num in nums:
            newRob = max(rob1 + num, rob2)     # Rob current OR skip current
            rob1 = rob2
            rob2 = newRob
        return rob2
