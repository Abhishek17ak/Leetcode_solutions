'''
Brute Force Method
Scan through the entire array linearly to find the target element and return its index.

Time Complexity: O(n) (linear scan through all elements)

Space Complexity: O(1)

def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

'''
'''
Optimal Method (Modified Binary Search)
Use binary search with the key insight that in a rotated sorted array, 
at least one half (left or right) will always be properly sorted. 
Determine which half is sorted, then check if the target lies within that sorted half's range.

Time Complexity: O(log n) (binary search)

Space Complexity: O(1)
'''
def search(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:          # Found target
            return mid
        
        if nums[l] <= nums[mid]:         # Left half is sorted
            if target > nums[mid] or target < nums[l]:  # Target not in left half
                l = mid + 1              # Search right half
            else:                        # Target is in left half
                r = mid - 1              # Search left half
        else:                            # Right half is sorted
            if target < nums[mid] or target > nums[r]:  # Target not in right half
                r = mid - 1              # Search left half
            else:                        # Target is in right half
                l = mid + 1              # Search right half
    
    return -1                            # Target not found

