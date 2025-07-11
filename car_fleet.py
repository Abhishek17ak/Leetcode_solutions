'''
Brute Force Method
For each car, simulate its movement, and check if it catches up to any car ahead before reaching the target. Merge cars into fleets as they catch up.

Time Complexity: O(n²) (each car may need to check all cars ahead)

Space Complexity: O(n) (for fleet tracking)

def carFleet(target, position, speed):
    n = len(position)
    fleets = [i for i in range(n)]
    times = [(target - position[i]) / speed[i] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if position[i] < position[j] and times[i] <= times[j]:
                fleets[i] = fleets[j]
    return len(set(fleets))

'''
'''
Optimal Method (Sort + Stack)
Sort cars by position from closest to farthest from the target. 
For each car, compute its arrival time. Use a stack to track fleets: 
if a car's arrival time is less than or equal to the fleet ahead, it joins that fleet.

Time Complexity: O(n log n) (for sorting)

Space Complexity: O(n) (for the stack)
'''


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]  # Combine position and speed
        pair.sort(reverse=True)                           # Sort by position (closest to target first)
        stack = []                                        # Stack to track arrival times
        
        for p, s in pair:                                 # Process cars from closest to farthest
            stack.append((target - p) / s)               # Calculate time to reach target
            if len(stack) >= 2 and stack[-1] <= stack[-2]:  # Current car catches up?
                stack.pop()                               # Remove current car (forms fleet)
                
        return len(stack)                                 # Number of fleets
