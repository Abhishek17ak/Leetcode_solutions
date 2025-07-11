'''
Brute Force Method
For each index, compute the product of all elements except the one at that index by multiplying all other elements in a nested loop.

Time Complexity: O(n²)

Space Complexity: O(n) (for the result array)
def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n
    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= nums[j]
        res[i] = prod
    return res

'''
'''
Optimal Method (Prefix and Suffix Products)
Calculate prefix and suffix products for each index and multiply them to get the result. This avoids division and ensures O(n) time.

Time Complexity: O(n)

Space Complexity: O(n) (for prefix, suffix, and result arrays)'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n                    # Result array
        pref = [0] * n                   # Prefix products (left side)
        suff = [0] * n                   # Suffix products (right side)

        # Initialize boundaries
        pref[0] = suff[n - 1] = 1
        
        # Build prefix products (left to right)
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        
        # Build suffix products (right to left)
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        
        # Combine prefix and suffix for final result
        for i in range(n):
            res[i] = pref[i] * suff[i]
        
        return res
#O(n),O(n)
