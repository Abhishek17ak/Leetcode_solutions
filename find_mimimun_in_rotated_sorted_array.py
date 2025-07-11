'''
Brute Force Method
Scan through the entire array linearly to find the minimum element.

Time Complexity: O(n) (linear scan through all elements)

Space Complexity: O(1)

def findMin(nums):
    return min(nums)

'''
'''
Optimal Method (Binary Search)
Use binary search to find the minimum element by identifying which half of the array contains the rotation point. The key insight is that in a rotated sorted array, one half will always be properly sorted.

Time Complexity: O(log n) (binary search)

Space Complexity: O(1)
'''

def findMin(nums):
    res = nums[0]                       # Track minimum found so far
    l, r = 0, len(nums) - 1             # Binary search pointers
    
    while l <= r:
        if nums[l] < nums[r]:           # Left half is sorted, min is at left
            res = min(res, nums[l])
            break
        
        m = (l + r) // 2                # Find middle
        res = min(res, nums[m])         # Update minimum
        
        if nums[m] >= nums[l]:          # Left half is sorted
            l = m + 1                   # Search right half (has rotation point)
        else:                           # Right half is sorted
            r = m - 1                   # Search left half (has rotation point)
    
    return res

        