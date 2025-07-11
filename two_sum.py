'''
Brute Force Method
Check every pair of indices (i, j) and return the first pair where nums[i] + nums[j] == target.

Time Complexity: O(n²)

Space Complexity: O(1)

def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

'''

'''Optimal Method (Hash Map)
Use a hash map to store each number and its index as you iterate. For each number, check if target - num is already in the map.

Time Complexity: O(n)

Space Complexity: O(n)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapi = {}                           # Dictionary to store: value → index
        for i, n in enumerate(nums):        # Loop through array with index and value
            diff = target - n               # Calculate what number we need to find
            if diff in mapi:                # Check if we've seen the needed number before
                return [mapi[diff], i]      # Found it! Return both indices
            mapi[n] = i                     # Store current number and its index
