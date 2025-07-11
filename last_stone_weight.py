'''
Brute Force Method
Sort the array after each stone smash to always get the two heaviest stones. Remove the heaviest stones, calculate the result, and add back if needed.

Time Complexity: O(n² log n) (sort after each operation, up to n operations)

Space Complexity: O(1) (sorting in-place, only a few variables)

def lastStoneWeight(stones):
    while len(stones) > 1:
        stones.sort()
        first = stones.pop()
        second = stones.pop()
        if first != second:
            stones.append(first - second)
    return stones[0] if stones else 0

'''
'''
Optimal Method (Max Heap)
Use a max heap to efficiently get the two heaviest stones. Since Python's heapq is a min heap, convert all values to negative to simulate a max heap.

Time Complexity: O(n log n) (heapify is O(n), each of the n operations is O(log n))

Space Complexity: O(n) (heap storage)
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones]
        #we dont have maxheap so we convert all values to negative to use minheap as maxheap
        heapq.heapify(stones)

        while len(stones)>1:#we want to resturn single remaining value
            first = heapq.heappop(stones)#largest value
            second=heapq.heappop(stones)#second largest value
            if second!=first:
                heapq.heappush(stones,first-second)#we simulate the battle and add result
            #as second and first are oposite , take in reverse like first-second instead of opp
            
        return abs(stones[0]) if stones else 0
        