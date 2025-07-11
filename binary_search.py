'''
Brute Force Method
Scan through the array from left to right and return the index 
if the target is found, otherwise return -1.

Time Complexity: O(n) (linear scan)

Space Complexity: O(1)

def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

'''
'''
Optimal Method (Binary Search)
Use binary search: repeatedly divide the search interval in half. 
If the value of the search key is less than the item in the middle, 
narrow the interval to the lower half. Otherwise, narrow it to the upper half. 
Continue until the value is found or the interval is empty.

Time Complexity: O(log n) (halves the search space each time)

Space Complexity: O(1)
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)  
            if nums[m] > target:
                r = m
            elif nums[m] <= target:
                l = m + 1
        return l - 1 if (l and nums[l - 1] == target) else -1