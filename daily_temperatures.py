'''
Brute Force Method
For each day, look ahead to find the next day with a warmer temperature. Record the number of days waited, or 0 if none found.

Time Complexity: O(n²) (for each day, may scan all future days)

Space Complexity: O(n) (for the result array)

def dailyTemperatures(temperatures):
    n = len(temperatures)
    res = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if temperatures[j] > temperatures[i]:
                res[i] = j - i
                break
    return res

'''
'''
Optimal Method (Monotonic Stack)
Use a stack to store indices of days with unresolved warmer temperatures. 
For each day, pop from the stack until the current temperature is not warmer 
than the one at the stack's top. For each pop, record the wait in the result array.

Time Complexity: O(n) (each index pushed and popped at most once)

Space Complexity: O(n) (for result array and stack)
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)       # Result array, initialized to 0
        stack = []                          # Stack to store (temperature, index) pairs
        
        for i, t in enumerate(temperatures):    # Process each day
            while stack and t > stack[-1][0]:  # Found a warmer day!
                stackT, stackInd = stack.pop() # Get waiting day info
                res[stackInd] = i - stackInd   # Calculate days to wait
            stack.append((t, i))               # Add current day to stack
            
        return res
