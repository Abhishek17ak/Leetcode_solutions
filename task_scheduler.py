'''
Brute Force Method
Simulate the task execution by trying all possible orderings and picking the one with minimum cycles. For each cycle, check which tasks are available (not in cooldown) and execute one.

Time Complexity: O(n! × m) where n is number of unique tasks, m is total tasks (exponential due to trying all permutations)

Space Complexity: O(m) for tracking task states
def leastInterval(tasks, n):
    from collections import Counter
    count = Counter(tasks)
    
    def simulate(remaining, last_used, time):
        if not any(remaining.values()):
            return time
        
        min_time = float('inf')
        for task in remaining:
            if remaining[task] > 0 and time - last_used.get(task, -n-1) > n:
                remaining[task] -= 1
                last_used[task] = time
                min_time = min(min_time, simulate(remaining, last_used, time + 1))
                remaining[task] += 1
        
        if min_time == float('inf'):
            return simulate(remaining, last_used, time + 1)
        return min_time
    
    return simulate(count, {}, 0)

'''
'''
Optimal Method (Max Heap + Queue for Cooldown)
Use a max heap to always execute the most frequent task available. 
Use a queue to track tasks in cooldown period. 
The heap ensures we prioritize tasks with higher frequency, 
and the queue manages the cooldown timing.

Time Complexity: O(m log k) where m is total tasks, k is unique tasks 
(each task processed once, heap operations are O(log k))

Space Complexity: O(k) for heap and queue storage
'''

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) 
        #each task occurance counter
        maxHeap=[-cnt for cnt in count.values()]
        #negative for converting minheap to maxheap
        heapq.heapify(maxHeap)
        time=0
        q = deque()                              # Queue: [remaining_count, available_time]
        
        while maxHeap or q:                      # While tasks remain
            time += 1

            if not maxHeap:                      # No tasks ready, fast-forward
                time = q[0][1]
            else:                               # Execute most frequent task
                cnt = 1 + heapq.heappop(maxHeap)  # Reduce count by 1
                if cnt:                          # If task has more instances
                    q.append([cnt, time + n])    # Add to cooldown queue
                    
            if q and q[0][1] == time:           # Check if any task is ready
                heapq.heappush(maxHeap, q.popleft()[0])  # Move back to heap
                
        return time