'''
Brute Force Method
Store all values in a list. For each add operation, sort the entire list and return the kth largest element.

Time Complexity:

Constructor: O(n log n) for initial sorting

add: O(n log n) for sorting after each addition

Space Complexity: O(n) for storing all elements
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
    
    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k - 1]

'''
'''
Optimal Method (Min Heap of Size k)
Maintain a min heap of exactly k elements containing the k largest elements seen so far. The root of this heap is always the kth largest element.

Time Complexity:

Constructor: O(n + (n-k) log k) = O(n log k) for heapify and removing excess elements

add: O(log k) for heap operations

Space Complexity: O(k) for maintaining heap of size k
'''

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap,self.k=nums,k   #initialize
        heapq.heapify(self.minHeap)  #convert to heap
        while len(self.minHeap)>k:
            heapq.heappop(self.minHeap)
    #we want k largest elements, so we keep the heap of k size and pop all smaller values
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)
        # we add a new value and pop the lowest to keep to heap size =k
        return self.minHeap[0]
        
