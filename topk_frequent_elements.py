'''
Brute Force Method
Count the frequency of each element, then sort the unique elements by frequency and return the top k.

Time Complexity: O(n log n) (counting is O(n), sorting by frequency is O(n log n))

Space Complexity: O(n) (for frequency map and result)
def topKFrequent(nums, k):
    count = {}
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in sorted_items[:k]]
'''
'''
Optimal Method (Min Heap)
Time: (n log k)
Space: (n+k)
n= len of array, k = no. of top frequent elements
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each number
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Step 2: Use min-heap to keep track of top k frequent elements
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))  # Push (frequency, number)
            if len(heap) > k:                        # Keep only k elements
                heapq.heappop(heap)                  # Remove least frequent

        # Step 3: Extract results from heap
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])       # Get the number (not frequency)
        return res

