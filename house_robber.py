'''
Brute Force Method (Recursive)
Try all possibilities: for each house, decide to rob it (and skip the next) or skip it. Take the maximum over all choices.

Time Complexity: O(2ⁿ) (exponential, as each house branches into two choices)

Space Complexity: O(n) (recursion stack)

def rob(nums):
    def dfs(i):
        if i >= len(nums):
            return 0
        return max(nums[i] + dfs(i+2), dfs(i+1))
    return dfs(0)

'''
'''
Optimal Method (Dynamic Programming, O(1) Space)
Keep track of the maximum money you can rob up to the previous 
house (rob2) and the house before that (rob1). For each house, 
decide whether to rob it (and add to rob1) or skip it (keep rob2). Update the two trackers as you go.

Time Complexity: O(n) (single pass through the list)

Space Complexity: O(1) (constant space, just two variables)
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0                   # Track max money from previous scenarios

        for num in nums:                    # Consider each house
            temp = max(num + rob1, rob2)    # Rob current house OR skip it
            rob1 = rob2                     # Update previous values
            rob2 = temp
        
        return rob2                         # Maximum money we can rob
