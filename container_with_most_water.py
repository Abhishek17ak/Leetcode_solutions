'''Brute Force Method
Check every pair of bars (i, j), calculate the area they form as a container, 
and keep track of the maximum area found.

Time Complexity: O(n²) (since you check all pairs)

Space Complexity: O(1) (only a few variables for tracking)
def maxArea(height):
    n = len(height)
    max_area = 0
    for i in range(n):
        for j in range(i + 1, n):
            area = (j - i) * min(height[i], height[j])
            max_area = max(max_area, area)
    return max_area

'''
'''
Use two pointers, one at the start and one at the end of the array. Calculate the area, update the maximum, and move the pointer pointing to the shorter bar inward. Repeat until the pointers meet.

Time Complexity: O(n) (each bar is considered at most once)

Space Complexity: O(1) (constant extra space)
'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a = 0                               # Track maximum area found
        l, r = 0, len(heights) - 1         # Two pointers: left and right
        
        while l < r:                        # While pointers haven't met
            area = (r - l) * min(heights[l], heights[r])  # Calculate current area
            a = max(a, area)                # Update maximum area
            
            if heights[l] < heights[r]:     # Move the shorter line
                l += 1                      # Move left pointer right
            else:
                r -= 1                      # Move right pointer left
        
        return a
