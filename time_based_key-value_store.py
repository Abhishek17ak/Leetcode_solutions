'''
Brute Force Method
For each get operation, scan through all stored values for the key linearly 
to find the most recent value with timestamp ≤ given timestamp.

Time Complexity:

set: O(1)

get: O(n) where n is the number of values for the key

Space Complexity: O(n) for storing all key-value-timestamp tuples
class TimeMap:
    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.keyStore.get(key, [])
        res = ""
        for value, ts in values:
            if ts <= timestamp:
                res = value
        return res

'''
'''
Optimal Method (Binary Search)
Since timestamps are in strictly increasing order, 
use binary search to efficiently find the most recent value with timestamp ≤ given timestamp.

Time Complexity:

set: O(1) (append to list)

get: O(log n) where n is the number of values for the key

Space Complexity: O(n) for storing all key-value-timestamp tuples
'''


class TimeMap:
    def __init__(self):
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])  # Add to end (timestamps increasing)

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        
        while l <= r:                           # Binary search
            m = (l + r) // 2
            if values[m][1] <= timestamp:       # Valid timestamp found
                res = values[m][0]              # Update result
                l = m + 1                       # Look for more recent valid timestamp
            else:                               # Timestamp too large
                r = m - 1                       # Search left half
        return res
