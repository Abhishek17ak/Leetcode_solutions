'''
Brute Force Method
Check all possible triplets (i, j, k) with i < j < k and see if their sum is zero. Store unique triplets using a set to avoid duplicates.

Time Complexity: O(n³)

Space Complexity: O(n²) (for storing unique triplets)

def threeSum(nums):
    n = len(nums)
    res = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    res.add(triplet)
    return [list(triplet) for triplet in res]
'''
'''
Sort the array. For each number, use two pointers to find pairs that 
sum to the negative of the current number. Skip duplicates to ensure unique triplets.

Time Complexity: O(n²)

Space Complexity: O(1) (not counting the output list)
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []                              # Store all valid triplets
        nums.sort()                           # Sort array first
        
        for i, a in enumerate(nums):          # Fix first number 'a'
            if a > 0:                         # Early termination optimization
                break
            if i > 0 and a == nums[i-1]:      # Skip duplicate 'a' values
                continue
                
            l, r = i + 1, len(nums) - 1       # Two pointers for remaining numbers
            while l < r:                      # Find pairs that sum with 'a' to 0
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:              # Sum too big, need smaller number
                    r -= 1
                elif threeSum < 0:            # Sum too small, need bigger number
                    l += 1
                else:                         # Found valid triplet!
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:  # Skip duplicate 'l' values
                        l += 1
        return res
