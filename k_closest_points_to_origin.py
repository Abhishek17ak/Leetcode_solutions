'''
Brute Force Method
Calculate the distance for all points, sort them by distance, and return the first k points.

Time Complexity: O(n log n) (sorting all points by distance)

Space Complexity: O(n) (for storing distances and result)
def kClosest(points, k):
    distances = []
    for x, y in points:
        dist = (x**2) + (y**2)
        distances.append([dist, x, y])
    distances.sort()
    return [[x, y] for dist, x, y in distances[:k]]

'''
'''
Optimal Method (Min Heap)
Use a min heap to store all points with their distances. 
The heap automatically maintains the closest points at the top, 
allowing efficient extraction of the k closest points.

Time Complexity: O(n + k log n) (heapify is O(n), k extractions are O(k log n))

Space Complexity: O(n) (heap storage and result)
'''


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        for x,y in points:
            dist=(x**2)+(y**2)
            minHeap.append([dist,x,y])
            #we take two points and append it to minHeap with distance creating 3 ele list
        heapq.heapify(minHeap)
        res=[]
        while k>0:
            dist,x,y=heapq.heappop(minHeap)#we get k lowest(min) points from minHeap to res
            #min points= closest
            res.append([x,y])
            k-=1
        return res