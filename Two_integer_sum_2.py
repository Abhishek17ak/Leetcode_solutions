'''
Brute Force Method
Check every pair of indices (i, j) to see if their sum equals the target. 
Return the first valid pair.

Time Complexity: O(n²)

Space Complexity: O(1)

def twoSum(numbers, target):
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]  # 1-indexed

'''
'''
Use two pointers (left and right) since the array is sorted. 
Move pointers inward based on the sum compared to the target.

Time Complexity: O(n)

Space Complexity: O(1)
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1          # Two pointers: left and right
        
        while l < r:                        # While pointers haven't met
            curSum = numbers[l] + numbers[r]  # Calculate current sum
            
            if curSum > target:             # Sum too big, need smaller numbers
                r -= 1                      # Move right pointer left (smaller values)
            elif curSum < target:           # Sum too small, need bigger numbers
                l += 1                      # Move left pointer right (bigger values)
            else:                           # Found exact match!
                return [l + 1, r + 1]       # Return 1-indexed positions
        
        return []                           # No solution found (shouldn't happen per problem)
