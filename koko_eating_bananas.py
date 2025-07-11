'''
Brute Force Method
Try every possible eating speed k from 1 up to the largest pile size. For each k, 
calculate the total hours required to eat all bananas at that speed. Return the k smallest 
where the total hours is less than or equal to h


Time Complexity: O(max(piles) x n) (inefficient if pile sizes are large)

Space Complexity: O(1)

import math
def minEatingSpeed(piles, h):
    for k in range(1, max(piles) + 1):
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)
        if hours <= h:
            return k

'''
'''(binary search on speeds between 1 to k)
This code finds the minimum eating speed (bananas per hour) that allows Koko to eat all 
banana piles within h hours. Koko can only eat from one pile per hour, 
and if she finishes a pile early, she waits until the next hour.
Time Complexity: O(n x log(max(piles))) (efficient even for large pile sizes)

Space Complexity: O(1)
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)               # Search range: 1 to max pile size
        res = r                            # Track minimum valid speed found
        
        while l <= r:                      # Binary search
            k = (l + r) // 2               # Try this eating speed
            hours = 0                      # Calculate total hours needed
            
            for p in piles:                # For each pile
                hours += math.ceil(p / k)  # Hours to finish this pile
                
            if hours <= h:                 # Can finish within time limit
                res = min(res, k)          # Update minimum speed
                r = k - 1                  # Try slower speeds
            else:                          # Takes too long
                l = k + 1                  # Need faster speed
                
        return res
