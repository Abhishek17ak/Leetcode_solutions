'''
Brute Force Method
Check every pair of elements in the array to see if any two are equal.

Time Complexity: O(n²)

Space Complexity: O(1)
 def containsDuplicate(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False

'''
'''
Optimal Method (Using Hash Set)
Iterate through the array, adding each element to a set. If an element is already in the set, return True.

Time Complexity: O(n)

Space Complexity: O(n)

Optimal Code (With Short Comments):
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False