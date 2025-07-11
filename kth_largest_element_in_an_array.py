'''
Brute Force Method
Sort the array in descending order and return the element at index k-1.

Time Complexity: O(n log n) (sorting the entire array)

Space Complexity: O(1) if sorting in-place, O(n) if creating new sorted array

def findKthLargest(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]

'''
'''
Optimal Method (Min Heap of Size k)
Maintain a min heap of exactly k elements containing the k largest elements seen so far.
The root of this heap is always the kth largest element.

Time Complexity: O(n log k) (each insertion/deletion is O(log k), done n times)

Space Complexity: O(k) (heap stores at most k elements)
'''

import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a min heap to store the k largest elements
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)  # Add current number to heap
            
            # If heap size exceeds k, remove the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # The root of min heap is the kth largest element
        return min_heap[0]
'''"I can solve this with heapq.nlargest() for a clean one-liner,
 or implement a manual min heap to demonstrate the underlying algorithm.
  Which would you prefer to see?"
  class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]
  '''
