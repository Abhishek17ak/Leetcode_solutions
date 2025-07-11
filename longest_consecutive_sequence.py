'''
Brute Force Method
Sort the array and then iterate through it to find the longest consecutive sequence by checking adjacent elements.

Time Complexity: O(n log n) (due to sorting)

Space Complexity: O(n) (for sorted array or if sorting in-place)
def longestConsecutive(nums):
    if not nums:
        return 0
    nums = sorted(set(nums))  # Sort and remove duplicates
    longest = 1
    current = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            current += 1
        else:
            longest = max(longest, current)
            current = 1
    return max(longest, current)

'''
'''
Use a set for O(1) lookups. For each number, only start counting a sequence if the number just before it is not in the set (meaning this number is the start of a sequence). Then count consecutive numbers forward.

Time Complexity: O(n) (each element visited at most twice)

Space Complexity: O(n) (for the set)
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)                    # Convert to set for O(1) lookups
        longest = 0                           # Track the longest sequence found
        
        for n in nums:                        # Check each number
            if (n - 1) not in numSet:         # Is this the START of a sequence?
                length = 1                    # Start counting from this number
                while (n + length) in numSet: # Keep extending the sequence
                    length += 1
                longest = max(length, longest) # Update longest if needed
        
        return longest
